from otree.api import *
import random
import itertools

doc = """
Your app description
"""

class C(BaseConstants):
    NAME_IN_URL = 'IntroQ'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    # DICTATOR_ROLE = 'A'
    # RECIPIENT_ROLE = 'Б'

    Q_GENDER = [
        [1, 'Мужской'],
        [2, 'Женский'],
    ]

    Q_FINANCIAL_CONDITIONS = [
        [1, '1 — Денег не хватает даже на питание'],
        [2, '2 — На питание денег хватает, но не хватает на покупку одежды и обуви'],
        [3, '3 — На покупку одежды и обуви денег хватает, но не хватает на покупку мелкой бытовой техники'],
        [4, '4 — На покупку мелкой бытовой техники денег хватает, но не хватает на покупку крупной бытовой техники'],
        [5, '5 — Денег хватает на покупку крупной бытовой техники, но не хватает на новую машину'],
        [6, '6 — На новую машину денег хватает, но не хватает на небольшую квартиру'],
        [7, '7 — На небольшую квартиру денег хватает, но не хватает на большую квартиру в хорошем районе'],
        [8, '8 — Материальных затруднений не испытываем, при необходимости есть возможность приобрести квартиру, дом'],
        # [9, 'Затрудняюсь ответить'],
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    year_of_birth = models.IntegerField(
        label='В каком году Вы родились?',
        min=1900,
        max=2022,
        # blank=True
    )
    gender = models.StringField(
        label='Пожалуйста, укажите Ваш пол.',
        choices=C.Q_GENDER,
        widget=widgets.RadioSelectHorizontal,
        # blank=True
    )
    financial_conditions = models.IntegerField(
        label='Пожалуйста, выберите вариант ответа, который наиболее точно описывает финансовое положение Вашей семьи.',
        choices=C.Q_FINANCIAL_CONDITIONS,
        widget=widgets.RadioSelect
    )

    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)

    quiz1 = models.IntegerField(label='Предположим, игрок А решил оставить 10 очков себе. '
                                      'Сколько очков будет передано игроку Б?')
    quiz2 = models.BooleanField(label='Может ли игрок Б выбрать передать очки игроку А?')
    quiz3 = models.IntegerField(label='Сколько очков игрок А может распределить между собой и игроком Б?')


# FUNCTIONS
# def other_player(player: Player):
#     return player.get_others_in_group()[0]


# def creating_session(subsession):
#     subsession.group_randomly(fixed_id_in_group=True)


# PAGES
class IntroQ(Page):
    form_model = 'player'
    form_fields = ['year_of_birth',
                   'gender',
                   'financial_conditions',
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.financial_conditions = player.field_display('financial_conditions')


class InstructionGeneral(Page):
    pass


class InstructionDG(Page):
    pass


class UnderstandingDG(Page):
    form_model = 'player'
    form_fields = [
        'quiz1',
        'quiz2',
        'quiz3'
    ]

    @staticmethod
    def error_message(player: Player, values):
        solutions = dict(quiz1=90, quiz2=False, quiz3=100)

        errors = {name: 'Неверный ответ' for name in solutions if values[name] != solutions[name]}
        if errors:
            player.num_failed_attempts += 1
            return errors


page_sequence = [
    InstructionGeneral,
    IntroQ,
    InstructionDG,
    UnderstandingDG,
]
