#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import sys
import re

from collections import defaultdict, Counter
from operator import itemgetter

import xlsxwriter
from natsort import natsorted

lists = {}
fields = []
current_answer = {}


def cleanup(s):
    if isinstance(s, basestring):
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


def traverse(dct, path):
    if isinstance(dct, dict):
        for k, v in dct.iteritems():
            if path:
                current_path = "%s.%s" % (path, k)
            else:
                current_path = k

            if isinstance(v, list):
                lists[current_path] = max(lists.get(current_path, 0), len(v))
                for i, val in enumerate(v):
                    traverse(val, "%s.%02d" % (current_path, i + 1))
            else:
                traverse(v, current_path)
    else:
        if path not in fields:
            fields.append(path)

        current_answer[path] = cleanup(dct)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    all_tasks = []

    with open(in_file, "r") as fp:
        for r in fp:
            # print(r)
            answers = json.loads(r)
            current_task = []

            for answer in answers:
                current_answer = defaultdict(str)
                traverse(answer, "")
                current_task.append(current_answer)

            all_tasks.append(current_task)

    fields = natsorted(fields)

    workbook = xlsxwriter.Workbook(out_file)
    worksheet = workbook.add_worksheet('Group&Clean')
    for i, f in enumerate(fields):
        worksheet.write_string(0, i, f)

    line_no = 1
    for task in all_tasks:
        if not task:
            print("Oups, no answers")
            continue
        for i, field in enumerate(fields):
            values = map(itemgetter(field), task)

            x = Counter(values)
            _, freq = x.most_common(1)[0]

            fmt = workbook.add_format()
            if freq == 1:
                fmt.set_bg_color('red')
            elif freq == 2:
                fmt.set_bg_color('yellow')

            for j, val in enumerate(values):
                worksheet.write_string(line_no + j, i, unicode(val), fmt)

        line_no += len(task)

    workbook.close()
