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
from typing import final
from classes.config.config_validators_clss import ConfigValidations, InvalidValueValidation
from classes.config.yolo_hiper_params import AbstractYoloHiperParams


@final
class YoloHiperParams(AbstractYoloHiperParams):
    """ Class to config hiper params. """

    def __init__(self, threshold=0.5, threshold_nns=0.3):
        # Removing shared boxes with low probability (NO-MAX-SUPPRESSION).
        self._threshold_nns = threshold_nns
        # Defining the level of certainty for the placement of boxes.
        self._threshold = threshold
        self._check()

    def _check(self):
        """ Execute validations. """
        ConfigValidations(
            validations=[InvalidValueValidation(value=v) for v in (self._threshold_nns, self._threshold)]
        ).execute()
        return self

    @property
    def threshold_nns(self):
        """
        This property returns the value of _threshold_nns.
        :return: _threshold_nns
        """
        return self._threshold_nns

    @property
    def threshold(self):
        """
        This property returns the value of _threshold.
        :return: _threshold
        """
        return self._threshold
