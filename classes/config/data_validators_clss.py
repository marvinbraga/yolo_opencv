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
from typing import final
from pathlib import Path

from classes.config.data_exceptions import ConfigDataFileNotFound
from classes.core.validators_clss import BaseValidator, BaseValidation


@final
class DataValidations(BaseValidator):
    """ Validations to path rules. """
    pass


@final
class DataFileExistsValidation(BaseValidation):
    """ Validation to file exists. """
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def execute(self):
        """
        This method executes the validation.
        :return: self.
        """
        self._is_ok = Path(self._file_name).is_file()
        if not self._is_ok:
            raise ConfigDataFileNotFound(file_name=self._file_name)
        return self
