# from otree.api import *
import random
# import itertools
from otree.api import Currency as c, currency_range, expect, Bot
from . import *


class PlayerBot(Bot):
    def play_round(self):
        # yield Intro, dict(income=random.randint(1, 150))
        if self.player.role == C.DICTATOR_ROLE and 6 > self.player.group.treatment > 2:
                yield Detection, dict(check_info=random.choice([True, False]))
        elif self.player.role == C.DICTATOR_ROLE and self.player.group.treatment == 6:
            yield DetectionAvoid, dict(avoid_info=random.choice([True, False]))

        if self.player.role == C.DICTATOR_ROLE:
            yield MainDictatorDecision, dict(share=random.randint(0, 100))


        yield Demographics, dict(education=random.randint(1, 9),
                                 marriage=random.randint(1, 5),
                                 children=random.randint(0, 8),
                                 children_live=random.randint(0, 8)
                                 )
        yield InequalityAssessment, dict(inequality_problem=random.randint(1, 5),
                                         income_inequality_increasing=random.randint(1, 3),
                                         income_satisfactory=random.randint(1, 4),
                                         income_deserving=random.randint(1, 4),
                                         income_comp_parents=random.randint(1, 3),
                                         unemployment_100=random.randint(0, 100),

                                         high_position_family=random.randint(1, 4),
                                         high_position_education=random.randint(1, 4),
                                         high_position_work=random.randint(1, 4),
                                         high_position_networking=random.randint(1, 4),
                                         high_position_social_elevators=random.randint(1, 4),
                                         )
        yield Perception, dict(russian_pyramid=random.choice([1, 2, 3, 4, 5]),
                               ideal_pyramid=random.choice([1, 2, 3, 4, 5]),
                               median_income=random.randint(0, 100),
                               poor_10=random.randint(0, 100),
                               rich_10=random.randint(0, 100),
                               percent_below=random.randint(0, 100),
                               income=random.randint(0, 120)
                               )
        yield Redistribution, dict(redistr_changes=random.randint(1, 3),
                                   redistr_benefits_now=random.randint(1, 3),
                                   redistr_benefits_life=random.randint(1, 3),
                                   redistr_tax_rate=random.randint(1, 3),
                                   )
        yield PoliticalPreferences, dict(general_trust=random.randint(1, 4),
                                         trust_country=random.randint(1, 10),
                                         trust_political_parties=random.randint(1, 10),
                                         trust_government=random.randint(1, 10),
                                         trust_courts=random.randint(1, 10),
                                         trust_television=random.randint(1, 10),
                                         trust_mass_media=random.randint(1, 10),
                                         social_mobility=random.randint(1, 10),
                                         politics_interest=random.randint(1, 10),

                                         effort_luck=random.randint(1, 10),
                                         responsibility=random.randint(1, 10),
                                         income_equality=random.randint(1, 10),
                                         competition=random.randint(1, 10),
                                         left_right=random.randint(1, 10),
                                         party_vote=random.randint(1, 9),
                                         corruption=random.randint(1, 10),

                                         democracy_redistribution=random.randint(1, 10),
                                         democracy_elections=random.randint(1, 10),
                                         democracy_unemployment_allowance=random.randint(1, 10),
                                         democracy_income_equality=random.randint(1, 10),
                                         democracy_order=random.randint(1, 10),
                                         democracy_gender_equality=random.randint(1, 10),

                                         important_democracy=random.randint(1, 10),
                                         Russia_democracy=random.randint(1, 10),
                                         )
        yield Big5, dict(
            big5_1=random.randint(1, 5),
            big5_2=random.randint(1, 5),
            big5_3=random.randint(1, 5),
            big5_4=random.randint(1, 5),
            big5_5=random.randint(1, 5),
            big5_6=random.randint(1, 5),
            big5_7=random.randint(1, 5),
            big5_8=random.randint(1, 5),
            big5_9=random.randint(1, 5),
            big5_10=random.randint(1, 5),

            just_allowance=random.randint(1, 10),
            just_freeride=random.randint(1, 10),
            just_thieving=random.randint(1, 10),
            just_tax_evasion=random.randint(1, 10),
            just_bribe=random.randint(1, 10),
            just_violence=random.randint(1, 10),
            just_political_violence=random.randint(1, 10),
            freedom_choice=random.randint(1, 10),
            life_satisfaction=random.randint(1, 10),
            finance_satisfaction=random.randint(1, 10)
        )
        yield BackgroundInfo, dict(religion=random.randint(1, 8),
                                   mother_education=random.randint(1, 9),
                                   father_education=random.randint(1, 9),
                                   place_living_now=random.randint(1, 5),
                                   place_living_sensible_years=random.randint(1, 5),
                                   occupation=random.randint(1, 7),
                                   charity=random.randint(1, 4)
                                   )
        # yield LastQ,
        yield DGDecision,
        yield Submission(TheEnd, check_html=False)




        # if self.player.id_in_group == 1:
        #     yield Offer, dict(kept=cu(99))
        #     expect(self.player.payoff, cu(99))
        # else:
        #     expect(self.player.payoff, cu(1))
        # yield Results
