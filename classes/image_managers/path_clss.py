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
import os
from typing import final
import cv2
import matplotlib.pyplot as plt
from classes.image_managers.base_opencv_saver_clss import BaseImageSaver
from classes.image_managers.validators_clss import PathValidations, FileExistsValidation


@final
class PathImageManager(BaseImageSaver):
    """ This class implements the loading of image files through directory paths. """
    def __init__(self, path_list):
        super().__init__()
        self._path_list = path_list
        self._file_names_list = []
        self._load_names()._loads()

    def _load_names(self):
        """ Load file names from path list. """
        for path in self._path_list:
            self._file_names_list += self.load_images_from_dir(path)
        return self

    def _loads(self):
        """
        This method load image files.
        :return: self.
        """
        self._input = [self._check(file_name) for file_name in self._file_names_list]
        return self

    @staticmethod
    def _check(file_name):
        """
        This method verifies file.
        :return: Dict item.
        """
        result = {'file_name': file_name, 'data': None}
        if PathValidations(validations=[FileExistsValidation(file_name)]).is_ok:
            result = {'file_name': file_name, 'data': cv2.imread(file_name)}
        return result

    def search_image(self, file_name):
        """ This methods gets the image for file_name. """
        result = None
        for data in self._input:
            if data.get('file_name') == file_name:
                result = data.get('data')
                break
        return result

    def show_image(self, file_name):
        """ This method shows the image object. """
        image = self.search_image(file_name)
        if image:
            img = plt.gcf()
            img.set_size_inches(16, 10)
            plt.axis('off')
            plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            plt.show()
        return self

    @staticmethod
    def load_images_from_dir(path):
        """ This method loads all images in a directory. """
        return [os.path.join(path, f) for f in os.listdir(path)]
