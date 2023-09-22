from os import environ


SESSION_CONFIGS = [
    dict(
        name='full_bot',
        display_name='random (bot), 20 players',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=20,
        use_browser_bots=True
    ),
    dict(
        name='full_bot_4',
        display_name='random (bot), 4 players',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=4,
        use_browser_bots=True
    ),
    dict(
        name='NEW_DG',
        display_name='NEW_DG, without bots, 2',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        # use_browser_bots=True
    ),
    dict(
        name='treat_1',
        display_name='Treatment 1',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=1,
    ),
    dict(
        name='treat_2',
        display_name='Treatment 2',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=2,
    ),
    dict(
        name='treat_3',
        display_name='Treatment 3',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=3,
    ),
    dict(
        name='treat_4',
        display_name='Treatment 4',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=4,
    ),
    dict(
        name='treat_5',
        display_name='Treatment 5',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=5,
    ),
    dict(
        name='treat_6',
        display_name='Treatment 6',
        app_sequence=['IntroQ', 'dictator'],
        num_demo_participants=2,
        default_treatment=6,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.01, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['financial_conditions'] #here u can gige through apps
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
