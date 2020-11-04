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
import numpy as np


class BoxDetect:
    """ Class to detect image. """
    def __init__(self, threshold, image, scores, position, classe_id, confidence, boxes, assurances, id_classes):
        self._id_classes = id_classes
        self._assurances = assurances
        self._boxes = boxes
        self._confidence = confidence
        self._classe_id = classe_id
        self._position = position
        self._scores = scores
        self._image = image
        self._threshold = threshold

    def _check(self):
        """
        This method checks whether a class has been found.
        :return: True/False.
        """
        return self._confidence > self._threshold

    def execute(self):
        """
        This method the rules of verification and association.
        :return: Self.
        """
        if self._check():
            (h, w) = self._image.shape[:2]
            # Creating the detection box.
            box = self._position * np.array([w, h, w, h])
            (centerX, centerY, width, height) = box.astype('int')
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            # Saving the detection values.
            self._boxes.append([x, y, int(width), int(height)])
            self._assurances.append(float(self._confidence))
            self._id_classes.append(self._classe_id)
        return self