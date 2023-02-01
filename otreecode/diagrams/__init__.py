from otree.api import *
import random
import itertools

doc = """
Your app description
"""



class C(BaseConstants):
    NAME_IN_URL = 'diagrams'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    Q_PYRAMIDS = [
        [1, 'A'],
        [2, 'B'],
        [3, 'C'],
        [4, 'D'],
        [5, 'E']
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    russian_pyramid = models.StringField(
        label='Как Вы считаете, какая диаграмма наиболее близка к обществу России сегодня?',
        choices=C.Q_PYRAMIDS,
        widget=widgets.RadioSelectHorizontal
    )

    ideal_pyramid = models.StringField(
        label='Какой тип общества Вы бы предпочли?',
        choices=C.Q_PYRAMIDS,
        widget=widgets.RadioSelectHorizontal
    )

    median_income = models.IntegerField(
        label='Как вы думаете, сколько составляет медианный ежемесячный доход в России?',
        min=0
    ) #slider!

    poor_10 = models.IntegerField(
        label='Как Вы думаете, какой средний ежемесячный доход у 10% самых бедных жителей России?',
        min=0
    )

    rich_10 = models.IntegerField(
        label='Как Вы думаете, какой средний ежемесячный доход у 10% самых богатых жителей России?',
        min=0
    )

    percent_below = models.IntegerField(
        label='Как Вы думаете, какой процент людей в России зарабатывает меньше, чем Вы?',
        min=0, max=100
    )

    info = models.BooleanField()

def creating_session(subsession):
    info = itertools.cycle([False, True, True, True])
    for player in subsession.get_players():
        player.info = next(info)
        print('set info to', player.info)

# PAGES
# class Intro(Page):
#

class InfoIncome(Page):
    form_model = 'player'
    form_fields = ['russian_pyramid',
                   'ideal_pyramid',
                   'median_income',
                   'poor_10',
                   'rich_10',
                   'percent_below',
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        # participant.income = player.income
        participant.info = player.info

class InfoTreatment(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.info == 1

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [
    # Intro,
    InfoIncome,
    InfoTreatment,
    ResultsWaitPage,
    Results
]
