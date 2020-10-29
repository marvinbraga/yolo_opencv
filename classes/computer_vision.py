# coding=utf-8
"""
GNU Affero General Public License v3.0

Permissions of this strongest copyleft license are conditioned on making
available complete source code of licensed works and modifications, which
include larger works using a licensed work, under the same license.
Copyright and license notices must be preserved.
Contributors provide an express grant of patent rights.
When a modified version is used to provide a service over a network, the
complete source code of the modified version must be made available.

Marvin Computer Vision Framework, 2020
Marcus Vinicius Braga.
"""
from abc import ABCMeta, abstractmethod
from time import time

import cv2
import numpy as np
import matplotlib.pyplot as plt


class AbstractComputerVision(metaclass=ABCMeta):
    """ Abstract class to Computer Vision operations. """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """ This method execute the principal operation. """
        pass

    @abstractmethod
    def set_image(self, image_file_name):
        """ This method sets the image property. """
        pass

    @abstractmethod
    def get_output(self):
        """ This method create the output file.  """
        pass

    @abstractmethod
    def save_to_file(self, file_name='result.jpg'):
        """ This method saves the predicted result in a file. """
        pass

    @property
    @abstractmethod
    def output(self):
        """  This method gets the output image.  """
        pass

    @property
    @abstractmethod
    def elapsed_time(self):
        """ This method returns the elapsed time from execution. """
        pass


class ImageComputerVision(AbstractComputerVision):
    """ Class to execute computer vision tasks with Yolo4 and OpenCV. """

    def __init__(self, labels_file_name, weights_file_name, config_file_name):
        self._config_file_name = config_file_name
        self._weights_file_name = weights_file_name
        self._labels_file_name = labels_file_name
        # Other properties.
        self._outputs = None
        self._net = None
        self._colors = None
        self._layers_names = None
        self._output_layers_names = None
        self._layer_outputs = None
        self._image = None
        self._image_copy = None
        self._elapsed_time = None
        self._boxes = []
        self._assurances = []
        self._id_classes = []
        # Initialize.
        self._get_labels()._get_weights()

    def set_image(self, image_file_name):
        """ This method sets the image property. """
        self._image = cv2.imread(image_file_name)
        self._image_copy = self._image.copy()
        return self

    @property
    def image(self):
        """ This method returns the image property value. """
        return self._image

    def show_image(self, image):
        """ This method shows the image object. """
        img = plt.gcf()
        img.set_size_inches(16, 10)
        plt.axis('off')
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.show()
        return self

    def execute(self, *args, **kwargs):
        """ This method execute the process to detect labels in image """
        start_time = time()
        try:
            # Converting the image to blob.
            blob = cv2.dnn.blobFromImage(self._image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
            # Send image to RN.
            self._net.setInput(blob)
            # Getting values from RN.
            self._layer_outputs = self._net.forward(self._output_layers_names)
        finally:
            finish_time = time()
            self._elapsed_time = finish_time - start_time
        return self

    def get_output(self):
        """ This method create the output file.  """
        self._get_predict()._get_objects()._make_results()
        return self

    def _get_predict(self, threshold=0.5):
        """
        This method gets predict results.
        :param threshold: Defining the level of certainty for the placement of boxes.
        :return: self.
        """
        (h, w) = self._image.shape[:2]
        # Getting information results...
        for output in self._layer_outputs:
            for detection in output:
                scores = detection[5:]
                classe_id = np.argmax(scores)
                confidence = scores[classe_id]
                if confidence > threshold:
                    # Creating the detection box.
                    box = detection[0:4] * np.array([w, h, w, h])
                    (centerX, centerY, width, height) = box.astype('int')
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    # Saving the detection values.
                    self._boxes.append([x, y, int(width), int(height)])
                    self._assurances.append(float(confidence))
                    self._id_classes.append(classe_id)
        return self

    def _get_objects(self, threshold=0.5, threshold_nns=0.3):
        """
        This method get the output values.
        :param threshold: Defining the level of certainty for the placement of boxes.
        :param threshold_nns: Removing shared boxes with low probability (NO-MAX-SUPPRESSION).
        :return: self.
        """
        self._outputs = cv2.dnn.NMSBoxes(self._boxes, self._assurances, threshold, threshold_nns)
        return self

    @property
    def output(self):
        """  This method gets the output image.  """
        return self._image

    @property
    def elapsed_time(self):
        """ This method returns the elapsed time from execution. """
        return self._elapsed_time

    def _get_labels(self):
        """ This method get the labels from file. """
        self._labels = open(self._labels_file_name).read().strip().split('\n')
        # Define boxes colors.
        self._colors = np.random.randint(0, 255, size=(len(self._labels), 3), dtype='uint8')
        return self

    def _get_weights(self):
        """ This method get the weights from file. """
        self._net = cv2.dnn.readNet(self._config_file_name, self._weights_file_name)
        self._layers_names = self._net.getLayerNames()
        self._output_layers_names = self._net.getUnconnectedOutLayersNames()
        return self

    def _make_results(self):
        """ This method create boxes in image. """
        if len(self._outputs) > 0:
            for i in self._outputs.flatten():
                (x, y) = (self._boxes[i][0], self._boxes[i][1])
                (w, h) = (self._boxes[i][2], self._boxes[i][3])
                color = [int(c) for c in self._colors[self._id_classes[i]]]
                cv2.rectangle(self._image, (x, y), (x + w, y + h), color, 2)
                texto = '{}: {:.4f}'.format(self._labels[self._id_classes[i]], self._assurances[i])
                cv2.putText(self._image, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return self

    def save_to_file(self, file_name='result.jpg'):
        """ This method saves the predicted result in a file. """
        cv2.imwrite(file_name, self._image)
        return self


def start():
    """ Initiate a test. """
    img = '../resources/images/cachorros.jpg'
    weights = '../resources/data/yolov4.weights'
    labels = '../resources/data/coco.names'
    config = '../resources/data/yolov4.cfg'
    cv = ImageComputerVision(labels, weights, config)
    cv.set_image(img).execute().get_output().save_to_file()
    print('Tempo de processamento: {:.2f} seg.'.format(cv.elapsed_time))
    cv.show_image(cv.image)


if __name__ == '__main__':
    start()
