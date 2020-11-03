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
from classes.report.abstract import AbstractReport


class LabelsToCount(AbstractReport):
    """ Class to get info to selected labels. """
    def __init__(self, labels_to_count):
        self._get_labels_to_count(labels_to_count)
        self._label = None
        self._found_label = None
        self._labels_found_in_image = None

    def _get_labels_to_count(self, labels_to_count):
        self._labels_to_count = {}
        if labels_to_count:
            for label in labels_to_count:
                self._labels_to_count[label] = 0
        return self

    @property
    def output(self):
        """
        Returns the report.
        :return: Report dict.
        """
        return self._labels_to_count

    def was_label_found(self):
        """
        This method checks whether a class has been found.
        :return: True/False.
        """
        return True if len(self._labels_to_count) == 0 else self._found_label is not None

    def generate_report(self, label):
        """
        This method generate a report.
        :param label: Class label.
        :return: Self.
        """
        self._found_label = self._labels_to_count.get(label)
        if self._found_label is not None:
            # Found in image
            if self._labels_found_in_image is None:
                self._labels_found_in_image = {label: 0}
            if self._labels_found_in_image.get(label) is None:
                self._labels_found_in_image[label] = 0
            self._labels_found_in_image[label] += 1
            # Found in images
            self._labels_to_count[label] += 1
        return self

    def append_label(self, label):
        """
        This method add a label to report.
        :return:
        """
        self._labels_to_count[label] = 0
        return self
