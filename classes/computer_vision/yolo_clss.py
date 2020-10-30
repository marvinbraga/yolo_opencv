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
import cv2
import numpy as np
from time import time

from classes.computer_vision.image_boxes_clss import ImageBox
from classes.computer_vision.yolo import AbstractYolo


class Yolo(AbstractYolo):
    """ This class implements Yolo with OpenCV. """

    def __init__(self, file_name, image, config, hiper_params, report=None):
        self._image = image
        self._image_copy = self._image.copy()
        self._file_name = file_name
        self._config = config
        self._hiper_params = hiper_params
        self._report = report
        # Other properties
        self._net = None
        self._layers_names = None
        self._output_layers_names = None
        self._elapsed_time = None
        self._layer_outputs = None
        self._boxes = []
        self._assurances = []
        self._id_classes = []
        self._get_weights()

    def _get_weights(self):
        """ This method get the weights from file. """
        self._net = cv2.dnn.readNet(self._config.config_file, self._config.weights_file)
        self._layers_names = self._net.getLayerNames()
        self._output_layers_names = self._net.getUnconnectedOutLayersNames()
        return self

    @property
    def elapsed_time(self):
        """ This method returns the elapsed time from execution. """
        return self._elapsed_time

    @property
    def output(self):
        """  This method gets the output image.  """
        return self._image

    def execute(self):
        """ This method execute the process to detect labels in image """
        start_time = time()
        try:
            self._resize_image()
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

    def _resize_image(self, max_width=600):
        """ This method adjusts the image size if its width is greater than 600. """
        image = self._image
        if image.shape[1] > max_width:
            height = int(max_width / (image.shape[1] / image.shape[0]))
            self._image = cv2.resize(image, (max_width, height))
        return self

    def get_output(self):
        """ This method create the output file.  """
        self._get_predict()._get_objects()._make_results()
        return self

    def _get_predict(self):
        """
        This method gets predict results.
        :return: self.
        """
        # TODO: Reduzir método.
        (h, w) = self._image.shape[:2]
        # Getting information results...
        for output in self._layer_outputs:
            for detection in output:
                scores = detection[5:]
                classe_id = np.argmax(scores)
                confidence = scores[classe_id]
                if confidence > self._hiper_params.threshold:
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

    def _get_objects(self):
        """
        This method get the output values.
        :return: self.
        """
        self._outputs = cv2.dnn.NMSBoxes(
            self._boxes, self._assurances, self._hiper_params.threshold, self._hiper_params.threshold_nns)
        return self

    def _make_results(self):
        """ This method create boxes in image. """
        # TODO: Reduzir método.
        if len(self._outputs) > 0:
            for i in self._outputs.flatten():
                # Verify labels.
                label = self._config.labels[self._id_classes[i]]
                # Make boxes.
                (x, y) = (self._boxes[i][0], self._boxes[i][1])
                (w, h) = (self._boxes[i][2], self._boxes[i][3])
                color = [int(c) for c in self._config.colors[self._id_classes[i]]]
                ImageBox(self._image, color, label, self._assurances[i], (x, y), (x + w, y + h)).make()
        return self

    @staticmethod
    def _check_negative(value):
        """ This method adjusts the value if it is less than zero. """
        result = 0 if value < 0 else value
        return result
