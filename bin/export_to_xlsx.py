#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import sys

from collections import Counter
from operator import itemgetter

import xlsxwriter
from flattener import Flattener, to_str


def parse_in_file(in_file):
    flattener = Flattener()
    all_tasks = []

    with open(in_file, "r") as fp:
        for r in fp:
            answers = json.loads(r)
            all_tasks.append(flattener.process_task(answers))

    return flattener.sorted_fields, all_tasks


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    fields, all_tasks = parse_in_file(in_file)
    conflicts_counter = Counter()

    workbook = xlsxwriter.Workbook(out_file)
    worksheet = workbook.add_worksheet('Group&Clean')
    for i, f in enumerate(fields):
        worksheet.write_string(0, i, ".".join(map(to_str, f)))

    line_no = 1
    for task in all_tasks:

        if not task:
            print("Oups, no answers")
            continue
        for i, field in enumerate(fields):
            values = map(itemgetter(field), task)

            x = Counter(values)
            _, freq = x.most_common(1)[0]

            fmt = None
            if freq == 1:
                conflicts_counter.update([freq])
                fmt = workbook.add_format()
                fmt.set_bg_color('red')
            elif freq == 2:
                conflicts_counter.update([freq])
                fmt = workbook.add_format()
                fmt.set_bg_color('yellow')

            for j, val in enumerate(values):
                if fmt is not None:
                    worksheet.write_string(line_no + j, i, unicode(val), fmt)
                else:
                    worksheet.write_string(line_no + j, i, unicode(val))

        line_no += len(task)

    workbook.close()

    print(conflicts_counter.most_common())
