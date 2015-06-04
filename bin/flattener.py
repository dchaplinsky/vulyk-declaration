#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from string import capwords
from collections import defaultdict
from openrefine import OpenRefine
from glob2 import glob

from natsort import natsorted


lists = {}
to_str = lambda x: "%02d" % (x + 1) if isinstance(x, int) else x
OPREF = OpenRefine(glob("edits/*.json"))


def title(s):
    chunks = s.split()
    chunks = map(lambda x: capwords(x, u"-"), chunks)
    return u" ".join(chunks)


def unify_path(path):
    return ".".join(
        map(lambda x: "xxx" if isinstance(x, int) else x, path))


FIELDS_TO_IGNORE = ['task.data.link', 'user.email', 'user.username']
FIELDS_TO_TITLIZE = [
    "answer.general.addresses.xxx.place_city",
    "answer.general.addresses.xxx.place_district",
    "answer.general.last_name",
    "answer.general.name",
    "answer.general.patronymic"
]

FIELDS_TO_CAPITALIZE = ["answer.general.family.xxx.name"]
FIELDS_TO_LOWERCASIZE = []
FIELDS_TO_PROOFREAD = ["answer.general.post.post"]

FIELDS_TO_NUM_NORMALIZE = [
    "answer.banks.45.xxx.sum",
    "answer.banks.45.xxx.sum_foreign",
    "answer.banks.46.xxx.sum",
    "answer.banks.46.xxx.sum_foreign",
    "answer.banks.47.xxx.sum",
    "answer.banks.47.xxx.sum_foreign",
    "answer.banks.48.xxx.sum",
    "answer.banks.48.xxx.sum_foreign",
    "answer.banks.49.xxx.sum",
    "answer.banks.49.xxx.sum_foreign",
    "answer.banks.50.xxx.sum",
    "answer.banks.50.xxx.sum_foreign",
    "answer.banks.51.xxx.sum",
    "answer.banks.51.xxx.sum_foreign",
    "answer.banks.52.xxx.sum",
    "answer.banks.52.xxx.sum_foreign",
    "answer.banks.53.xxx.sum",
    "answer.banks.53.xxx.sum_foreign",
    "answer.estate.23.xxx.costs",
    "answer.estate.23.xxx.costs_rent",
    "answer.estate.23.xxx.space",
    "answer.estate.24.xxx.costs",
    "answer.estate.24.xxx.costs_rent",
    "answer.estate.24.xxx.space",
    "answer.estate.25.xxx.costs",
    "answer.estate.25.xxx.costs_rent",
    "answer.estate.25.xxx.space",
    "answer.estate.26.xxx.costs",
    "answer.estate.26.xxx.costs_rent",
    "answer.estate.26.xxx.space",
    "answer.estate.27.xxx.costs",
    "answer.estate.27.xxx.costs_rent",
    "answer.estate.27.xxx.space",
    "answer.estate.28.xxx.costs",
    "answer.estate.28.xxx.costs_rent",
    "answer.estate.28.xxx.space",
    "answer.estate.29.xxx.costs_rent",
    "answer.estate.29.xxx.space",
    "answer.estate.30.xxx.costs_rent",
    "answer.estate.30.xxx.space",
    "answer.estate.31.xxx.costs_rent",
    "answer.estate.31.xxx.space",
    "answer.estate.32.xxx.costs_rent",
    "answer.estate.32.xxx.space",
    "answer.estate.33.xxx.costs_rent",
    "answer.estate.33.xxx.space",
    "answer.estate.34.xxx.costs_rent",
    "answer.estate.34.xxx.space",
    "answer.income.10.family",
    "answer.income.10.value",
    "answer.income.11.family",
    "answer.income.11.value",
    "answer.income.12.family",
    "answer.income.12.value",
    "answer.income.13.family",
    "answer.income.13.value",
    "answer.income.14.family",
    "answer.income.14.value",
    "answer.income.15.family",
    "answer.income.15.value",
    "answer.income.16.family",
    "answer.income.16.value",
    "answer.income.17.family",
    "answer.income.17.value",
    "answer.income.18.family",
    "answer.income.18.value",
    "answer.income.19.family",
    "answer.income.19.value",
    "answer.income.20.family",
    "answer.income.20.value",
    "answer.income.5.family",
    "answer.income.5.value",
    "answer.income.6.family",
    "answer.income.6.value",
    "answer.income.7.family",
    "answer.income.7.value",
    "answer.income.8.family",
    "answer.income.8.value",
    "answer.income.9.family",
    "answer.income.9.value",
    "answer.liabilities.54.sum",
    "answer.liabilities.54.sum_foreign",
    "answer.liabilities.55.sum",
    "answer.liabilities.55.sum_foreign",
    "answer.liabilities.56.sum",
    "answer.liabilities.56.sum_foreign",
    "answer.liabilities.57.sum",
    "answer.liabilities.57.sum_foreign",
    "answer.liabilities.58.sum",
    "answer.liabilities.58.sum_foreign",
    "answer.liabilities.59.sum",
    "answer.liabilities.59.sum_foreign",
    "answer.liabilities.60.sum",
    "answer.liabilities.60.sum_foreign",
    "answer.liabilities.61.sum",
    "answer.liabilities.61.sum_foreign",
    "answer.liabilities.62.sum",
    "answer.liabilities.62.sum_foreign",
    "answer.liabilities.63.sum",
    "answer.liabilities.63.sum_foreign",
    "answer.liabilities.64.sum",
    "answer.liabilities.64.sum_foreign",
    "answer.vehicle.35.xxx.sum",
    "answer.vehicle.35.xxx.sum_rent",
    "answer.vehicle.36.xxx.sum",
    "answer.vehicle.36.xxx.sum_rent",
    "answer.vehicle.37.xxx.sum",
    "answer.vehicle.37.xxx.sum_rent",
    "answer.vehicle.38.xxx.sum",
    "answer.vehicle.38.xxx.sum_rent",
    "answer.vehicle.39.xxx.sum",
    "answer.vehicle.39.xxx.sum_rent",
    "answer.vehicle.40.xxx.sum",
    "answer.vehicle.40.xxx.sum_rent",
    "answer.vehicle.41.xxx.sum",
    "answer.vehicle.41.xxx.sum_rent",
    "answer.vehicle.42.xxx.sum",
    "answer.vehicle.42.xxx.sum_rent",
    "answer.vehicle.43.xxx.sum",
    "answer.vehicle.43.xxx.sum_rent",
    "answer.vehicle.44.xxx.sum",
    "answer.vehicle.44.xxx.sum_rent"
]

TWO_IS_ENOUGH = [
    "answer.banks.45.xxx.sum",
    "answer.banks.45.xxx.sum_foreign",
    "answer.banks.45.xxx.sum_foreign_units",
    "answer.banks.45.xxx.sum_units",
    "answer.banks.46.xxx.sum",
    "answer.banks.46.xxx.sum_foreign",
    "answer.banks.46.xxx.sum_foreign_units",
    "answer.banks.46.xxx.sum_units",
    "answer.banks.47.xxx.sum",
    "answer.banks.47.xxx.sum_foreign",
    "answer.banks.47.xxx.sum_foreign_units",
    "answer.banks.47.xxx.sum_units",
    "answer.banks.48.xxx.sum",
    "answer.banks.48.xxx.sum_foreign",
    "answer.banks.48.xxx.sum_foreign_units",
    "answer.banks.48.xxx.sum_units",
    "answer.banks.49.xxx.sum",
    "answer.banks.49.xxx.sum_foreign",
    "answer.banks.49.xxx.sum_foreign_units",
    "answer.banks.49.xxx.sum_units",
    "answer.banks.50.xxx.sum",
    "answer.banks.50.xxx.sum_foreign",
    "answer.banks.50.xxx.sum_foreign_units",
    "answer.banks.50.xxx.sum_units",
    "answer.banks.51.xxx.sum",
    "answer.banks.51.xxx.sum_foreign",
    "answer.banks.51.xxx.sum_foreign_units",
    "answer.banks.51.xxx.sum_units",
    "answer.banks.52.xxx.sum",
    "answer.banks.52.xxx.sum_foreign",
    "answer.banks.52.xxx.sum_foreign_units",
    "answer.banks.52.xxx.sum_units",
    "answer.banks.53.xxx.sum",
    "answer.banks.53.xxx.sum_foreign",
    "answer.banks.53.xxx.sum_foreign_units",
    "answer.banks.53.xxx.sum_units",
    "answer.estate.23.xxx.costs",
    "answer.estate.23.xxx.costs_rent",
    "answer.estate.23.xxx.space",
    "answer.estate.24.xxx.costs",
    "answer.estate.24.xxx.costs_rent",
    "answer.estate.24.xxx.space",
    "answer.estate.25.xxx.costs",
    "answer.estate.25.xxx.costs_rent",
    "answer.estate.25.xxx.space",
    "answer.estate.26.xxx.costs",
    "answer.estate.26.xxx.costs_rent",
    "answer.estate.26.xxx.space",
    "answer.estate.27.xxx.costs",
    "answer.estate.27.xxx.costs_rent",
    "answer.estate.27.xxx.space",
    "answer.estate.28.xxx.costs",
    "answer.estate.28.xxx.costs_rent",
    "answer.estate.28.xxx.space",
    "answer.estate.29.xxx.costs_property",
    "answer.estate.29.xxx.costs_rent",
    "answer.estate.29.xxx.space",
    "answer.estate.30.xxx.costs_property",
    "answer.estate.30.xxx.costs_rent",
    "answer.estate.30.xxx.space",
    "answer.estate.31.xxx.costs_property",
    "answer.estate.31.xxx.costs_rent",
    "answer.estate.31.xxx.space",
    "answer.estate.32.xxx.costs_property",
    "answer.estate.32.xxx.costs_rent",
    "answer.estate.32.xxx.space",
    "answer.estate.33.xxx.costs_property",
    "answer.estate.33.xxx.costs_rent",
    "answer.estate.33.xxx.space",
    "answer.estate.34.xxx.costs_property",
    "answer.estate.34.xxx.costs_rent",
    "answer.estate.34.xxx.space",
    "answer.liabilities.54.sum",
    "answer.liabilities.54.sum_foreign",
    "answer.liabilities.55.sum",
    "answer.liabilities.55.sum_foreign",
    "answer.liabilities.56.sum",
    "answer.liabilities.56.sum_foreign",
    "answer.liabilities.57.sum",
    "answer.liabilities.57.sum_foreign",
    "answer.liabilities.58.sum",
    "answer.liabilities.58.sum_foreign",
    "answer.liabilities.59.sum",
    "answer.liabilities.59.sum_foreign",
    "answer.liabilities.60.sum",
    "answer.liabilities.60.sum_foreign",
    "answer.liabilities.61.sum",
    "answer.liabilities.61.sum_foreign",
    "answer.liabilities.62.sum",
    "answer.liabilities.62.sum_foreign",
    "answer.liabilities.63.sum",
    "answer.liabilities.63.sum_foreign",
    "answer.liabilities.64.sum",
    "answer.liabilities.64.sum_foreign",
    "answer.income.10.family",
    "answer.income.10.value",
    "answer.income.11.family",
    "answer.income.11.value",
    "answer.income.12.family",
    "answer.income.12.value",
    "answer.income.13.family",
    "answer.income.13.value",
    "answer.income.14.family",
    "answer.income.14.value",
    "answer.income.15.family",
    "answer.income.15.value",
    "answer.income.16.family",
    "answer.income.16.value",
    "answer.income.17.family",
    "answer.income.17.value",
    "answer.income.18.family",
    "answer.income.18.value",
    "answer.income.19.family",
    "answer.income.19.value",
    "answer.income.20.family",
    "answer.income.20.value",
    "answer.income.5.family",
    "answer.income.5.value",
    "answer.income.6.family",
    "answer.income.6.value",
    "answer.income.7.family",
    "answer.income.7.value",
    "answer.income.8.family",
    "answer.income.8.value",
    "answer.income.9.family",
    "answer.income.9.value",
    "answer.vehicle.35.xxx.sum",
    "answer.vehicle.35.xxx.sum_rent",
    "answer.vehicle.36.xxx.sum",
    "answer.vehicle.36.xxx.sum_rent",
    "answer.vehicle.37.xxx.sum",
    "answer.vehicle.37.xxx.sum_rent",
    "answer.vehicle.38.xxx.sum",
    "answer.vehicle.38.xxx.sum_rent",
    "answer.vehicle.39.xxx.sum",
    "answer.vehicle.39.xxx.sum_rent",
    "answer.vehicle.40.xxx.sum",
    "answer.vehicle.40.xxx.sum_rent",
    "answer.vehicle.41.xxx.sum",
    "answer.vehicle.41.xxx.sum_rent",
    "answer.vehicle.42.xxx.sum",
    "answer.vehicle.42.xxx.sum_rent",
    "answer.vehicle.43.xxx.sum",
    "answer.vehicle.43.xxx.sum_rent",
    "answer.vehicle.44.xxx.sum",
    "answer.vehicle.44.xxx.sum_rent"
]


def normalize_number(s):
    s = s.strip().replace(" ", "").replace(",", ".").rstrip(".")
    s = s.lstrip("0")
    if s.endswith(".0"):
        s = s[:-2]

    if s.endswith(".00"):
        s = s[:-3]

    return s


def cleanup(s, path):
    path = ".".join(map(lambda x: "xxx" if isinstance(x, int) else x, path))

    if path in FIELDS_TO_IGNORE:
        return s

    if isinstance(s, basestring):
        if path in FIELDS_TO_PROOFREAD:
            s = OPREF.process(s)

        s = s.replace("—", " - ")
        s = re.sub("([^\s])\-\s+", r"\1-", s)
        s = re.sub("\s+\-([^\s])", r"-\1", s)
        s = re.sub("\.([^\s])", r". \1", s)
        s = re.sub("\s*\(\s*", " (", s)
        s = re.sub("\s*\)\s*", ") ", s)
        s = s.replace(" ,", ", ")
        s = s.replace(" .", ". ")
        s = re.sub("\s+", " ", s)
        s.strip().rstrip(".")

        if path in FIELDS_TO_TITLIZE:
            s = title(s)

        if path in FIELDS_TO_CAPITALIZE and s:
            chunks = s.split(None, 1)
            s = " ".join([chunks[0].capitalize()] + chunks[1:])

        if path in FIELDS_TO_LOWERCASIZE and s:
            chunks = s.split(None, 1)
            s = " ".join([chunks[0].lower()] + chunks[1:])

        if path in FIELDS_TO_NUM_NORMALIZE:
            s = normalize_number(s)

        return s
    else:
        return s


class Flattener(object):
    def __init__(self):
        self.lists = {}
        self.fields = []

    def traverse(self, dct, current_answer, path):
        if isinstance(dct, dict):
            for k, v in dct.iteritems():
                if path:
                    current_path = path + tuple([k])
                else:
                    current_path = tuple([k])

                if isinstance(v, list):
                    self.lists[current_path] = max(
                        self.lists.get(current_path, 0),
                        len(v))

                    for i, val in enumerate(v):
                        self.traverse(val, current_answer,
                                      current_path + tuple([i]))
                else:
                    self.traverse(v, current_answer, current_path)
        else:
            if path not in self.fields:
                self.fields.append(path)

            current_answer[path] = cleanup(dct, path)

    def process_answer(self, answer):
        current_answer = defaultdict(str)
        self.traverse(answer, current_answer, tuple())

        for path in current_answer.keys():
            # Extra logic to cover the case when volunteers are writting
            # sums into comments field rather than value field
            if unify_path(path) in TWO_IS_ENOUGH:
                # if value field is empty
                if not current_answer[path]:
                    # And comment field looks like a number after normalization
                    comment_path = path[:-1] + (path[-1] + "_comment",)
                    comment = normalize_number(current_answer[comment_path])

                    # Let's put number from comment to value field
                    if re.search("^\d+([\.,]\d+)?$", comment):
                        current_answer[path] = comment
                        current_answer[comment_path] = "!MOVED_TO_VAL"

        return current_answer

    def process_task(self, task):
        return [self.process_answer(answer) for answer in task]

    @property
    def sorted_fields(self):
        return natsorted(self.fields,
                         key=lambda x: ".".join(map(to_str, x)))
