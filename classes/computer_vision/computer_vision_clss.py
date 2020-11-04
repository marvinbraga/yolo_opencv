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
from classes.computer_vision.abstract import AbstractComputerVision
from classes.computer_vision.yolo_clss import Yolo


class ImageObjectsDetect(AbstractComputerVision):
    """ Class to execute computer vision tasks with Yolo4 and OpenCV. """

    def __init__(self, config, hiper_params, file_manager, report=None):
        self._report = report
        self._file_manager = file_manager
        self._hiper_params = hiper_params
        self._config = config

    def execute(self, *args, **kwargs):
        """ This method execute the principal operation. """
        for data in self._file_manager.input:
            file_name = data.get('file_name')
            image = data.get('data')
            # Get prediction and classification.
            self._file_manager.output.append({'file_name': file_name, 'data': Yolo(
                file_name, image, self._config, self._hiper_params, self._report
            ).execute().get_output().output})
        return self

    def get_output(self):
        """ This method create the output dict.  """
        return self._file_manager.output

    def get_output_as_base64(self):
        """ This method create the output dict.  """
        return self._file_manager.output_in_base64

    def save_to_file(self, path):
        """ This method saves the predicted result in a file. """
        self._file_manager.save_in_files(path)
        return self

    def get_report(self):
        """ This method returns the report of execution. """
        return None if self._report is None else self._report.output


class VideoObjectsDetect(AbstractComputerVision):
    """ Class to execute video computer vision tasks with Yolo4 and OpenCV. """

    def __init__(self, config, hiper_params, file_manager, report=None):
        self._report = report
        self._file_manager = file_manager
        self._hiper_params = hiper_params
        self._config = config

    def execute(self, *args, **kwargs):
        """ This method execute the principal operation. """
        for data in self._file_manager.input:
            file_name = data.get('file_name')
            image = data.get('data')
            # Get prediction and classification.
            self._file_manager.output.append({'file_name': file_name, 'data': Yolo(
                file_name, image, self._config, self._hiper_params, self._report
            ).execute().get_output().output})
        return self

    def get_output(self):
        """ This method create the output dict.  """
        return self._file_manager.output

    def get_output_as_base64(self):
        """ This method create the output dict.  """
        return self._file_manager.output_in_base64

    def save_to_file(self, path):
        """ This method saves the predicted result in a file. """
        self._file_manager.save_in_files(path)
        return self

    def get_report(self):
        """ This method returns the report of execution. """
        return None if self._report is None else self._report.output
