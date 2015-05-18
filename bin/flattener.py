#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from natsort import natsorted
from collections import defaultdict


lists = {}

to_str = lambda x: "%02d" % (x + 1) if isinstance(x, int) else x


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

            current_answer[path] = cleanup(dct)

    def process_answer(self, answer):
        current_answer = defaultdict(str)
        self.traverse(answer, current_answer, tuple())

        return current_answer

    def process_task(self, task):
        return [self.process_answer(answer) for answer in task]

    @property
    def sorted_fields(self):
        return natsorted(self.fields,
                         key=lambda x: ".".join(map(to_str, x)))
