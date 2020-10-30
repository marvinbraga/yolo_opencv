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
from classes.computer_vision.computer_vision_clss import ImageObjectsDetect
from classes.config.yolo_data_clss import YoloConfig
from classes.config.yolo_hiper_params_clss import YoloHiperParams
from classes.image_managers.factories import FactoryImageManager

if __name__ == '__main__':
    weights = '../resources/data/yolov4.weights'
    labels = '../resources/data/coco.names'
    config = '../resources/data/yolov4.cfg'
    input_path = '../resources/fotos_teste'
    output_path = '../resources/results'
    ImageObjectsDetect(
        config=YoloConfig(labels, config, weights),
        hiper_params=YoloHiperParams(),
        file_manager=FactoryImageManager.PATH.new_instance([input_path])
    ).execute().save_to_file(path=output_path)
