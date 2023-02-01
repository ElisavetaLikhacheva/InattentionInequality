from os import environ


SESSION_CONFIGS = [
     dict(
         name='diag_dictator',
         display_name='diagrams and dictator',
         app_sequence=['diagrams', 'dictator'],
         num_demo_participants=2,
         distribution=True,
         # use_browser_bots=True
     ),
    dict(
         name='dictator',
         display_name='Perceived distrib',
         app_sequence=['dictator'],
         num_demo_participants=2,
         distribution=False
     ),
    dict(
         name='diagrams',
         display_name='Diagrams',
         app_sequence=['diagrams'],
         num_demo_participants=2,
         use_browser_bots=True
    ),
    dict(
         name='slider',
         display_name='slider',
         app_sequence=['slider'],
         num_demo_participants=1
    ),
    dict(
             name='dictator_only',
             display_name='dictator_only ',
             app_sequence=['dictator'],
             num_demo_participants=2,
             # use_browser_bots=True
        ),
    dict(
             name='dictator_respl',
             display_name='dictator with revealed respl (T3)',
             app_sequence=['dictator'],
             num_demo_participants=2,
             recipient_place=True
        ),
    dict(
             name='questionnaire',
             display_name='questionnaire only',
             app_sequence=['questionnaire'],
             num_demo_participants=1
        ),
    dict(
             name='dictator_with_recpl1',
             display_name='dictator with recpl1',
             app_sequence=['dictator'],
             num_demo_participants=2,
             recipient_place=True
        )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
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
