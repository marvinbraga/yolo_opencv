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


class VideoCodec(Enum):
    """ Classification of video codecs. """
    AVI = 0, *'xvid'
    MP4 = 1, *'mp4v'
    MJPG = 2, *'mjpg'
    DIVX = 3, *'divx'
    X264 = 4, *'x264'

    def codec(self) -> tuple:
        """
        Returns codec tuple.
        :return: Tuple.
        """
        return self.value[1:]
