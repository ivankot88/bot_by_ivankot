import peewee
import datetime
from telebot import TeleBot
from pyowm import OWM
import datetime
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

database = peewee.SqliteDatabase("database.db")

class Users(peewee.Model):
    id = peewee.IntegerField()
    telephone = peewee.CharField()
    hobbies = peewee.CharField()
    country = peewee.CharField()
    first_name = peewee.CharField()
    second_name = peewee.CharField()
    reputation = peewee.IntegerField()
    latitude = peewee.FloatField()
    longitude = peewee.FloatField()
    weather = peewee.IntegerField()
    weather_time = peewee.TimeField()
    fun = peewee.CharField()

    class Meta:
        database = database


class Reminder(peewee.Model):
    id = peewee.IntegerField()
    time = peewee.TimeField()
    text = peewee.CharField()
    date = peewee.DateTimeField()

    class Meta:
        database = database


class Events(peewee.Model):
    id = peewee.IntegerField()
    date = peewee.DateField()
    time = peewee.TimeField()
    text = peewee.CharField()
    count = peewee.IntegerField()
    fun = peewee.CharField()
    creator = peewee.IntegerField()
    members = peewee.CharField()
    status = peewee.IntegerField()
    address = peewee.CharField()
    class Meta:
        database = database


class Emoji:
    def __init__(self):
        self.pictures = {
            'смех':'😂',
            'палец':'👍' ,
            'солнце':'☀',
            'подмигивание':'😉',
            'туча1':'🌤',
            'туча2':'⛅',
            'туча3':'🌥',
            'дождь1':'🌦',
            'туча5':'☁',
            'дождь2':'🌧',
            'гроза1':'⛈',
            'гроза2':'🌩',
            'снег':'🌨',
            'грусть':'😞',
            'улыбка':'😀',
            'улыбка1':'😊',
            'пальто':'🧥',
            'перчатки':'🧤',
            'зонт':'☂'
        }

    def weather1(text,self):
        if text == 'Clouds':
            return '☁'
        elif text == 'Clear':
            return '☀'
        elif text == 'Snow':
            return '🌨'
        elif text == 'Thunderstorm':
            return '⛈'
        elif text == 'Drizzle':
            return '🌨'
        elif text == 'Rain':
            return '🌧'
        else:
            return ''


class Words:
    def __init__(self):
        file = open('welcome_words.txt')
        file1 = open('farewell_words.txt')
        self.welcome = file.readlines()
        self.leave = file1.readlines()