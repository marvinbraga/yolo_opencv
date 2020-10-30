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


class AbstractYoloConfig(metaclass=ABCMeta):
    """ Abstract class to yolo config data. """

    @property
    @abstractmethod
    def labels(self):
        """
        This property returns _labels value.
        :return:
        """
        pass

    @property
    @abstractmethod
    def colors(self):
        """
        This property returns _colors value.
        :return:
        """
        pass

    @property
    @abstractmethod
    def config_file(self):
        """
        This property returns _config_file value.
        :return:
        """
        pass

    @property
    @abstractmethod
    def weights_file(self):
        """
        This property returns _weights_file value.
        :return:
        """
        pass
