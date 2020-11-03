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


class AbstractReport(metaclass=ABCMeta):
    """ Interface to report classes. """
    @abstractmethod
    def was_label_found(self):
        """
        This method checks whether a class has been found.
        :return: True/False.
        """
        pass

    @abstractmethod
    def generate_report(self, label):
        """
        This method generate a report.
        :param label: Class label.
        :return: Self.
        """
        pass

    @abstractmethod
    def append_label(self, label):
        """
        This method add a label to report.
        :param label: Class label.
        :return:
        """
        pass

    @property
    @abstractmethod
    def output(self):
        """
        Returns the report.
        :return: Report dict.
        """
        pass
