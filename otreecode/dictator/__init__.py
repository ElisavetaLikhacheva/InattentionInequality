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
    ENDOWMENT = 100
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
    income = models.IntegerField(
        label='Сколько в среднем ежемесячно Вы зарабатываете? (В тысячах рублей)',
        min=0
    )
    other_player_decile = models.IntegerField()
    decile = models.IntegerField()

    # роль зависит от дохода, тот, у кого выше — dictator
    def role(player):
        other_player_income = other_player(player).participant.income
        if player.participant.income == other_player_income:
            return random.choice(['A', 'B'])
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


# def role(self):
#     players = self.get_others_in_group()
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
        print('in func')
        quest_detect = itertools.cycle([True, False])
        for player in group.get_players():
            print(player.participant.info, player.round_number, 'xnjsjnck')
            if player.participant.info:
                if player.round_number > 1:
                    print('in for cycle')
                    player.group.quest_detection_recipient_place = next(quest_detect)
                    print('quest_detection_recipient_place is', player.group.quest_detection_recipient_place)
                else:
                    player.group.quest_detection_recipient_place = 0
            else:
                player.group.quest_detection_recipient_place = 0

class Intro(Page):
    form_model = 'player'
    form_fields = ['income']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.income = player.income
        if player.income < 31:
            player.decile = 1
        else:
            player.decile = 2
        participant.decile = player.decile

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class WP2(WaitPage):
    pass

class Detection(Page):
    form_model = 'group'
    form_fields = ['detection_recipient_place']

    @staticmethod
    def is_displayed(player: Player):
        return player.group.quest_detection_recipient_place == 1 and player.role() == 'A' and player.participant.info == 1
        # and player.round_number>1

class WP3(WaitPage):
    # TODO: подумать над логикой для if — вроде ок

    @staticmethod
    def after_all_players_arrive(group: Group):
        print('in func WP3')
        recipient_place = itertools.cycle([False, True])
        if group.quest_detection_recipient_place:
            group.recipient_place = group.detection_recipient_place
        else:
            group.detection_recipient_place = 0
            group.recipient_place = next(recipient_place)
        print('recipient_place is WP3', group.recipient_place)

        

        # for player in group.get_players():
        #     print('in for cycle WP3')
        #     if not player.participant.info and player.role != 'A':
        #         # if player.round_number>1:
        #         player.group.recipient_place = player.group.detection_recipient_place = 0
        #     else:
        #         if
                        # else:
                        #     player.group.recipient_place = next(recipient_place)





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

class MyPage(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.role() == 'A'

    form_model = 'group'
    form_fields = ['share']

    @staticmethod
    def vars_for_template(player: Player):
        other_player_income = other_player(player).participant.income
        if other_player_income < 31:
            other_player_decile = 1
        else:
            other_player_decile = 2
        return dict(other_player_income=other_player_income,
                    other_player_decile=other_player_decile)
# TODO здесь чтоже что-то с доходом и децилями

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'


class DGDecision(Page):
    pass
    # for player in group.get_others_in_group():
    #     player.recipplinfo = player.income
    #     return player.recipplinfo
    # pass
    # @staticmethod
    # def vars_for_template(player: Player):
    #     partner = get_partner(player)
    #     my_partner_previous = partner.in_all_rounds()
    #     my_previous_partners = [
    #         get_partner(me_prev) for me_prev in player.in_all_rounds()
    #     ]
    #
    #     return dict(
    #         partner=partner,
    #         my_partner_previous=my_partner_previous,
    #         my_previous_partners=my_previous_partners,
    #     )


# for player in subsession.get_players():
#             participant = player.participant
#             participant.time_pressure = random.choice([True, False])





    # здесь почти работающий код:)
    # @staticmethod
    # def after_all_players_arrive(group: Group):
    #     print('in func')
    #     recipient_place = itertools.cycle([True, False])
    #     quest_detect = itertools.cycle([True, False])
    #     for player in group.get_players():
    #         print('in for cycle')
    #         player.group.recipient_place = next(recipient_place)
    #         player.group.quest_detection_recipient_place = next(quest_detect)
    #         if not player.group.quest_detection_recipient_place:
    #             print('in if condition')
    #             player.group.detection_recipient_place = 0
    #             player.group.recipient_place = 0
    #         print('recipient_place is', player.group.recipient_place)








page_sequence = [
    WP1,
    Intro,
    WP2,
    Detection,
    WP3,
    MyPage,
    ResultsWaitPage,
    DGDecision
]
