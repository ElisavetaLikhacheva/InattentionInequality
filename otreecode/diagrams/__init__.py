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
    )  # slider!

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
    income = models.IntegerField(
        label='Сколько в среднем ежемесячно Вы зарабатываете? (В тысячах рублей)',
        min=0
    )
    info = models.BooleanField()
    decile = models.IntegerField()


def creating_session(subsession):
    info = itertools.cycle([False, True, True, True])
    for player in subsession.get_players():
        if 'info' in subsession.session.config:
            player.info = subsession.session.config['info']
        else:
            player.info = next(info)
        print('set info to', player.info)


def participant_income_place(player: Player):
    true_decile = list([11349, 15957, 20404, 25082, 31100, 38050, 45000, 57821, 81466])
    if player.income <= int(true_decile[0] / 1000):
        player.decile = 1
    for i in range(0, 9):
        if player.income > int(true_decile[i] / 1000):
            player.decile = i + 2
        else:
            break
    return player.decile


# PAGES
class Intro(Page):
    pass


class InfoIncome(Page):
    form_model = 'player'
    form_fields = ['russian_pyramid',
                   'ideal_pyramid',
                   'median_income',
                   'poor_10',
                   'rich_10',
                   'percent_below',
                   'income'
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.info = player.info
        participant.income = player.income
        player.decile = participant_income_place(player)
        participant.decile = player.decile


class InfoTreatment(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.info == 1

    @staticmethod
    def js_vars(player: Player):
        return dict(decile=player.decile)

    @staticmethod
    def vars_for_template(player: Player):
        decile = participant_income_place(player)
        decile_below = []
        for i in range(1, decile):
            decile_below.append(i)

        max_decile_higher = len(decile_below) + 2
        decile_higher = []
        for j in range(max_decile_higher, 11):
            decile_higher.append(j)
        people_poorer = (decile - 1) * 10

        return dict(decile_below=decile_below,
                    decile_higher=decile_higher,
                    people_poorer=people_poorer)


class IntroDictator(Page):
    pass


page_sequence = [
    Intro,
    InfoIncome,
    InfoTreatment,
    # ResultsWaitPage,
    # IncomeQ,
    # Results,
    IntroDictator
]
