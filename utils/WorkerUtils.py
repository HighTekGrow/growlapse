
import threading

class WorkerUtils:
    @staticmethod
    def startWorker(time_lapse, worker):
        t = threading.Thread(target=worker, args=(time_lapse,))
        t.daemon = True
        t.start()
        return t

