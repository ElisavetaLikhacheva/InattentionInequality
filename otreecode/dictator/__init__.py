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
    NUM_ROUNDS = 2
    ENDOWMENT = cu(100)
    DICTATOR_ROLE = 'A'
    RECIPIENT_ROLE = 'Б'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    share = models.IntegerField(min=0, max=C.ENDOWMENT, label='Сколько Вы передадите игроку Б?')

    # detection_recipient_place — переменная с ответом игрока на вопрос о выявлении места партнера
    detection_recipient_place = models.BooleanField(label='Хотите ли Вы это сделать?')
    treatment = models.IntegerField()


class Player(BasePlayer):
    other_player_income = models.IntegerField()
    other_player_decile = models.IntegerField()


# FUNCTIONS
def set_payoffs(group):
    dictator = group.get_player_by_role('A')
    recipient = group.get_player_by_role('Б')
    dictator.payoff = C.ENDOWMENT - group.share
    recipient.payoff = group.share


def other_player(player: Player):
    return player.get_others_in_group()[0]


# PAGES
class WP1(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        treatment = itertools.cycle([1, 2, 3])
        subsession = group.subsession
        players = subsession.get_players()
        for p in players:
            if p.role == C.DICTATOR_ROLE:
                if p.participant.info:
                    if p.round_number > 1:
                        if 'treatment' in subsession.session.config:
                            p.group.treatment = subsession.session.config['treatment']
                        else:
                            p.group.treatment = next(treatment)
                    else:
                        p.group.treatment = 1
                else:
                    p.group.treatment = 0
        if group.treatment != 3:
            group.detection_recipient_place = 0
        print('WP1', group.treatment)


class WP2(WaitPage):
    pass


class Detection(Page):
    form_model = 'group'
    form_fields = ['detection_recipient_place']

    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.DICTATOR_ROLE and player.group.treatment == 3 and player.round_number != 1



class WP3(WaitPage):
    pass


class MainDictatorDecision(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.role == C.DICTATOR_ROLE

    form_model = 'group'
    form_fields = ['share']

    @staticmethod
    def vars_for_template(player: Player):
        other_player_income = int(other_player(player).participant.income)
        other_player_decile = int(other_player(player).participant.decile)
        return dict(other_player_income=other_player_income,
                    other_player_decile=other_player_decile)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class DGDecision(Page):
    pass


class IntroDQ(Page):
    pass


page_sequence = [
    # IncomeQ,
    WP1,
    Detection,
    WP2,
    MainDictatorDecision,
    ResultsWaitPage,
    DGDecision,
    IntroDQ,
]
