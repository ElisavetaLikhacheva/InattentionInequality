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
    Q_OPTIONS_ = [
        [1, 'Да'],
        [2, 'Скорее да'],
        [3, 'Скорее нет'],
        [4, 'Нет'],
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
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
    high_position_family = models.StringField(
        label='родиться в обеспеченной семье?',
        choices=C.Q_4_IMPORTANT,
        widget=widgets.RadioSelectHorizontal
    )
    high_position_education = models.StringField(
        label='получить хорошее образование?',
        choices=C.Q_4_IMPORTANT,
        widget=widgets.RadioSelectHorizontal
    )
    high_position_work = models.StringField(
        label='упорно работать?',
        choices=C.Q_4_IMPORTANT,
        widget=widgets.RadioSelectHorizontal
    )
    high_position_networking = models.StringField(
        label='знать нужных людей?',
        choices=C.Q_4_IMPORTANT,
        widget=widgets.RadioSelectHorizontal
    )
    high_position_social_elevators = models.StringField(
        label='развитые социальные лифты?',
        choices=C.Q_4_IMPORTANT,
        widget=widgets.RadioSelectHorizontal
    )




# PAGES
class InequalityAssessment(Page):
    form_model = 'player'
    form_fields = ['inequality_problem',
                   'income_increasing',
                   'income_satisfactory',
                   'income_deserving',
                   'high_position_family',
                   'high_position_education',
                   'high_position_work',
                   'high_position_networking',
                   'high_position_social_elevators',
                   # 'high_position_education',
                   ]




class Results(Page):
    pass


page_sequence = [
    # Intro,
    InequalityAssessment,
    # Results
]
