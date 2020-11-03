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

from classes.report.labels_to_count_clss import LabelsToCount


class FactoryReport(Enum):
    """ Class factory to reports. """
    LABELS_TO_COUNT = 0, 'Contador de Labels'

    def new_instance(self, *args, **kwargs):
        """ Get object. """
        cls = {
            FactoryReport.LABELS_TO_COUNT: LabelsToCount,
        }[self]
        return cls(*args, **kwargs)
