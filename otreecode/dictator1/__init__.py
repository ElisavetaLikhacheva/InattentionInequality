from otree.api import *
import random
import itertools

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'dictator'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 2
    ENDOWMENT = cu(100)
    # DICTATOR_ROLE = 'Dictator'
    # RECIPIENT_ROLE = 'Recipient'

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    share = models.IntegerField(min=0, max=C.ENDOWMENT, label='Сколько Вы передадите игроку В?')

    quest_detection_recipient_place = models.BooleanField(label='Хотите ли вы узнать место другого игрока?')
    detection_recipient_place = models.BooleanField()
    recipient_place = models.BooleanField()

class Player(BasePlayer):
    other_player_income = models.IntegerField()
    other_player_decile = models.IntegerField()


    # роль зависит от дохода, тот, у кого выше — dictator
    def role(player):
        other_player_income = other_player(player).participant.income
        if player.participant.income == other_player_income:
            if player.id_in_group == 1:
                return 'A'
            else:
                return 'B'
        if player.participant.income > other_player_income:
            return 'A'
        else:
            return 'B'



# FUNCTIONS
def set_payoffs(self):
    dictator = self.get_player_by_role('A')
    recipient = self.get_player_by_role('B')
    dictator.payoff = C.ENDOWMENT - self.share
    recipient.payoff = self.share

# def role(player):
#     players = player.get_others_in_group()
#     minimum_income = min([p.income for p in players])
#     # recipients = [p for p in players if p.income == group.minimum_income]
#     if self.participant.income == group.minimum_income:
#         return 'p1'
#     else:
#         return 'p2'

def other_player(player: Player):
    return player.get_others_in_group()[0]


# PAGES
class WP1(WaitPage):
    group_by_arrival_time = True

    @staticmethod
    def after_all_players_arrive(group: Group):
        quest_detect = itertools.cycle([True, False, False])
        players = group.get_players()
        for player in players:
            if player.participant.income != other_player(player).participant.income:
                max_income = max([p.participant.income for p in players])
                print('max income is', max_income)
                if player.participant.info and player.participant.income == max_income and player.round_number > 1:
                        player.group.quest_detection_recipient_place = next(quest_detect)
                        print('quest_detection_recipient_place is', player.group.quest_detection_recipient_place)
                else:
                    player.group.quest_detection_recipient_place = 0
            else:
                if player.participant.info and player.id_in_group == 1 and player.round_number > 1:
                    player.group.quest_detection_recipient_place = next(quest_detect)
                    print('quest_detection_recipient_place is', player.group.quest_detection_recipient_place)
                else:
                    player.group.quest_detection_recipient_place = 0



class WP2(WaitPage):
    pass

class Detection(Page):
    form_model = 'group'
    form_fields = ['detection_recipient_place']

    @staticmethod
    def is_displayed(player: Player):
        return player.group.quest_detection_recipient_place == 1 and player.role() == 'A' and player.participant.info == 1

class WP3(WaitPage):
    @staticmethod
    def after_all_players_arrive(group: Group):
        recipient_place = itertools.cycle([False, True])
        # for p in group.get_players():
        if group.quest_detection_recipient_place:
            group.recipient_place = group.detection_recipient_place
        # elif not p.participant.info:
        #     group.recipient_place = group.detection_recipient_place = 0
        else:
            group.detection_recipient_place = 0
            group.recipient_place = next(recipient_place)
        print('recipient_place is WP3', group.recipient_place)





    # @staticmethod
    # def after_all_players_arrive(group: Group):
    #     print('in func WP3')
    #     recipient_place = itertools.cycle([False, True])
    #     for player in group.get_players():
    #         print('in for cycle WP3')
    #         if not player.participant.info and player.role != 'A':
    #             # if player.round_number>1:
    #             player.group.recipient_place = player.group.detection_recipient_place = 0
    #         else:
    #             if player.group.quest_detection_recipient_place:
    #                 player.group.recipient_place = player.group.detection_recipient_place
    #             else:
    #                 player.group.detection_recipient_place = 0
    #                 player.group.recipient_place = next(recipient_place)
    #         print('recipient_place is WP3', player.group.recipient_place)
    #         # else:
    #         #     player.group.recipient_place = next(recipient_place)

class MainDictatorDecision(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'A'

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
