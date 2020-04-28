from db.db import db


class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(400))

    def serialize(self):
        return {"id": self.id,
                "message": self.message}
