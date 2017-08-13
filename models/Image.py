class Image:
    id = None
    timelapse_id = None
    path = None
    timeTaken = None

    def __init__(self, data):
        self.id = data['id']
        self.path = data['path']
        self.timelapse_id = data['timelapse_id']
        self.timeTaken = data['created']

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getTimelapseId(self):
        return self.timelapse_id

    def setTimelapseId(self, id):
        self.timelapse_id = id

    def getPath(self):
        return self.path

    def setPath(self, path):
        self.path = path

    def getTimeTaken(self):
        return self.timeTaken

    def setTimeTaken(self, time):
        self.timeTaken = time

    def getDict(self):
        return {
            'id': self.id,
            'path': self.path,
            'timetaken': self.timeTaken,
            'time_lapse_id': self.timelapse_id
        }