#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import json
from glob2 import glob
from nltk.tokenize import word_tokenize


class OpenRefine(object):
    """docstring for OpenRefine"""

    def __init__(self, list_of_edits, by_word=True):
        super(OpenRefine, self).__init__()
        self.repl = {}
        self.by_word = by_word

        for l in list_of_edits:
            self.load_edits(l)

        print("OpenRefine edits loaded: %s" % len(self.repl))

    def load_edits(self, fname):
        with open(fname, "r") as fp:
            edits = json.load(fp)

        for edit in edits:
            for subedit in edit["edits"]:
                for frm in subedit["from"]:
                    if frm in self.repl and subedit["to"] != self.repl[frm]:
                        print(", ".join([frm, self.repl[frm], subedit["to"]]))

                    self.repl[frm.lower()] = subedit["to"]

    def process(self, sentence):
        if self.by_word:
            return " ".join([
                self.repl.get(word, word)
                for word in word_tokenize(sentence.lower().strip('"'))
            ])
        else:
            return self.repl.get(sentence.lower(), sentence)


if __name__ == '__main__':
    opref = OpenRefine(glob("edits/*.json"))

    print(opref.process("прокурор відділу захисту прав і свобод громадян та інтересів держави кправління правозахисної та представницької діяльності Головного управління нагляду за доержанням законів у воєнній сфері Генеральної прокуратури України"))