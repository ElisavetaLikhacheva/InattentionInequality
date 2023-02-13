from os import environ


SESSION_CONFIGS = [
    dict(
         name='diagrams_info_0',
         display_name='Only diagrams with info=0',
         app_sequence=['diagrams'],
         num_demo_participants=2,
         info=0,
         # use_browser_bots=True
    ),
    dict(
         name='diagrams_info_1',
         display_name='Only diagrams with info=1',
         app_sequence=['diagrams'],
         num_demo_participants=2,
         info=1,
         # use_browser_bots=True
    ),
    dict(
         name='diagrams_dictator_random',
         display_name='diagrams and dictator random',
         app_sequence=['diagrams', 'dictator'],
         num_demo_participants=2,
         # use_browser_bots=True
     ),
    dict(
        name='diagrams_dictator',
        display_name='diagrams and dictator: info0(, quest0, detection0, rec_pl0)',
        app_sequence=['diagrams', 'dictator'],
        num_demo_participants=2,
        info=1,
        quest_detection_recipient_place=0,
        detection_recipient_place=0,
        recipient_place=0,
        # use_browser_bots=True
    ),
    dict(
        name='full',
        display_name='diagrams, dictator, questionnaire random',
        app_sequence=['diagrams', 'dictator', 'questionnaire'],
        num_demo_participants=2,
        # use_browser_bots=True
    ),
    dict(
         name='questionnaire',
         display_name='questionnaire only',
         app_sequence=['questionnaire'],
         num_demo_participants=1
        ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['income',
                      'info',
                      'decile']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ru'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '8604444008529'
