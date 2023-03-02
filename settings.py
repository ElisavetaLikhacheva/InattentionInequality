from os import environ
#
# from otree.api import (
#     models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
#     Currency as c, currency_range
# )

import os

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


SESSION_CONFIGS = [
    # dict(
    #     name='public_goods',
    #     display_name="Public Goods",
    #     num_demo_participants=3,
    #     app_sequence=['public_goods', 'payment_info'],
    # ),
    # dict(
    #     name='guess_two_thirds',
    #     display_name="Guess 2/3 of the Average",
    #     num_demo_participants=3,
    #     app_sequence=['guess_two_thirds', 'payment_info'],
    # ),
    # dict(
    #     name='survey',
    #     display_name='survey',
    #     num_demo_participants=1,
    #     app_sequence=['survey', 'payment_info'],
    # ),
    {
        'name': 'my_survey',
        'display_name': "Опрос базовый Алматы",
        'num_demo_participants': 5,
        'app_sequence': ['my_survey'],
        'use_browser_bots': False
    },
    {
        'name': 'PG_standard',
        'display_name': "Базовая игра",
        'num_demo_participants': 5,
        'app_sequence': ['PG_standard'],
        'use_browser_bots': True
    },
    {
        'name': 'PG_standard_6',
        'display_name': "Базовая игра_6",
        'num_demo_participants': 6,
        'app_sequence': ['PG_standard_6'],
        'use_browser_bots': False
    },

    # {
    #     'name': 'PG_try',
    #     'display_name': "Групповая игра (драфт)",
    #     'num_demo_participants': 5,
    #     'app_sequence': ['PG_try'],Поскольку у игрока 1
    # },
    {
        'name': 'PG_punishment',
        'display_name': "Базовая игра с наказаниями",
        'num_demo_participants': 5,
        'app_sequence': ['PG_standard', 'PG_punishment', 'my_survey'],
        'use_browser_bots': False
    },
    {
        'name': 'PG_punishment_6',
        'display_name': "Базовая игра с наказаниями_6",
        'num_demo_participants': 6,
        'app_sequence': ['PG_punishment_6'],
        'use_browser_bots': False,
    },
    {
        'name': 'PG_threshold',
        'display_name': "Пороговая игра",
        'num_demo_participants': 5,
        'app_sequence': ['PG_threshold'],
        'use_browser_bots': False,
    },
    {
        'name': 'PG_threshold_6',
        'display_name': "Пороговая игра_6",
        'num_demo_participants': 6,
        'app_sequence': ['PG_threshold_6'],
        'use_browser_bots': True,
    },
    {
        'name': 'PG_punishment_threshold',
        'display_name': "Пороговая игра с наказаниями",
        'num_demo_participants': 5,
        'app_sequence': ['PG_punishment_threshold'], #'PG_threshold_6',
        'use_browser_bots': True,
    },
    {
        'name': 'PG_emotions',
        'display_name': "Общественное благо с эмоциями",
        'num_demo_participants': 6,
        'app_sequence': ['PG_emotions'],
    },

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = '' # 'USD'
USE_POINTS = True
ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
    dict(name='roomfor20', display_name='Room for 20', participant_label_file='PlayerList20.txt',),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = 'nb462pbifxhhq2@s1u=dc5+_(w$(k25b%7c_(se2b+zt=^@lcj'

INSTALLED_APPS = ['otree']
