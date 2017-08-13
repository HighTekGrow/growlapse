import time
import imageio

class FileUtils:
    @staticmethod
    def getImageName():
        return "{0}{1}.png".format(FileUtils.getImagePath(), str(time.time()))

    @staticmethod
    def getImagePath():
        return "./images/"

    @staticmethod
    def getGifFilePath():
        return "./output/"

    @staticmethod
    def writeGif(time_lapse, preview):
        if preview is True:
            name = '{0}preview_{1}.gif'.format(FileUtils.getGifFilePath(), str(time.time()))
        else:
            name = '{0}{1}.gif'.format(FileUtils.getGifFilePath(), str(time.time()))

        with imageio.get_writer(name, mode='I') as writer:
            for filename in time_lapse.getImages():
                image = imageio.imread(filename)
                writer.append_data(image)
                
        return name
