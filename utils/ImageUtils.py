from models.Image import Image

class ImageUtils:
    @staticmethod
    def addTimeLapseImages(db, time_lapse):
        conn = db.connect()
        images = conn.execute("SELECT id, timelapse_id, path, created, deleted FROM images WHERE timelapse_id = ? AND deleted = 0", [time_lapse.getId()])
        image_list = [{key: value for (key, value) in row.items()} for row in images]
        for image_dict in image_list:
            image = Image(image_dict)
            time_lapse.addImage(image)

    @staticmethod
    def getAllImages(db):
        conn = db.connect()
        result = conn.execute("SELECT id, timelapse_id, path, created, deleted FROM images WHERE deleted = 0")
        image_list = [{key: value for (key, value) in row.items()} for row in result]
        all_images = []
        for i in image_list:
            all_images.append(Image(i).getDict())
        return all_images
    @staticmethod
    def getImage(db, id):
        conn = db.connect()
        result = conn.execute("SELECT id, timelapse_id, path, created, deleted FROM images WHERE id = ? AND deleted = 0 LIMIT 1", [ id ])
        image_list = [{key: value for (key, value) in row.items()} for row in result]
        return Image(image_list[0])

    @staticmethod
    def addImageToDB(db, time_lapse, file):
        conn = db.connect()
        result = conn.execute("INSERT INTO images (timelapse_id, path) VALUES (?, ?)", [time_lapse.getId(), file])
        return ImageUtils.getImage(db, result.lastrowid)
        
