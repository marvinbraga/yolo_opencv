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


class ResizeImage:
    """ Class to resize an image. """
    def __init__(self, image):
        self._image = image

    def execute(self, max_width=600):
        """ This method adjusts the image size if its width is greater than 600. """
        image = self._image
        if image.shape[1] > max_width:
            height = int(max_width / (image.shape[1] / image.shape[0]))
            self._image = cv2.resize(image, (max_width, height))
        return self

    @property
    def output(self):
        """ Image adjusted. """
        return self._image