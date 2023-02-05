from otree.api import *
import random
import itertools

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    Q_GENDER = [
        [1, 'Мужской'],
        [2, 'Женский'],
        [3, 'Другой'],
    ]
    Q_EDUCATION = [
        [1, 'Начальное общее образование (4 класса)'],
        [2, 'Основное общее образование (9 классов)'],
        [3, 'Среднее (полное) общее образование (11 классов)'],
        [4, 'Среднее профессиональное образование (колледж/техникум)'],
        [5, 'Основное общее образование (9 классов)'],
        [6, 'Бакалавриат'],
        [7, 'Cпециалитет, магистратура'],
        [8, 'Аспирантура'],
    ]
    Q_MARRIAGE = [
        [1, 'Никогда не состоял(a)'],
        [2, 'В зарегистрированном браке'],
        [3, 'В незарегистрированном браке'],
        [4, 'Вдовец (вдова)'],
        [5, 'Разведен (разведена)']

    ]
    Q_INEQUALITY_PROBLEM = [
        [1, 'Не проблема вообще'],
        [2, 'Небольшая проблема'],
        [3, 'Проблема'],
        [4, 'Серьезная проблема'],
        [5, 'Очень серьезная проблема']
    ]
    Q_INCOME_INCREASING = [
        [1, 'Возросло'],
        [2, 'Не изменилось'],
        [3, 'Снизилось'],
    ]
    Q_4_YES_NO = [
        [1, 'Да'],
        [2, 'Скорее да'],
        [3, 'Скорее нет'],
        [4, 'Нет'],
    ]
    Q_4_IMPORTANT = [
        [1, 'Очень важно'],
        [2, 'Довольно важно'],
        [3, 'Не очень важно'],
        [4, 'Совсем неважно'],
    ]
    Q_TRUST = [
        [1, 'Почти всегда людям можно доверять'],
        [2, 'Обычно людям можно доверять'],
        [3, 'Обычно стоит быть осторожным в общении с людьми'],
        [4, 'Почти всегда нужно быть осторожным в общении с людьми'],
    ]
    Q_PARTY = [
        [1, 'Единая Россия'],
        [2, 'Коммунистическая партия Российской Федерации'],
        [3, 'Справедливая Россия — За правду'],
        [4, 'Либерально-демократическая партия России'],
        [5, 'Новые люди'],
        [6, 'Другая зарегестрированная партия'],
        [7, 'Нет партии, которая могла бы представлять мои интересы'],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

def high_position(label):
    return models.IntegerField(label=label, choices=C.Q_4_IMPORTANT, widget=widgets.RadioSelect)
def scale(label):
    return models.IntegerField(label=label, choices=range(1, 11), widget=widgets.RadioSelectHorizontal)


class Player(BasePlayer):
    year_of_birth = models.IntegerField(
        label='В каком году Вы родились?',
        min=1900,
        max=2022
    )
    gender = models.StringField(
        label='Пожалуйста, укажите Ваш пол.',
        choices=C.Q_GENDER,
        widget=widgets.RadioSelectHorizontal
    )
    education = models.StringField(
        label='Пожалуйста, укажите наивысшую оконченную ступень образования.',
        choices=C.Q_EDUCATION,
        widget=widgets.RadioSelect
    )
    marriage = models.StringField(
        label='Пожалуйста, укажите Ваш брачный статус',
        choices=C.Q_MARRIAGE,
        widget=widgets.RadioSelect
    )
    children = models.IntegerField(
        label='Сколько у Вас детей?',
        min=0
    )
    children_live = models.IntegerField(
        label='Сколько из них проживает с Вами?',
        min=0
    )

    #q related to inequality
    inequality_problem = models.StringField(
        label='Как Вы думаете, неравенство — серьезная проблема в России?',
        choices=C.Q_INEQUALITY_PROBLEM,
        widget=widgets.RadioSelect
    )
    income_increasing = models.StringField(
        label='Как Вы думаете, неравенство доходов возросло или снизилось в последние годы в России?',
        choices=C.Q_INCOME_INCREASING,
        widget=widgets.RadioSelect
    )
    income_satisfactory = models.StringField(
        label='Довольны ли Вы своим заработком?',
        choices=C.Q_4_YES_NO,
        widget=widgets.RadioSelectHorizontal
    )
    income_deserving = models.StringField(
        label='Как Вы считаете, люди с высоким заработком заслуживают такой уровень дохода?',
        choices=C.Q_4_YES_NO,
        widget=widgets.RadioSelectHorizontal
    )
    unemployment_100 = models.IntegerField(
        label='Как Вы думаете, сколько человек из каждых 100 людей на данный момент не имеет работы и ищет её?',
        min=0,
        max=100)
    high_position_family = high_position('родиться в обеспеченной семье?')
    high_position_education = high_position('получить хорошее образование?')
    high_position_work = high_position('упорно работать?')
    high_position_networking = high_position('знать нужных людей?')
    high_position_social_elevators = high_position('иметь в стране развитые социальные лифты?')

    #political preferences
    general_trust = models.IntegerField(
        label='Могли бы Вы сказать, что в целом людям стоит доверять или нужно быть осторожным?',
        choices=C.Q_TRUST,
        widget=widgets.RadioSelect,
    )
    trust_country = scale('Государству в целом')
    trust_political_parties = scale('Политическим партиям')
    trust_government = scale('Правительству')
    trust_courts = scale('Судам и судебной системе')
    trust_television = scale('Телевидение')
    trust_mass_media = scale('Новостные средства массовой информации')

    social_mobility = scale('Как Вы считаете, насколько хорошо работают социальные лифты в России?')
    politics_interest = scale('Можете ли Вы описать себя как человека, который интересуется политикой? ')
    effort_luck = scale('')
    responsibility = scale('')
    income_equality = scale('')
    left_right = scale('')

    party_vote = models.StringField(
        label='За какую партию Вы голосовали на выборах в Государственную думу, если бы они состоялись сегодня?',
        choices=C.Q_PARTY,
        widget=widgets.RadioSelect
    )

    democracy_redistribution = scale('Правительство берет налоги с богатых для поддержки бедных')
    democracy_elections = scale('Люди выбирают политических лидеров на свободных выборах')
    democracy_unemployment_allowance = scale('Безработные получают государственное пособие')
    democracy_income_equality = scale('Государство обеспечивает равенство доходов')
    democracy_order = scale('Люди подчиняются властям')
    democracy_gender_equality = scale('У мужчин и женщин равные права')

    important_democracy = scale('Насколько для Вас важно жить в демократической стране?')
    Russia_democracy = scale('Как Вы считаете, насколько демократично управляется Россия в настоящее время?')


def children_live_max(player):
    return player.children
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['year_of_birth',
                   'gender',
                   'education',
                   'marriage',
                   'children',
                   'children_live'
                   ]


class InequalityAssessment(Page):
    form_model = 'player'
    form_fields = ['inequality_problem',
                   'income_increasing',
                   'income_satisfactory',
                   'income_deserving',
                   'unemployment_100',
                   'high_position_family',
                   'high_position_education',
                   'high_position_work',
                   'high_position_networking',
                   'high_position_social_elevators',
                   ]

class PoliticalPreferences(Page):
    form_model = 'player'
    form_fields = [
        'general_trust',
        'trust_country',
        'trust_political_parties',
        'trust_government',
        'trust_courts',
        'trust_television',
        'trust_mass_media',
        'social_mobility',
        'politics_interest',
        'effort_luck',
        'responsibility',
        'income_equality',
        'left_right',
        'party_vote',

        'democracy_redistribution',
        'democracy_elections',
        'democracy_unemployment_allowance',
        'democracy_income_equality',
        'democracy_order',
        'democracy_gender_equality',

        'important_democracy',
        'Russia_democracy',
    ]

class BackgroundInfo(Page):
    pass

class Results(Page):
    pass


page_sequence = [
    # Intro,
    Demographics,
    InequalityAssessment,
    PoliticalPreferences,
    BackgroundInfo,
    # HighPosition,

    # Results
]
