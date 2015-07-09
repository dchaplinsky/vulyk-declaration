#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import re
import sys
import shutil
import json
import os.path
from collections import Counter
from pprint import pprint

from unicodecsv import DictReader, DictWriter
from rfc6266 import parse_requests_response
import requests
from urllib2 import urlopen, URLError
from translitua import translitua


def expand_gdrive_download_url(url):
    """
    Converts google drive links like
    https://drive.google.com/file/d/BLAHBLAH/view?usp=sharing
    https://drive.google.com/open?id=0BygiyWAl79DMUVJ3cGp1OVN5clU&authuser=0
    to links that can be used for direct download from gdrive with requests
    """

    if "http://docs.google.com/viewer?url=" in url:
        url = url.replace("http://docs.google.com/viewer?url=", "")
        url = url.replace("&embedded=true", "")

    m = re.search(r"file\/d\/([^\/]+)\/", url)
    if m is None:
        m = re.search(r"open\?id=([^&]+)", url)

    if m:
        return "https://docs.google.com/uc?export=download&id=%s" % m.group(1)
    else:
        return url


def download_file(url, fname):
    url = expand_gdrive_download_url(url)
    s = requests.Session()

    if "://" not in url.lower():
        return "!error=local_file"

    if url.startswith("ftp://"):
        # Special case for FTP
        try:
            req = urlopen(str(url), timeout=60)

            fname = "%s.%s" % (
                fname,
                os.path.splitext(url)[-1].strip(".").lower()
                or "html")

            if os.path.exists(fname):
                return fname

            with open(fname, 'wb') as f:
                shutil.copyfileobj(req, f)
            req.close()
            return fname
        except URLError:
            return "!error=404"

    try:
        resp = s.get(url, stream=True, verify=False, timeout=30)
    except requests.exceptions.ConnectionError:
        return "!error=connection_error"
    except requests.exceptions.Timeout:
        return "!error=timeout"
    except UnicodeEncodeError:
        return "!error=russian"

    if resp.ok:
        parsed = parse_requests_response(resp)

        fname = "%s.%s" % (
            fname,
            os.path.splitext(parsed.filename_unsafe)[-1].strip(".").lower()
            or "html")

        if os.path.exists(fname):
            return fname

        with open(fname, "wb") as handle:
            for block in resp.iter_content(1024):
                handle.write(block)
        return fname

    return "!error=%s" % resp.status_code


def prepare_fullname(name):
    return translitua(
        name.strip().lower().replace(
            " ", "_").replace(
            " ", "_").replace(
            '"', "_").replace(
            "'", "_").replace(
            '`', "_").replace(
            "ы", "и"))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        exit("Not enough arguments")

    in_file = sys.argv[1]
    out_dir = sys.argv[2]

    cnt = Counter()
    types = Counter()
    names = Counter()

    new_header = (
        "Ведомство",
        "Регион",
        "Должность",
        "ФИО",
        "Ссылка",
        "Примечание",
        "Взято в работу",
        "Локальный файл",
        "Локальный pdf",
        "Конверсия")

    with open(in_file, "r") as fp, \
            open(os.path.join(out_dir, "out.csv"), "w") as f_out, \
            open(os.path.join(out_dir, "out.json"), "w") as f_json_out:

        r = DictReader(fp)
        w = DictWriter(f_out, new_header)
        w.writeheader()

        for line in r:
            if (line["Ведомство"] and line["ФИО"] and
                    line["Взято в работу"].lower() == ""):

                print(line["ФИО"])

                desired_name = os.path.join(
                    out_dir, prepare_fullname(line["ФИО"]))

                if desired_name in names:
                    desired_name += "_" + str(names[desired_name])

                names.update([desired_name])
                desired_file = desired_name + ".pdf"

                if os.path.exists(desired_file):
                    line["Локальный файл"] = desired_file
                    line["Локальный pdf"] = desired_file

                    line["Конверсия"] = "Да"
                else:
                    fname = download_file(
                        unicode(line["Ссылка"]),
                        desired_name)

                    bname, ext = os.path.splitext(fname)
                    ext = ext.strip(".").lower()
                    if ext == "html":
                        fname = "!error=html"

                    line["Локальный файл"] = fname
                    if fname.startswith("!"):
                        cnt.update([fname])

                        line["Локальный pdf"] = desired_file
                    else:
                        types.update([ext])

                        line["Локальный pdf"] = (
                            fname if ext == "pdf" else bname + ".pdf")

                    line["Конверсия"] = "Да" if ext == "pdf" else ""

                if line["Конверсия"] == "Да":
                    f_json_out.write(json.dumps({
                        "office": line["Ведомство"],
                        "region": line["Регион"],
                        "position": line["Должность"],
                        "full_name": line["ФИО"],
                        "link": "http://unshred.it/static/declarations/chosen_ones/mega_batch/%s" % os.path.basename(line["Локальный pdf"])
                    }) + os.linesep)

                    # shutil.copy(
                    #     line["Локальный pdf"],
                    #     os.path.join(out_dir, "to_upload"))

                line["Локальный pdf"] = os.path.basename(line["Локальный pdf"])
                w.writerow(line)

    pprint(cnt.most_common())
    pprint(types.most_common())
