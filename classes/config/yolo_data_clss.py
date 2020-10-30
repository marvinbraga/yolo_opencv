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
from typing import final

from classes.config.data_validators_clss import DataValidations, DataFileExistsValidation
from classes.config.yolo_data import AbstractYoloConfig


@final
class YoloConfig(AbstractYoloConfig):
    """ This class implements yolo config data. """

    def __init__(self, labels_file, config_file, weights_file):
        self._weights_file = weights_file
        self._config_file = config_file
        self._labels_file = labels_file
        self._labels = None
        self._colors = None
        self._check()._get_labels()

    def _check(self):
        """ Execute validations. """
        DataValidations(
            validations=[DataFileExistsValidation(file_name=f) for f in [
                self._weights_file, self._labels_file, self._config_file]]
        ).execute()
        return self

    def _get_labels(self):
        """ This method get the labels from file. """
        self._labels = open(self._labels_file).read().strip().split('\n')
        # Define boxes colors.
        np.random.seed(77)
        self._colors = np.random.randint(0, 255, size=(len(self._labels), 3), dtype='uint8')
        return self

    @property
    def labels(self):
        """
        This property returns _labels value.
        :return:
        """
        return self._labels

    @property
    def colors(self):
        """
        This property returns _colors value.
        :return:
        """
        return self._colors

    @property
    def config_file(self):
        """
        This property returns _config_file value.
        :return:
        """
        return self._config_file

    @property
    def weights_file(self):
        """
        This property returns _weights_file value.
        :return:
        """
        return self._weights_file
