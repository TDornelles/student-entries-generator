import csv
import json
import pandas as pd
from numpy.random import randint
from pymongo import MongoClient


def generate_cpf():
    cpf = ""

    for i in range(9):
        cpf += str(randint(0, 9))

    cpf = generate_first_digit(cpf)
    cpf = generate_second_digit(cpf)
    print(cpf)


def generate_first_digit(cpf):
    pos = 10
    result = 0
    while pos >= 2:
        mult = int(cpf[10 - pos]) * pos
        result += mult
        pos -= 1

    result = result % 11
    if result < 2:
        return cpf + "0"
    else:
        result = 11 - result
        return cpf + str(result)


def generate_second_digit(cpf):
    pos = 11
    result = 0
    while pos >= 2:
        mult = int(cpf[11 - pos]) * pos
        result += mult
        pos -= 1

    result = result % 11

    if result < 2:
        return cpf + "0"
    else:
        result = 11 - result
        return cpf + str(result)


def make_students_json():

    name_data = pd.read_csv('resources/nomes.csv')


def __main__():
    client = MongoClient("mongodb+srv://tobiastd:qwerty123456@cluster0."
                         "auyaiih.mongodb.net/?retryWrites=true&w=majority")

    db = client.redis_test
    collection = db.students

    posts = db.posts

    # posts.insert_one(student).inserted_id


generate_cpf()