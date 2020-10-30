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
from classes.image_managers.abstracts import AbstractImageManager


class BaseImageManager(AbstractImageManager):
    """ This class implements the base image manager. """

    def __init__(self):
        self._path_list = []
        self._input = []
        self._output = []

    def set_output(self, value):
        """
        This methods sets the value of output property.
        :param value: [{'file_name': Image name, 'data': OpenCV data}]
        :return: self.
        """
        self._output = value
        return self

    @property
    def input(self):
        """
        This property returns the value of input info.
        :return: [{'file_name': Image name, 'data': OpenCV data}].
        """
        return self._input

    @property
    def output(self):
        """
        This property returns a list containing dictionary items formed
        by the name of the image file and the image itself as an OpenCV
        data.
        :return: [{'file_name': Image name, 'data': OpenCV data}]
        """
        return self._output
