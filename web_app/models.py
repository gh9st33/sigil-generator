from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sigil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sigilCode = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(200), nullable=False)
    sigilImage = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, sigilCode, message, sigilImage):
        self.sigilCode = sigilCode
        self.message = message
        self.sigilImage = sigilImage