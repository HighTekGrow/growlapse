class TimeLapse:
    id = None
    running = False
    name = None
    speed = None
    started = None
    lastImageTaken = None
    images = []

    def __init__(self, data):
        self.id = data[0]
        self.name = data[1]
        self.interval = data[2]
        self.length = data[3]
        self.started = data[4]
        self.running = data[5]
        self.images = []

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getInterval(self):
        return self.interval

    def setInterval(self, interval):
        self.interval = interval

    def getLength(self):
        return self.length

    def setLength(self, length):
        self.length = length

    def getStarted(self):
        return self.started

    def setStared(self, started):
        self.started = started

    def getImages(self):
        return self.images

    def setImages(self, images):
        self.images = images

    def getLastImageTaken(self):
        return self.lastImageTaken

    def setLastImageTaken(self, imageTaken):
        self.lastImageTaken = imageTaken

    def addImage(self, image):
        self.images.append(image.getPath())

    def setRunning(self, running):
        self.running = running

    def toDict(self):
        return {
            'id': self.id,
            'name': self.name,
            'interval': self.interval,
            'length': self.length,
            'time_started': self.started,
            'running': self.running
        }