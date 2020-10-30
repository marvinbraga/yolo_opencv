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


class ImageBox:
    """ Create a box in the image. """

    def __init__(self, image, color, label, assurance, position, size):
        self._size = size
        self._position = position
        self._assurance = assurance
        self._label = label
        self._color = color
        self._image = image

    def make(self):
        """ This method create a box. """
        x = self._position[0]
        y = self._position[1]
        background = np.full(self._image.shape, (0, 0, 0), dtype=np.uint8)
        text = '{}: {:.4f}'.format(self._label, self._assurance)
        cv2.putText(background, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        fx, fy, fw, fh = cv2.boundingRect(background[:, :, 2])
        cv2.rectangle(self._image, self._position, self._size, self._color, 2)

        cv2.rectangle(self._image, (fx, fy), (fx + fw, fy + fh), self._color, -1)
        cv2.rectangle(self._image, (fx, fy), (fx + fw, fy + fh), self._color, 3)
        cv2.putText(self._image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        return self
