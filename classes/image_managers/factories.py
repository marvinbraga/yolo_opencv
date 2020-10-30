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
from enum import Enum
from classes.image_managers.path_clss import PathImageManager


class FactoryImageManager(Enum):
    """ This factory create an object from Image Managers Classes. """
    PATH = 0
    BYTES = 1
    BASE64 = 2

    def new_instance(self, *args, **kwargs):
        """ This method create a respective object. """
        cls = {
            FactoryImageManager.PATH: PathImageManager,
            FactoryImageManager.BYTES: None,
            FactoryImageManager.BASE64: None,
        }[self]
        return cls(*args, **kwargs)
