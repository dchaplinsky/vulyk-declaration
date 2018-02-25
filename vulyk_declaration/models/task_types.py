# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from vulyk.blueprints.gamification.models.task_types import (
    AbstractGamifiedTaskType, POINTS_PER_TASK_KEY, COINS_PER_TASK_KEY,
    IMPORTANT_KEY)

from vulyk_declaration.models.tasks import DeclarationAnswer, DeclarationTask


class DeclarationTaskType(AbstractGamifiedTaskType):
    """
    Declaration Task to work with Vulyk.
    """
    answer_model = DeclarationAnswer
    task_model = DeclarationTask

    name = 'Декларації'
    description = 'Розпізнавання декларацій'

    template = 'index.html'
    helptext_template = 'help.html'
    type_name = 'declaration_task'

    redundancy = 3

    _task_type_meta = {
        POINTS_PER_TASK_KEY: 1.0,
        COINS_PER_TASK_KEY: 1.0,
        IMPORTANT_KEY: True
    }

    JS_ASSETS = ['static/scripts/jquery-ui.min.js',
                 'static/scripts/handlebars.js',
                 'static/scripts/jquery.validate.min.js',
                 'static/scripts/messages_uk.min.js',
                 'static/scripts/jquery-cloneya.min.js',
                 'static/scripts/jquery.dateSelectBoxes.js',
                 'static/scripts/jquery.placeholder.min.js',
                 'static/scripts/jquery.serializejson.js',
                 'static/scripts/data.js',
                 'static/scripts/main.js']

    CSS_ASSETS = ['static/styles/core-style.css',
                  'static/styles/style.css']
