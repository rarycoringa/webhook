from uuid import uuid4
from datetime import datetime
from urllib import parse

import peewee as pw

db = pw.SqliteDatabase('db.sqlite3')

class BaseModel(pw.Model):
    class Meta:
        database = db

class Webhook(BaseModel):
    id = pw.UUIDField(unique=True, default=uuid())
    url = pw.CharField()

class Task(BaseModel):
    id = pw.UUIDField(unique=True, default=uuid4())
    start_time = pw.DateTimeField(default=datetime.now)
    finish_time = pw.DateTimeField()
    finished = pw.BooleanField(default=False)
    webhook = ForeignKeyField(Webhook, backref='tasks')

    def send_webhook(self):
        return pw.model_to_dict(self)
