import time
from flask_cors import CORS, cross_origin
from flask import Flask, request, send_file
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from utils.CameraUtils import CameraUtils
from utils.ImageUtils import ImageUtils
from utils.TimeLapseUtils import TimeLapseUtils
from utils.WorkerUtils import WorkerUtils
from utils.FileUtils import FileUtils

db_connect = create_engine('sqlite:///timelapse.db')
app = Flask(__name__)
CORS(app)
api = Api(app)

class Preview(Resource):
    def get(self, time_lapse_id):
        try:
            tl = TimeLapseUtils.getTimeLapse(db_connect, time_lapse_id)
            filename = FileUtils.writeGif(tl, True)
            return send_file(filename, mimetype='image/gif')
        except:
            return {}

class TimeLapse(Resource):
    def get(self, id):
        try:
            return TimeLapseUtils.getTimeLapse(db_connect, id).toDict()
        except:
            return {}

    def delete(self, id):
        try:
            return TimeLapseUtils.removeTimeLapse(db_connect, id)
        except:
            return {}        


class TimeLapses(Resource):
    def get(self):
        try:
            return TimeLapseUtils.getAllTimeLapses(db_connect)
        except:
            return {}

    def post(self):
        tl = TimeLapseUtils.createTimeLapse(db_connect, request.form['name'], request.form['interval'], request.form['length'])
        WorkerUtils.startWorker(tl, worker)
        return tl.toDict()

class Images(Resource):
    def get(self):
        try:
            return ImageUtils.getAllImages(db_connect)
        except:
            return {}

class Image(Resource):
    def get(self, id):
        try:
            return ImageUtils.getImage(db_connect, id)
        except:
            return {}

api.add_resource(Images, '/images')
api.add_resource(Image, '/images/<id>')
api.add_resource(TimeLapses, '/timelapse')
api.add_resource(TimeLapse, '/timelapse/<id>')
api.add_resource(Preview, '/preview/<time_lapse_id>')

def get_image(camera):
    retval, im = camera.read()
    return im

def worker(time_lapse):
    j = 0
    TimeLapseUtils.updateTimeLapseRunning(db_connect, time_lapse.getId(), 1)
    while j < (time_lapse.getLength() / time_lapse.getInterval()):
        print "Taking image"
        time_lapse.addImage(CameraUtils.takeStillPicture(db_connect, time_lapse))
        j += 1
        time.sleep(time_lapse.getInterval())
    TimeLapseUtils.updateTimeLapseRunning(db_connect, time_lapse.getId(), 0)
    print 'Writing GIF'
    FileUtils.writeGif(time_lapse, False)
    print "Time Lapse Complete!"

if __name__ == '__main__':
    try:
        print "Starting server on port 5002"
        app.run(host='0.0.0.0', port='5002')
    except KeyboardInterrupt:
        print 'Killing app due to user interuption'
