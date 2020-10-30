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


class AbstractComputerVision(metaclass=ABCMeta):
    """ Abstract class to Computer Vision operations. """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """ This method execute the principal operation. """
        pass

    @abstractmethod
    def get_output(self):
        """ This method create the output dict.  """
        pass

    @abstractmethod
    def get_output_as_base64(self):
        """ This method create the output dict.  """
        pass

    @abstractmethod
    def save_to_file(self, path):
        """ This method saves the predicted result in a file. """
        pass

    @abstractmethod
    def get_report(self):
        """ This method returns the report of execution. """
        pass
