from otree.api import *
import random
import itertools

doc = """
Your app description
"""


# np.random.seed(0)
class C(BaseConstants):
    NAME_IN_URL = 'dictator'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    DICTATOR_ROLE = 'A'
    RECIPIENT_ROLE = 'Б'

    Q_GENDER = [
        [1, 'Мужской'],
        [2, 'Женский'],
    ]
    Q_FINANCIAL_CONDITIONS = [
        [1, 'Денег не хватает даже на питание'],
        [2, 'На питание денег хватает, но не хватает на покупку одежды и обуви'],
        [3, 'На покупку одежды и обуви денег хватает, но не хватает на покупку мелкой бытовой техники'],
        [4, 'На покупку мелкой бытовой техники денег хватает, но не хватает на покупку крупной бытовой техники'],
        [5, 'Денег хватает на покупку крупной бытовой техники, но мы не сможем купить новую машину'],
        [6, 'На новую машину денег хватает, но мы не можем купить небольшую квартиру'],
        [7, 'На небольшую квартиру денег хватает, но мы не смогли бы купить большую квартиру в хорошем районе'],
        [8, 'Материальных затруднений не испытываем, при необходимости могли бы приобрести квартиру, дом'],
        [9, 'Затрудняюсь ответить'],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    share = models.IntegerField(min=0, max=C.ENDOWMENT, label='Сколько Вы передадите игроку Б?')
    treatment = models.IntegerField()

    check_info = models.BooleanField(label='Хотите ли Вы узнать?')
    avoid_info = models.BooleanField(label='Хотите ли Вы пропустить?')


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
    financial_conditions = models.StringField(
        label='Пожалуйста, выберите утверждение, которое наиболее точно описывает Ваше финансовое положение.',
        choices=C.Q_FINANCIAL_CONDITIONS,
        widget=widgets.RadioSelect
    )
    other_player_income = models.IntegerField()


# FUNCTIONS
def set_payoffs(group):
    dictator = group.get_player_by_role('A')
    recipient = group.get_player_by_role('Б')
    dictator.payoff = C.ENDOWMENT - group.share
    recipient.payoff = group.share


def other_player(player: Player):
    return player.get_others_in_group()[0]


def creating_session(subsession):
    subsession.group_randomly(fixed_id_in_group=True)


# PAGES
class IncomeQ(Page):
    form_model = 'player'
    form_fields = ['year_of_birth',
                   'gender',
                   'financial_conditions',
                   ]



class WP1(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        treatment = itertools.cycle([2, 3, 4, 5, 6])
        subsession = group.subsession
        players = subsession.get_players()
        for p in players:
            p.group.treatment = next(treatment)

    # @staticmethod
    # def after_all_players_arrive(group: Group):
    #     treatment = itertools.cycle([1, 2, 3])
    #     subsession = group.subsession
    #     players = subsession.get_players()
    #     for p in players:
    #         if p.role == C.DICTATOR_ROLE:
    #             if p.participant.info:
    #                 if p.round_number > 1:
    #                     if 'treatment' in subsession.session.config:
    #                         p.group.treatment = subsession.session.config['treatment']
    #                     else:
    #                         p.group.treatment = next(treatment)
    #                 else:
    #                     p.group.treatment = 1
    #             else:
    #                 p.group.treatment = 0
    #     if group.treatment != 3:
    #         group.detection_recipient_place = 0
    #     print('WP1', group.treatment)


class WP2(WaitPage):
    pass


class Detection(Page):
    form_model = 'group'
    form_fields = ['check_info',
                   ]

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.DICTATOR_ROLE and 2 < player.group.treatment < 6

class DetectionAvoid(Page):
    form_model = 'group'
    form_fields = ['avoid_info',
                   ]

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.DICTATOR_ROLE and player.group.treatment == 6



class WP3(WaitPage):
    pass


class MainDictatorDecision(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.DICTATOR_ROLE

    form_model = 'group'
    form_fields = ['share']

    # @staticmethod
    # def vars_for_template(player: Player):
    #     other_player_income = int(other_player(player).participant.income)
    #     other_player_decile = int(other_player(player).participant.decile)
    #     return dict(other_player_income=other_player_income,
    #                 other_player_decile=other_player_decile)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class DGDecision(Page):
    pass


class IntroDQ(Page):
    pass


page_sequence = [
    WP1,
    IncomeQ, # replace to the first page
    Detection,
    DetectionAvoid,
    WP2,
    MainDictatorDecision,
    ResultsWaitPage,
    DGDecision,
    # IntroDQ,
]
