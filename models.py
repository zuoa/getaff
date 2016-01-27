# -*- coding: utf-8 -*-  
# create: 2016/1/21
# author: Yu
from peewee import *
from flask.ext.login import UserMixin

db = SqliteDatabase('_getaff.db')

class User(UserMixin):
    id = PrimaryKeyField()
    name = CharField(unique=True)

    class Meta:
        database = db


