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


class AbstractImageManager(metaclass=ABCMeta):
    """
    Interface for image managers that aims to recover images in a certain
    format, prepare them for use by YOLO4 with OpenCV and provide the
    result of its processing.
    """
    @property
    @abstractmethod
    def input(self):
        """
        This property returns the value of input info.
        :return: [{'file_name': Image name, 'data': OpenCV data}]
        """
        pass

    @abstractmethod
    def set_output(self, value):
        """
        This methods sets the value of output property.
        :param value: [{'file_name': Image name, 'data': OpenCV data}]
        :return: self.
        """
        pass

    @property
    @abstractmethod
    def output(self):
        """
        This property returns a list containing dictionary items formed
        by the name of the image file and the image itself as an OpenCV
        data.
        :return: [{'file_name': Image name, 'data': OpenCV data}]
        """
        pass


class AbstractImageSaver(metaclass=ABCMeta):
    """
    Interface for image saver (YOLO4 with OpenCV).
    """
    @property
    @abstractmethod
    def output_in_base64(self):
        """
        This property returns a list containing dictionary items formed
        by the filename of image and the image itself already in the
        string base64 format.
        :return: [{'file_name': Image name, 'data': Image in base64 string}]
        """
        pass

    @property
    @abstractmethod
    def output_in_bytes(self):
        """
        This property returns a list containing dictionary items formed
        by the name of the image file and the image itself already in
        byte format.
        :return: [{'file_name': Image name, 'data': Image in bytes}]
        """
        pass

    @abstractmethod
    def save_in_files(self, path):
        """
        This method saves the images contained in the output property to a file.
        :param path: Path to save files.
        :return: self.
        """
        pass
