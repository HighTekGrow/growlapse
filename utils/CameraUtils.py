from __future__ import division
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


        image = CameraUtils.get_image(camera)
        total_count = 0
        black_count = 0
        for x in image:
            for j in x:
                for k in j:
                    total_count += 1
                    if k == 0:
                        black_count += 1
                    if total_count > 100:
                        break

        image = None
        percent_black_pixels = int(round((black_count / total_count) * 100))
        if (percent_black_pixels < 50):
            print "Writing Image"
            cv2.imwrite(file_name, CameraUtils.get_image(camera))
            image = ImageUtils.addImageToDB(db, time_lapse, file_name)
        del (camera)
        return image



    @staticmethod
    def get_image(camera):
        retval, im = camera.read()
        return im

