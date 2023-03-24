import random
from uuid import UUID

import pandas as pd
from numpy.random import randint
from pymongo import MongoClient

import resources.mongo_strings
import redis

r = redis.Redis(host='localhost', port=6379, db=0)

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
    def __init__(self):
        self.nome: str = get_name()
        self.cpf: str = generate_cpf()
        self.curso: str = get_curso()
        self.ano: str = generate_year()

    def to_string(self):
        print(self.nome + self.cpf + self.curso + self.ano)


def make_student_json(student: Student):
    student_json = {
        "nome": student.nome,
        "cpf": student.cpf,
        "curso": student.curso,
        "ano": student.ano
    }

    return student_json


def __main__():
    client = MongoClient(resources.mongo_strings.connection_string)

    db = client.redis_test
    collection = db.students
    doc_count = int(input("insert how many documents?"))
    for i in range(doc_count):
        student = Student()
        student_json = make_student_json(student)
        collection.insert_one(student_json)

    r.flushall()
    cursor = collection.find({})
    for document in cursor:
        r.set(str(generate_cpf()), str(document))


__main__()
