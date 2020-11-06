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
from classes.computer_vision.computer_vision_clss import ImageObjectsDetect, VideoObjectsDetect
from classes.config.video_codec_clss import VideoCodec
from classes.config.yolo_data_clss import YoloConfig
from classes.config.yolo_hiper_params_clss import YoloHiperParams
from classes.config.yolo_video_params_clss import YoloVideoParams
from classes.image_managers.factories import FactoryImageManager
from classes.report.factory import FactoryReport

if __name__ == '__main__':
    weights = '../resources/data/yolov4.weights'
    labels = '../resources/data/coco.names'
    config = '../resources/data/yolov4.cfg'
    output_path = '../resources/results'
    test_image = False
    if test_image:
        input_path = '../resources/fotos_teste'
        # Image detect.
        print(ImageObjectsDetect(
            config=YoloConfig(labels, config, weights),
            hiper_params=YoloHiperParams(),
            file_manager=FactoryImageManager.PATH.new_instance([input_path]),
            report=FactoryReport.LABELS_TO_COUNT.new_instance(['dog', 'cat'])
        ).execute().save_to_file(path=output_path).get_report())
    else:
        # Video detect.
        file_name = '../resources/videos/video_rua01.mp4'
        print(VideoObjectsDetect(
            file_name=file_name, output_path=output_path, config=YoloConfig(labels, config, weights),
            hiper_params=YoloHiperParams(), video_params=YoloVideoParams(codec=VideoCodec.MP4, fps=60),
            report=FactoryReport.LABELS_TO_COUNT.new_instance([])
        ).execute().get_report())
