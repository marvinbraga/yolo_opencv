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
from classes.core.validators import AbstractValidator, Validations, AbstractValidation


class BaseValidator(AbstractValidator):
    """ Class implements a base validator. """

    def __init__(self, validations: Validations):
        self._validations = validations
        self._is_ok = False

    def execute(self):
        """
        Execute validations.
        :return: self.
        """
        self._is_ok = True
        for validation in self._validations:
            if not validation.execute().is_ok:
                self._is_ok = False
                break
        return self

    def append(self, validation: AbstractValidation):
        """
        Associate a validation.
        :return: self.
        """
        self._validations.append(validation)
        return self

    @property
    def is_ok(self):
        """
        This method verify if rules is ok.
        :return: True/False.
        """
        return self.execute()._is_ok


class BaseValidation(AbstractValidation):
    """ Base class to validations. """
    def __init__(self):
        self._is_ok = False

    @property
    def is_ok(self):
        """
        This method verify if execution is ok.
        :return: True/False.
        """
        return self._is_ok

    def execute(self):
        """
        This method executes the validation.
        :return: self.
        """
        return self
