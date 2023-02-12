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
    share = models.IntegerField(min=0, max=C.ENDOWMENT, label='Сколько Вы передадите игроку В?')

    quest_detection_recipient_place = models.BooleanField(label='Хотите ли вы узнать место другого игрока?')
    detection_recipient_place = models.BooleanField(label='Хотите ли Вы это сделать?')
    recipient_place = models.BooleanField()


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
        quest_detect = itertools.cycle([True, False, False])
        subsession = group.subsession
        players = subsession.get_players()
        for p in players:
            if p.role == C.DICTATOR_ROLE:
                if p.participant.info and p.round_number > 1:
                    p.group.quest_detection_recipient_place = next(quest_detect)
                else:
                    p.group.quest_detection_recipient_place = False
        print('WP1', group.quest_detection_recipient_place)

class WP2(WaitPage):
    pass


class Detection(Page):
    form_model = 'group'
    form_fields = ['detection_recipient_place']

    @staticmethod
    def is_displayed(player: Player):
        return player.group.quest_detection_recipient_place and player.role == C.DICTATOR_ROLE and player.participant.info


class WP3(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        recipient_place = itertools.cycle([True, False])
        subsession = group.subsession
        players = subsession.get_players()
        for p in players:
            if p.role == C.DICTATOR_ROLE:
                if p.participant.info and p.round_number > 1:
                    if not p.group.quest_detection_recipient_place:
                        p.group.detection_recipient_place = False
                        p.group.recipient_place = next(recipient_place)
                    else:
                        p.group.recipient_place = p.group.detection_recipient_place
                else:
                    p.group.recipient_place = p.group.detection_recipient_place = False



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




page_sequence = [
    # IncomeQ,
    WP1,
    # WP2,
    Detection,
    WP3,
    MainDictatorDecision,
    ResultsWaitPage,
    DGDecision
]
