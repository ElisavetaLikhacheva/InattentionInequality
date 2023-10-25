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
        [3, '3 — На покупку одежды и обуви денег хватает, но не хватает на покупку бытовой техники (холодильник, телевизор, компьютер)'],
        [4, '4 — На покупку бытовой техники денег хватает, но не хватает на покупку автомобиля'],
        [5, '5 — На автомобиль денег хватает, но не хватает на покупку недвижимого имущества'],
        [6, '6 — Материальных затруднений не испытываем, есть возможность приобрести любое движимое и недвижимое имущество'],
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
        #initial=1999,
        # blank=True
    )
    gender = models.StringField(
        label='Пожалуйста, укажите Ваш пол.',
        choices=C.Q_GENDER,
        widget=widgets.RadioSelectHorizontal,
        #initial=1,
        # blank=True
    )
    financial_conditions = models.IntegerField(
        label='Пожалуйста, выберите вариант ответа, который наиболее точно описывает финансовое положение Вашей семьи, не залезая в долги и не беря кредитов.',
        choices=C.Q_FINANCIAL_CONDITIONS,
        widget=widgets.RadioSelect,
        #initial=1,
    )

    num_failed_attempts = models.IntegerField(initial=0)
    failed_too_many = models.BooleanField(initial=False)

    quiz1 = models.IntegerField(label='Предположим, участник А решил оставить 50 очков себе. '
                                      'Сколько очков будет передано участнику Б?')
    quiz2 = models.BooleanField(label='Может ли участник Б выбрать передать очки участнику А?')
    quiz3 = models.IntegerField(label='Сколько очков участник А может распределить между собой и участником Б?')

    prior_1 = models.PositiveIntegerField(label='1 — Денег не хватает даже на питание')
    prior_2 = models.PositiveIntegerField(label='2 — На питание денег хватает, но не хватает на покупку одежды и обуви')
    prior_3 = models.PositiveIntegerField(label='3 — На покупку одежды и обуви денег хватает, но не хватает на покупку бытовой техники (холодильник, телевизор, компьютер)')
    prior_4 = models.PositiveIntegerField(label='4 — На покупку бытовой техники денег хватает, но не хватает на покупку автомобиля')
    prior_5 = models.PositiveIntegerField(label='5 — На автомобиль денег хватает, но не хватает на покупку недвижимого имущества')
    prior_6 = models.PositiveIntegerField(label='6 — Материальных затруднений не испытываем, есть возможность приобрести любое движимое и недвижимое имущество')


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
        participant.num_financial_conditions = player.financial_conditions


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
        solutions = dict(quiz1=100, quiz2=False, quiz3=150)

        errors = {name: 'Неверный ответ' for name in solutions if values[name] != solutions[name]}
        if errors:
            player.num_failed_attempts += 1
            return errors


# class PriorBeliefs(Page):
#     form_model = 'player'
#     form_fields = [
#         'prior_1',
#         'prior_2',
#         'prior_3',
#         'prior_4',
#         'prior_5',
#         'prior_6',
#     ]
#
#     @staticmethod
#     def error_message(player: Player, values):
#         # since 'values' is a dict, you could also do sum(values.values())
#         if values['prior_1'] + values['prior_2'] + values['prior_3'] + values['prior_4'] + values['prior_5'] + values['prior_6'] != 100:
#             return 'Числа должны в сумме давать 100'


page_sequence = [
    InstructionGeneral,
    IntroQ,
    InstructionDG,
    UnderstandingDG,
    #PriorBeliefs,
]
