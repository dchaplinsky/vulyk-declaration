#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from collections import Counter
import json
from operator import itemgetter
import six
import sys
import xlsxwriter


from .flattener import (
    Flattener, to_str, FIELDS_TO_IGNORE, unify_path)


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

    red_fmt = workbook.add_format()
    red_fmt.set_bg_color('red')

    cyan_fmt = workbook.add_format()
    cyan_fmt.set_bg_color('cyan')

    yellow_fmt = workbook.add_format()
    yellow_fmt.set_bg_color('yellow')

    line_no = 1
    for task in all_tasks:

        if not task:
            print("Oups, no answers")
            continue
        for i, field in enumerate(fields):
            unified_path = unify_path(field)

            values = map(itemgetter(field), task)

            x = Counter(values)
            common_value, freq = x.most_common(1)[0]
            other_values_empty = all(
                map(lambda x: not x[0], x.most_common()[1:])
            )

            fmt = None
            use_common_value = False

            # Do not apply formatting for some fields like email or username
            if unified_path not in FIELDS_TO_IGNORE:
                if (unified_path.endswith("hidden") or
                        unified_path.endswith("unclear")) and "on" in values:
                    use_common_value = True
                    common_value = "on"

                    if values.count("on") < len(values):
                        fmt = cyan_fmt
                else:
                    if freq == 1:
                        conflicts_counter.update([freq])
                        fmt = red_fmt
                    elif freq == 2:
                        fmt = workbook.add_format()

                        # Check if field that has two common answers out of 3+
                        # belongs to the list of fields where two answers is
                        # enough
                        if (common_value and other_values_empty):
                            fmt = cyan_fmt
                            use_common_value = True
                        else:
                            fmt = yellow_fmt
                            conflicts_counter.update([freq])
                    elif freq >= 3:
                        use_common_value = True

            for j, val in enumerate(values):
                # TODO: move to flattener?
                if use_common_value:
                    val = common_value

                if fmt is not None:
                    worksheet.write_string(line_no + j, i, six.text_type(val), fmt)
                else:
                    worksheet.write_string(line_no + j, i, six.text_type(val))

        line_no += len(task)

    workbook.close()

    # Print, how many conflicts in groups we have
    print(conflicts_counter.most_common())
