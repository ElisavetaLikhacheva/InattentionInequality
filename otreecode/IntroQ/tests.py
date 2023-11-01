# from otree.api import *
import random
# import itertools
from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield InstructionGeneral,
        yield IntroQ, dict(year_of_birth=random.randint(1900, 2022),
                          gender=random.choice([1, 2]),
                          financial_conditions=random.randint(1, 6),
                               )
        yield InstructionDG,
        yield UnderstandingDG, dict(quiz1=100,
                                    quiz2=False,
                                    quiz3=150)

        # # yield Intro, dict(income=random.randint(1, 150))
        #
        # if self.player.role == C.DICTATOR_ROLE and  self.player.group.treatment == 3:
        #     yield Detection, dict(detection_recipient_place=random.choice([True, False])
        #                           )
        #
        # if self.player.role == C.DICTATOR_ROLE:
        #     yield MainDictatorDecision, dict(share=random.randint(0, 100))
        #
        # yield DGDecision,
        # yield IntroDQ,




        # if self.player.id_in_group == 1:
        #     yield Offer, dict(kept=cu(99))
        #     expect(self.player.payoff, cu(99))
        # else:
        #     expect(self.player.payoff, cu(1))
        # yield Results
