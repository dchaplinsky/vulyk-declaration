#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import codecs
import json
import sys
import re

sys.stdout = codecs.getwriter('utf8')(sys.stdout)


lists = {}
fields = []
current_answer = {}

REGIONS_MAP = {
    "ukraine": "Загальнодержавний регіон",
    "kiev": "м. Київ",
    "1": "Івано-Франківська область",
    "2": "Вінницька область",
    "3": "Волинська область",
    "4": "Дніпропетровська область",
    "5": "Донецька область",
    "6": "Житомирська область",
    "7": "Закарпатська область",
    "8": "Запорізька область",
    "9": "Кіровоградська область",
    "10": "Київська область",
    "11": "Кримська Автономна Республіка",
    "Sevostopol": "м. Севастополь",
    "Sevastopol": "м. Севастополь",
    "12": "Луганська область",
    "13": "Львівська область",
    "14": "Миколаївська область",
    "15": "Одеська область",
    "16": "Полтавська область",
    "17": "Рівненська область",
    "18": "Сумська область",
    "19": "Тернопільська область",
    "20": "Харківська область",
    "21": "Херсонська область",
    "22": "Хмельницька область",
    "23": "Черкаська область",
    "24": "Чернівецька область",
    "25": "Чернігівська область"
}


def cleanup(s):
    if isinstance(s, str):
        s = s.replace("—", " - ")
        s = re.sub("([^\s])\-\s+", r"\1-", s)
        s = re.sub("\s+\-([^\s])", r"-\1", s)
        s = re.sub("\.([^\s])", r". \1", s)
        s = re.sub("\s*\(\s*", " (", s)
        s = re.sub("\s*\)\s*", ") ", s)
        s = s.replace(" ,", ", ")
        s = s.replace(" .", ". ")
        s = re.sub("\s+", " ", s)
        return s.strip().rstrip(".")
    else:
        return s


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    all_tasks = []

    with open(in_file, "r") as fp:
        for r in fp:
            answers = json.loads(r)
            current_task = []

            for answer in answers:
                region = REGIONS_MAP.get(
                    answer["answer"]["general"]["post"].get("region"))

                data = map(cleanup, [
                    answer["answer"]["general"]["last_name"].capitalize(),
                    answer["answer"]["general"]["name"].capitalize(),
                    answer["answer"]["general"]["patronymic"].capitalize(),
                    region,
                    answer["answer"]["general"]["post"]["office"],
                    answer["answer"]["general"]["post"]["post"],
                    answer["answer"]["intro"]["declaration_year"]
                ])

                print("%s %s %s,%s,%s,%s,%s" % tuple(data))
