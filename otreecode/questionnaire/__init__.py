from otree.api import *
import random
import itertools
from django import forms

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    Q_GENDER = [
        [1, 'Мужской'],
        [2, 'Женский'],
    ]
    Q_EDUCATION = [
        [1, 'Начальное общее образование (4 класса)'],
        [2, 'Основное общее образование (9 классов)'],
        [3, 'Среднее (полное) общее образование (11 классов)'],
        [4, 'Среднее профессиональное образование (колледж/техникум)'],
        [5, 'Основное общее образование (9 классов)'],
        [6, 'Бакалавриат'],
        [7, 'Cпециалитет, магистратура'],
        [8, 'Аспирантура'],
        [9, 'Нет'],
    ]
    Q_MARRIAGE = [
        [1, 'Никогда не состоял(a)'],
        [2, 'В зарегистрированном браке'],
        [3, 'В незарегистрированном браке'],
        [4, 'Вдовец (вдова)'],
        [5, 'Разведен (разведена)']

    ]
    Q_INEQUALITY_PROBLEM = [
        [1, 'Не проблема вообще'],
        [2, 'Небольшая проблема'],
        [3, 'Проблема'],
        [4, 'Серьезная проблема'],
        [5, 'Очень серьезная проблема']
    ]
    Q_INCOME_INCREASING = [
        [1, 'Возросло'],
        [2, 'Не изменилось'],
        [3, 'Снизилось'],
    ]
    Q_4_YES_NO = [
        [1, 'Да'],
        [2, 'Скорее да'],
        [3, 'Скорее нет'],
        [4, 'Нет'],
    ]
    Q_4_IMPORTANT = [
        [1, 'Очень важно'],
        [2, 'Довольно важно'],
        [3, 'Не очень важно'],
        [4, 'Совсем неважно'],
    ]
    Q_TRUST = [
        [1, 'Почти всегда людям можно доверять'],
        [2, 'Обычно людям можно доверять'],
        [3, 'Обычно стоит быть осторожным в общении с людьми'],
        [4, 'Почти всегда нужно быть осторожным в общении с людьми'],
    ]
    Q_PARTY = [
        [1, 'Единая Россия'],
        [2, 'Коммунистическая партия Российской Федерации (КПРФ)'],
        [3, 'Справедливая Россия — За правду (СРЗП)'],
        [4, 'Либерально-демократическая партия России (ЛДПР)'],
        [5, 'Новые люди'],
        [6, 'Российская объединённая демократическая партия «Яблоко»'],
        [7, 'Другая зарегистрированная партия'],
        [8, 'Нет партии, которая могла бы представлять мои интересы'],
        [9, 'Я не интересуюсь политикой'],
    ]
    Q_PLACE_LIVING = [
        [1, 'Крупный город (население больше 1 миллиона человек)'],
        [2, 'Город с населением от 250 тысяч человек до миллиона'],
        [3, 'Небольшой город с населением до 250 тысяч человек'],
        [4, 'Город с населением от 50 до 250 тысяч человек'],
        [5, 'Населенный пункт до 50 тысяч человек'],
    ]
    Q_OCCUPATION = [
        [1, 'Государственная служба'],
        [2, 'Частный сектор'],
        [3, 'Собственный бизнес или самозанятость'],
        [4, 'Некоммерческий сектор'],
        [5, 'Студент'],
        [6, 'Безработный'],
        [7, 'Выбыл(а) из состава рабочей силы (выход на пенсию, отпуск по уходу за ребенком)'],
    ]
    Q_CHARITY = [
        [1, 'Нет'],
        [2, 'Да, жертвовал(а) деньги на благотворительность'],
        [3, 'Да, участвовал(а) в качестве волонтера'],
        [4, 'Да, жертвовал(а) деньги и участвовал(а) волонтером']
    ]
    Q_FINANCIAL_CONDITIONS = [
        [1, 'Денег не хватает даже на питание'],
        [2, 'На питание денег хватает, но не хватает на покупку одежды и обуви'],
        [3, 'На покупку одежды и обуви денег хватает, но не хватает на покупку мелкой бытовой техники'],
        [4, 'На покупку мелкой бытовой техники денег хватает, но не хватает на покупку крупной бытовой техники'],
        [5, 'Денег хватает на покупку крупной бытовой техники, но мы не сможем купить новую машину'],
        [6, 'На новую машину денег хватает, но мы не можем купить небольшую квартиру'],
        [7, 'На небольшую квартиру денег хватает, но мы не смогли бы купить большую квартиру в хорошем районе'],
        [8, 'Материальных затруднений не испытываем, при необходимости могли бы приобрести квартиру, дом'],
        [9, 'Затрудняюсь ответить'],
    ]
    Q_RELIGION = [
        [1, 'Католицизм'],
        [2, 'Протестантизм'],
        [3, 'Православие'],
        [4, 'Иудаизм'],
        [5, 'Ислам'],
        [6, 'Буддизм'],
        [7, 'Другую религию'],
        [8, 'Не исповедую никакой религии (атеист)']
    ]
    Q_BIG5 = [
        [1, 'Полностью согласен'],
        [2, 'Скорее согласен'],
        [3, 'Затрудняюсь ответить'],
        [4, 'Скорее не согласен'],
        [5, 'Полностью не согласен']
    ]
    Q_BENEFITS = [
        [1, 'Проигрываю'],
        [2, 'Безразлично'],
        [3, 'Выигрываю']
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


def high_position(label):
    return models.IntegerField(label=label, choices=C.Q_4_IMPORTANT, widget=widgets.RadioSelect)


def scale(label):
    return models.IntegerField(label=label, choices=range(1, 11), widget=widgets.RadioSelectHorizontal)


def big5(label):
    return models.IntegerField(label=label, choices=C.Q_BIG5, widget=widgets.RadioSelect)


class Player(BasePlayer):
    year_of_birth = models.IntegerField(
        label='В каком году Вы родились?',
        min=1900,
        max=2022
    )
    gender = models.StringField(
        label='Пожалуйста, укажите Ваш пол.',
        choices=C.Q_GENDER,
        widget=widgets.RadioSelectHorizontal
    )
    education = models.StringField(
        label='Укажите наивысшую оконченную ступень образования, по которой Вы имеете диплом.',
        choices=C.Q_EDUCATION,
        widget=widgets.RadioSelect
    )
    marriage = models.StringField(
        label='Вы состоите в браке?',
        choices=C.Q_MARRIAGE,
        widget=widgets.RadioSelect
    )
    children = models.IntegerField(
        label='Сколько у Вас детей?',
        min=0
    )
    children_live = models.IntegerField(
        label='Сколько из них проживает с Вами?',
        min=0
    )

    # q related to inequality
    inequality_problem = models.StringField(
        label='Как Вы думаете, неравенство — серьезная проблема в России?',
        choices=C.Q_INEQUALITY_PROBLEM,
        widget=widgets.RadioSelect
    )
    income_inequality_increasing = models.StringField(
        label='Как Вы считаете, неравенство доходов возросло или снизилось в последние годы в России?',
        choices=C.Q_INCOME_INCREASING,
        widget=widgets.RadioSelect
    )
    income_satisfactory = models.StringField(
        label='Довольны ли Вы своим заработком?',
        choices=C.Q_4_YES_NO,
        widget=widgets.RadioSelectHorizontal
    )
    income_deserving = models.StringField(
        label='Как Вы считаете, люди с высоким заработком заслуживают такой уровень дохода?',
        choices=C.Q_4_YES_NO,
        widget=widgets.RadioSelectHorizontal
    )
    income_comp_parents = models.StringField(
        label='По сравнению с уровнем жизни Ваших родителей, когда они были в Вашем возрасте, '
              'Вы живете сейчас лучше, хуже или примерно также?',
        choices=[
            [1, 'Лучше'],
            [2, 'Хуже'],
            [3, 'Примерно также'],
        ],
        widget=widgets.RadioSelectHorizontal
    )
    unemployment_100 = models.IntegerField(
        label='Как Вы думаете, сколько человек из каждых 100 людей на данный момент не имеет работы и ищет её?',
        min=0,
        max=100)

    high_position_family = high_position('родиться в обеспеченной семье?')
    high_position_education = high_position('получить хорошее образование?')
    high_position_work = high_position('упорно работать?')
    high_position_networking = high_position('знать нужных людей?')
    high_position_social_elevators = high_position('иметь в стране развитые социальные лифты?')

    # economic redistribution
    redistr_changes = models.StringField(
        label='Хотели бы Вы изменить систему перераспределения в России?',
        choices=[
            [1, 'Уменьшить перераспределение'],
            [2, 'Оставить без изменений'],
            [3, 'Увеличить перераспределение']
        ],
        widget=widgets.RadioSelect
    )
    redistr_benefits_now = models.StringField(
        label='В этом году',
        choices=C.Q_BENEFITS,
        widget=widgets.RadioSelect
    )
    redistr_benefits_life = models.StringField(
        label='В течение жизни',
        choices=C.Q_BENEFITS,
        widget=widgets.RadioSelect
    )
    redistr_tax_rate = models.StringField(
        label='Хотели бы вы изменить налоговую ставку в России?',
        choices=[
            [1, 'Уменьшить налоговую ставку'],
            [2, 'Оставить без изменений'],
            [3, 'Увеличить налоговую ставку']
        ],
        widget=widgets.RadioSelect
    )

    # political preferences
    general_trust = models.IntegerField(
        label='Могли бы Вы сказать, что в целом людям стоит доверять или нужно быть осторожным?',
        choices=C.Q_TRUST,
        widget=widgets.RadioSelect
    )
    trust_country = scale('Государству в целом')
    trust_political_parties = scale('Политическим партиям')
    trust_government = scale('Правительству')
    trust_courts = scale('Судам и судебной системе')
    trust_television = scale('Телевидение')
    trust_mass_media = scale('Новостные средства массовой информации')

    social_mobility = scale('Как Вы считаете, насколько хорошо работают социальные лифты в России?')
    politics_interest = scale('Можете ли Вы описать себя как человека, который интересуется политикой? ')

    effort_luck = scale('')
    responsibility = scale('')
    income_equality = scale('')
    competition = scale('')
    left_right = scale('')

    party_vote = models.StringField(
        label='За какую партию Вы голосовали на выборах в Государственную думу, если бы они состоялись сегодня?',
        choices=C.Q_PARTY,
        widget=widgets.RadioSelect
    )
    corruption = scale('В какую точку Вы поместили бы Россию на этой шкале?')

    democracy_redistribution = scale('Правительство берет налоги с богатых для поддержки бедных')
    democracy_elections = scale('Люди выбирают политических лидеров на свободных выборах')
    democracy_unemployment_allowance = scale('Безработные получают государственное пособие')
    democracy_income_equality = scale('Государство обеспечивает равенство доходов')
    democracy_order = scale('Люди подчиняются властям')
    democracy_gender_equality = scale('У мужчин и женщин равные права')

    important_democracy = scale('Насколько для Вас важно жить в демократической стране?')
    Russia_democracy = scale('Как Вы считаете, насколько демократично управляется Россия в настоящее время?')

    # background
    religion = models.StringField(
        label='Какую религию Вы исповедуете?',
        choices=C.Q_RELIGION,
        widget=widgets.RadioSelect
    )
    mother_education = models.StringField(
        label='Пожалуйста, укажите наивысшую оконченную ступень образования Вашей матери.',
        choices=C.Q_EDUCATION,
        widget=widgets.RadioSelect
    )
    father_education = models.StringField(
        label='Пожалуйста, укажите наивысшую оконченную ступень образования Вашего отца.',
        choices=C.Q_EDUCATION,
        widget=widgets.RadioSelect
    )
    place_living_now = models.StringField(
        label='Какая из указанных категорий лучше всего описывает место, где Вы сейчас проживаете?',
        choices=C.Q_PLACE_LIVING,
        widget=widgets.RadioSelect
    )
    place_living_sensible_years = models.StringField(
        label='Какая из указанных категорий лучше всего описывает место, где Вы проживали в возрасте 16-20 лет?',
        choices=C.Q_PLACE_LIVING,
        widget=widgets.RadioSelect
    )
    occupation = models.StringField(
        label='Пожалуйста, укажите сферу Вашей деятельности.',
        choices=C.Q_OCCUPATION,
        widget=widgets.RadioSelect
    )
    charity = models.StringField(
        label='Жертвовали ли Вы за последний год деньги на благотворительность '
              'или участвовали волонтером в некоммерческих организациях?',
        choices=C.Q_CHARITY,
        widget=widgets.RadioSelect
    )
    financial_conditions = models.StringField(
        label='Пожалуйста, выберите утверждение, которое наиболее точно описывает Ваше финансовое положение.',
        choices=C.Q_FINANCIAL_CONDITIONS,
        widget=widgets.RadioSelect
    )
    # big5
    big5_1 = big5(label='сдержанный человек')
    big5_2 = big5(label='в целом доверчивый человек')
    big5_3 = big5(label='склонны к лени')
    big5_4 = big5(label='расслаблены и способны справляться со стрессом')
    big5_5 = big5(label='имеете немного интересов')
    big5_6 = big5(label='общительны')
    big5_7 = big5(label='склонны выискивать чужие ошибки')
    big5_8 = big5(label='тщательно выполняете работу')
    big5_9 = big5(label='легко нервничаете')
    big5_10 = big5(label='имеете богатое воображение')

    big5_extraversion = models.FloatField()
    big5_agreeableness = models.FloatField()
    big5_conscientiousness = models.FloatField()
    big5_neuroticism = models.FloatField()
    big5_openness = models.FloatField()

    # just
    just_allowance = scale('Получение государственных пособий, на которые человек не имеет права ')
    just_freeride = scale('Проезд без оплаты в общественном транспорте')
    just_thieving = scale('Кража чужой собственности')
    just_tax_evasion = scale('Неуплата налогов, если есть такая возможность')
    just_bribe = scale('Получение взятки, используя служебное положение')
    just_violence = scale('Насилие против других людей ')
    just_political_violence = scale('Использование насилия в политической борьбе ')

    # personal
    freedom_choice = scale('')
    life_satisfaction = scale('')
    finance_satisfaction = scale('')


def children_live_max(player):
    return player.children


def big5_calculation(first, second):
    return 3 + (first - second) / 2


# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['year_of_birth',
                   'gender',
                   'education',
                   'marriage',
                   'children',
                   'children_live'
                   ]


class InequalityAssessment(Page):
    form_model = 'player'
    form_fields = ['inequality_problem',
                   'income_inequality_increasing',
                   'income_satisfactory',
                   'income_deserving',
                   'income_comp_parents',
                   'unemployment_100',

                   'high_position_family',
                   'high_position_education',
                   'high_position_work',
                   'high_position_networking',
                   'high_position_social_elevators',
                   ]


class Redistribution(Page):
    form_model = 'player'
    form_fields = [
        'redistr_changes',
        'redistr_benefits_now',
        'redistr_benefits_life',
        'redistr_tax_rate'
    ]


class PoliticalPreferences(Page):
    form_model = 'player'
    form_fields = [
        'general_trust',
        'trust_country',
        'trust_political_parties',
        'trust_government',
        'trust_courts',
        'trust_television',
        'trust_mass_media',

        'social_mobility',
        'politics_interest',

        'effort_luck',
        'responsibility',
        'income_equality',
        'competition',
        'left_right',
        'party_vote',
        'corruption',

        'democracy_redistribution',
        'democracy_elections',
        'democracy_unemployment_allowance',
        'democracy_income_equality',
        'democracy_order',
        'democracy_gender_equality',

        'important_democracy',
        'Russia_democracy',
    ]


class Big5(Page):
    form_model = 'player'
    form_fields = ['big5_1',
                   'big5_2',
                   'big5_3',
                   'big5_4',
                   'big5_5',
                   'big5_6',
                   'big5_7',
                   'big5_8',
                   'big5_9',
                   'big5_10',

                   'just_allowance',
                   'just_freeride',
                   'just_thieving',
                   'just_tax_evasion',
                   'just_bribe',
                   'just_violence',
                   'just_political_violence',
                   'freedom_choice',
                   'life_satisfaction',
                   'finance_satisfaction'
                   ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.big5_extraversion = big5_calculation(player.big5_6, player.big5_1)
        player.big5_agreeableness = big5_calculation(player.big5_2, player.big5_7)
        player.big5_conscientiousness = big5_calculation(player.big5_8, player.big5_3)
        player.big5_neuroticism = big5_calculation(player.big5_9, player.big5_4)
        player.big5_openness = big5_calculation(player.big5_10, player.big5_5)


class Risk(Page):
    pass


class BackgroundInfo(Page):
    form_model = 'player'
    form_fields = [
        'religion',
        'mother_education',
        'father_education',
        'place_living_now',
        'place_living_sensible_years',
        'occupation',
        'charity',
        'financial_conditions',
    ]


class LastQ(Page):
    pass


page_sequence = [
    # Intro,
    Demographics,
    InequalityAssessment,
    Redistribution,
    PoliticalPreferences,
    Big5,
    # Risk,
    BackgroundInfo,
    LastQ
]
