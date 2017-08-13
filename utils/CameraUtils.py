import cv2
from utils.FileUtils import FileUtils
from utils.ImageUtils import ImageUtils


class CameraUtils:
    camera_port = 0
    ramp_frames = 30

    @staticmethod
    def takeStillPicture(db, time_lapse):
        camera = cv2.VideoCapture(CameraUtils.camera_port)
        for i in xrange(CameraUtils.ramp_frames):
            temp = CameraUtils.get_image(camera)
        file_name = FileUtils.getImageName()
        cv2.imwrite(file_name, CameraUtils.get_image(camera))
        del (camera)
        return ImageUtils.addImageToDB(db, time_lapse, file_name)


    @staticmethod
    def get_image(camera):
        retval, im = camera.read()
        return im

