# from otree.api import *
import random
# import itertools
from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):
    def play_round(self):
        yield Intro, dict(income=random.randint(1, 150))
        # yield Detection, dict(detection_recipient_place=random.choice([True, False]))

        # if self.player.role == 'dictator':
        #     yield MyPage, dict(share=random.randint(0, 100))
        # yield DGDecision



        # if self.player.id_in_group == 1:
        #     yield Offer, dict(kept=cu(99))
        #     expect(self.player.payoff, cu(99))
        # else:
        #     expect(self.player.payoff, cu(1))
        # yield Results