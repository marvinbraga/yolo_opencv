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
import base64
import os
from abc import abstractmethod
import cv2
from classes.image_managers.abstracts import AbstractImageSaver
from classes.image_managers.base_clss import BaseImageManager


class BaseImageSaver(BaseImageManager, AbstractImageSaver):
    """ This class implements the base image saver. """

    @property
    def output_in_base64(self):
        """
        This property returns a list containing dictionary items formed
        by the filename of image and the image itself already in the
        string base64 format.
        :return: [{'file_name': Image name, 'data': Image in base64 string}]
        """
        return [{
            'file_name': item.get('file_name'),
            'data': base64.b64encode(cv2.imencode('.jpg', item.get('data')))
        } for item in self._output]

    @property
    def output_in_bytes(self):
        """
        This property returns a list containing dictionary items formed
        by the name of the image file and the image itself already in
        byte format.
        :return: [{'file_name': Image name, 'data': Image in bytes}]
        """
        result = []
        return result

    def save_in_files(self, path):
        """
        This method saves the images contained in the output property to a file.
        :return: self.
        """
        for item in self._output:
            data = item.get('data')
            if data is not None:
                file_name = os.path.join(path, os.path.split(item.get('file_name'))[-1])
                cv2.imwrite(os.path.normpath(file_name), data)
        return self
