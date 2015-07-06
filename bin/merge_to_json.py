import io
import sys
import json
from collections import Counter
from operator import itemgetter
from flattener import Flattener


def set_answer(answer, field, value):
    sub_answer = answer

    for step in field[:-1]:
        if step not in sub_answer:
            sub_answer[step] = {}
        sub_answer = sub_answer[step]

    sub_answer[field[-1]] = value

    return answer


def traverse_and_convert(dct):
    if isinstance(dct, dict):
        if all(map(lambda x: isinstance(x, int), dct.keys())):
            return [traverse_and_convert(dct[k]) for k in sorted(dct.keys())]
        else:
            for k, v in dct.iteritems():
                dct[k] = traverse_and_convert(v)

    return dct


if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]
    count = Counter()

    results = []
    with open(in_file, "r") as fp:
        for r in fp:
            answers = json.loads(r)

            flattener = Flattener()
            task_answers = flattener.process_task(answers)
            fields = flattener.sorted_fields

            grouped_answer = {}

            for field in fields:
                count.update(map(itemgetter(field), task_answers))
                set_answer(grouped_answer, field, dict(count))
                count.clear()

            results.append(traverse_and_convert(grouped_answer))

    with io.open(out_file, "w", encoding="utf-8") as fp:
        s = json.dumps(results, indent=4, ensure_ascii=False)
        fp.write(s)
