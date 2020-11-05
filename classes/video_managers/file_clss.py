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
import os
import time
from typing import final
import cv2
import matplotlib.pyplot as plt

from classes.computer_vision.yolo_clss import Yolo


@final
class ResizeVideo:
    """ Class to resize video. """
    def __init__(self, video, video_params):
        self._video_params = video_params
        self._video = video
        self._width = 0
        self._height = 0
        self._output = None

    @property
    def size(self):
        """
        Return the new size of video.
        :return: (Width, Height).
        """
        return self._width, self._height

    @property
    def output(self):
        """
        Returns output property.
        :return: video output.
        """
        return self._output

    def execute(self, file_name):
        """
        Adjust values to video size.
        :return:
        """
        self.resize()
        fourcc = cv2.VideoWriter_fourcc(*self._video_params.codec.codec())
        self._output = cv2.VideoWriter(file_name, fourcc, self._video_params.fps, (self._width, self._height))
        return self

    def resize(self):
        """
        Calculate new size of frame.
        :return: self.
        """
        self._height, self._width, _ = self._video.shape
        if self._width > self._video_params.max_width:
            prop = self._width / self._height
            self._width = self._video_params.max_width
            self._height = int(self._width / prop)
        return self


@final
class FileVideoManager:
    """ This class implements the loading of videos files. """

    FONT_SMALL_SIZE = 0.4
    FONT_DEFAULT_SIZE = 0.6
    FONT_NAME = cv2.FONT_HERSHEY_SIMPLEX

    def __init__(self, file_name, output_path, config, hiper_params, video_params, samples_to_display=0,
                 report=None):
        self._output_path = output_path
        self._video_params = video_params
        self._report = report
        self._config = config
        self._hiper_params = hiper_params
        self._file_name = file_name
        self._samples_to_display = samples_to_display
        self._connected = False
        self._captured = None
        self._video = None
        self._output = None
        self._current_sample = 0
        self._size = (0, 0)

    def _connect(self):
        self._captured = cv2.VideoCapture(self._file_name)
        self._connected, self._video = self._captured.read()
        return self

    def resize_output(self, file_name=None):
        """ Resize output video. """
        resize = ResizeVideo(video=self._video, video_params=self._video_params).execute(file_name)
        self._size = resize.size
        self._output = resize.output
        return self

    def show_image(self, image):
        """ This method shows the image object. """
        img = plt.gcf()
        img.set_size_inches(16, 10)
        plt.axis('off')
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        plt.show()
        return self

    def _output_file_name(self, path):
        """
        Get the output file name.
        :return: Output file name normalized.
        """
        file_name = os.path.join(path, os.path.split(self._file_name)[-1])
        return os.path.normpath(file_name)

    def execute(self):
        """
        Executes image processing.
        :return: self.
        """
        # TODO: Reduzir este método.
        self._connect().resize_output(self._output_file_name(self._output_path))
        try:
            total_time = time.time()
            while cv2.waitKey(1) < 0:
                self._connected, frame = self._captured.read()
                if not self._connected:
                    break

                t = time.time()
                try:
                    frame = cv2.resize(frame, self._size)
                    (H, W) = frame.shape[:2]
                    Yolo('', frame, self._config, self._hiper_params, self._report).execute().get_output()
                except Exception as e:
                    print('Error: ', str(e))
                    continue
                else:
                    self._print_info(H, frame, t, total_time)
                    self._output.write(frame)

            print('Terminou.')
            self._output.release()
        finally:
            cv2.destroyAllWindows()
        return self

    def _print_info(self, height, frame, t, total_time):
        text = ' Frame processado em {:.2f} segundos.'.format(time.time() - t)
        cv2.putText(frame, text, (20, height - 20),
                    self.FONT_NAME, self.FONT_SMALL_SIZE, (250, 250, 250), 0, lineType=cv2.LINE_AA)
        print(text)
        if self._current_sample < self._samples_to_display:
            self.show_image(frame)
            self._current_sample += 1
        print(' Tempo processado em {:.2f} segundos.'.format(time.time() - total_time))
        return self
