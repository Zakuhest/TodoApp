from app.db import db

class Task(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    createdAt = db.Column(db.DateTime(timezone=False))
    doneAt = db.Column(db.DateTime(timezone=False))
    deletedAt = db.Column(db.DateTime(timezone=False))

""" task_list = [
    {'id': 1, 'text':'Despertar', 'createdAt': datetime.now(), 'doneAt': None},
    {'id': 2, 'text':'Desayunar', 'createdAt': datetime.now(), 'doneAt': None},
    {'id': 3, 'text':'Bañar', 'createdAt': datetime.now(), 'doneAt': None},
    {'id': 4, 'text':'Salir', 'createdAt': datetime.now(), 'doneAt': None}
] """