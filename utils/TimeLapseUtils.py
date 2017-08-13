from models.TimeLapse import TimeLapse
from utils.ImageUtils import ImageUtils


class TimeLapseUtils:
    @staticmethod
    def getAllTimeLapses(db):
        time_lapses = []
        conn = db.connect()
        query = conn.execute("SELECT id, name, intervalinseconds, lengthinseconds, started, running FROM timelapses WHERE deleted = 0")
        for i in query.cursor.fetchall():
            tl = TimeLapse(i)
            ImageUtils.addTimeLapseImages(db, tl)
            time_lapses.append(tl.toDict())
        return time_lapses

    @staticmethod
    def createTimeLapse(db, name, interval, length):
        conn = db.connect()
        result = conn.execute("INSERT INTO timelapses (name, intervalinseconds, lengthinseconds, running) VALUES (?, ?, ?, 0)", [ name, interval, length ])

        return TimeLapseUtils.getTimeLapse(db, result.lastrowid)

    @staticmethod
    def updateTimeLapseRunning(db, id, running):
        conn = db.connect()
        result = conn.execute("UPDATE timelapses SET running = ? WHERE id = ?", [ running, id ])
        return TimeLapseUtils.getTimeLapse(db, id)

    @staticmethod
    def getTimeLapse(db, id):
        conn = db.connect()
        query = conn.execute("SELECT id, name, intervalinseconds, lengthinseconds, started, running FROM timelapses WHERE id = ? LIMIT 1", [ id ])
        time_lapse = TimeLapse(query.cursor.fetchall()[0])
        ImageUtils.addTimeLapseImages(db, time_lapse)
        return time_lapse

    @staticmethod
    def removeTimeLapse(db, id):
        conn = db.connect()
        query = conn.execute("UPDATE timelapses SET deleted = 1 WHERE id = ?", [ id ])
        return TimeLapseUtils.getAllTimeLapses(db)
