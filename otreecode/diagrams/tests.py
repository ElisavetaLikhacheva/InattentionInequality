# from otree.api import *
import random
# import itertools
from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):
    def play_round(self):
        # yield Intro
        yield InfoIncome, dict(russian_pyramid=random.choice([1, 2, 3, 4, 5]),
                               ideal_pyramid=random.choice([1, 2, 3, 4, 5]),
                               median_income=random.randint(0, 100),
                               poor_10=random.randint(0, 100),
                               rich_10=random.randint(0, 100),
                               percent_below=random.randint(0, 100),
                               income=random.randint(0, 120)
                               )

        if self.player.info == 1:
            yield InfoTreatment,
        # yield IncomeQ, dict(income=random.randint(1, 150))


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