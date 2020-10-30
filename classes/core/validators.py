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

from typing import List


class AbstractValidator(metaclass=ABCMeta):
    """ Interface to Validators """

    @abstractmethod
    def execute(self):
        """
        Execute validations
        :return: self.
        """
        pass

    @abstractmethod
    def append(self, validation):
        """
        Associate a validation
        :return: self.
        """
        pass

    @property
    @abstractmethod
    def is_ok(self):
        """
        This method verify if rules is ok.
        :return: True/False.
        """
        pass


class AbstractValidation(metaclass=ABCMeta):
    """ Interface to validations classes. """

    @property
    @abstractmethod
    def is_ok(self):
        """
        This method verify if execution is ok.
        :return: True/False.
        """
        pass

    @abstractmethod
    def execute(self):
        """
        This method executes the validation.
        :return: self.
        """
        pass


# List of validations.
Validations = List[AbstractValidation]
