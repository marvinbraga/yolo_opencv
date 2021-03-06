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


class AbstractYoloHiperParams(metaclass=ABCMeta):
    """ Interface to config hiper params. """

    @property
    @abstractmethod
    def threshold_nms(self):
        """
        This property returns the value of _threshold_nms.
        :return: _threshold_nms
        """
        pass

    @property
    @abstractmethod
    def threshold(self):
        """
        This property returns the value of _threshold.
        :return: _threshold
        """
        pass
