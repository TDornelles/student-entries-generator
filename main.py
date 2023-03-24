import random

import names_dataset
import pandas as pd
from numpy.random import randint
from pymongo import MongoClient
from names_dataset import NameDataset, NameWrapper

import resources.mongo_strings


def get_curso():
    cursos = pd.read_csv('resources/cursos.csv')['CURSONOME'].values.tolist()
    curso = random.choice(cursos)

    return curso

def get_name():
    first_names = pd.read_csv('resources/nomes.csv')['first_name'].values.tolist()
    first_name = random.choice(first_names)

    return first_name


def generate_year():
    year_end = str(randint(0, 23))
    if int(year_end) < 10:
        year = "200" + year_end
    else:
        year = "20" + year_end

    return year


def generate_cpf():
    cpf = ""

    for i in range(9):
        cpf += str(randint(0, 9))

    cpf = generate_first_digit(cpf)
    cpf = generate_second_digit(cpf)
    return cpf


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


class Student:
    first_names = pd.read_csv('resources/nomes.csv')
    first_names.columns

    cpf = generate_cpf()


def make_students_json():

    nd = names_dataset
    name_data = pd.read_csv('resources/nomes.csv')
    curso = get_curso()


def __main__():
    client = \
        MongoClient(resources.mongo_strings.connection_string)

    db = client.redis_test
    collection = db.students

    posts = db.posts

    # posts.insert_one(student).inserted_id



get_name()


