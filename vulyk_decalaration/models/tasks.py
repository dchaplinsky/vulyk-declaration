# -*- coding: utf-8 -*-

from mongoengine import DictField, StringField

from vulyk.models.tasks import AbstractTask, AbstractAnswer
from vulyk.models.task_types import AbstractTaskType


class DeclarationTask(AbstractTask):
    """
    Declaration Task to work with Vulyk.
    """
    pass


class DeclarationAnswer(AbstractAnswer):
    """
    Declaration Answer to work with Vulyk
    """
    pass


class DeclarationTaskType(AbstractTaskType):
    """
    Declaration Task to work with Vulyk.
    """
    answer_model = DeclarationAnswer
    task_model = DeclarationTask

    template = "index.html"
    helptext_template = "help.html"
    type_name = "declaration_task"

    redundancy = 3

    JS_ASSETS = ["static/scripts/keymaster.js",
                 "static/scripts/handlebars.js",
                 "static/scripts/bootstrap-select.js",
                 "static/scripts/base.js"]

    CSS_ASSETS = ["static/styles/bootstrap-select.css",
                  "static/styles/base.css"]
