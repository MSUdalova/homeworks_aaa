# Guido van Rossum <guido@python.org>
import random


def step2_umbrella():
    num_umbrella = random.randint(0, 2)
    steps_umbrella = [
        'Она взяла зонтик и пошла.'
        'Утка заметила, что в небе нет самолета, который мог бы ей помочь.\n'
        'И она решила сама открыть свой зонтик!\n'
        'Она открыла зонтик, это был один из многих прекрасных зонтиков,\n'
        'но потом она его захлопнула,потому что она устала,\n'
        'и она была уставшей.\n',
        'И пару банок краски!',
        'С ним она будет выглядеть старше и серьезнее.'
    ]

    return print(steps_umbrella[num_umbrella])


def step2_no_umbrella():
    num_no_umbrella = random.randint(0, 2)
    steps_no_umbrella = [
        'Может быть, стоит сходить за ней?\n'
        'Но она не пришла...\n'
        'Да и к лучшему.\n'
        'Я бы потом не знал, где ее искать.\n'
        'Мне нравится, что вы больны не мной,\n'
        ' Мне нравится, что я больна не вами, \n'
        'Что никогда тяжелый шар земной\n'
        ' Не уплывет под нашими ногами.\n'
        'Что никогда во мрак ночной\n'
        'Мне нравится что вы больные не мной.\n',
        'Не надо.\n'
        'Дождь будет.\n'
        'И она ушла.\n'
        'Она шла по улице, думая о жизни и о том, что скоро лето.\n'
        '"Это последний шанс" - говорила она себе.\n'
        'На ней было черное платье.\n'
        'Оно было коротким и обтягивающими и под ним, казалось, ничего нет.\n'
        'Утка пошла дальше.\n'
        'Вокруг было много красивых платьев.\n'
        'Но она не знала, какое выбрать, потому что знала точно,\n'
        'чего она хочет.\n'
        'Так она пришла к этому бару.\n'
        'Ее как обычно встретили с улыбкой на лице и предложили столик.',
        'Взять ей пистолет?\n'
        '- Тоже нет.'
    ]

    return print(steps_no_umbrella[num_no_umbrella])


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
