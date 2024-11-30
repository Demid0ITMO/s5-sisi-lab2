from pyswip import Prolog
import re

pl = Prolog()
pl.consult("db_from_lab_1.pl")

# РУСИФИКАЦИЯ
games = {
    'minecraft': 'майнкрафт',
    'fortnite': 'фортнайт',
    'pubg': 'пабг',
    'overwatch': 'овервотч',
    'dnd': 'днд',
    'skyrim': 'скайрим',
    'gta5': 'гта5',
    'zelda': 'зельда',
    'rocket_league': 'рокет лига',
    'among_us': 'амонг ас',
}

genres = {
    'экшн': 'action',
    'стратегия': 'strategy',
    'приключения': 'adventure',
    'ролевая': 'role_playing',
    'рпг': 'role_playing',
    'спортивная': 'sports',
}

platforms = {
    'пк': 'pc',
    'плэйстейшн': 'playstation',
    'иксбокс': 'xbox',
    'нинтендо': 'nintendo_switch',
}

ratings = {
    0: 'e',
    10: 'e10',
    13: 't',
    16: 'm',
    18: 'ao',
}


# СОСТАВЛЕНИЕ ПОДСТРОКИ ЗАПРОСА ДЛЯ ФИЛЬТРАЦИИ РЕЙТИНГОВ, КОТОРЫЕ ПОДХОДЯТ ПО ВОЗРАСТУ
def rating_query_filter(age):
    query_line = f'has_rating(X, {ratings[0]})'
    for r in ratings:
        if age < r:
            break
        if r != 0:
            query_line += f'; has_rating(X, {ratings[r]})'
    return query_line


# ПОИСК ИГР, ПОДХОДЯЩИХ ПО ЖАНРУ И ВОЗРАСТУ
def games_with_genre(args):
    genre = genres[args['input']]
    result = pl.query(f"has_genre(X, {genre}), ({rating_query_filter(args['age'])})")
    return [f"Игры в жанре {args['input']}", list(result)]


# ПОИСК ИГР, ПОДХОДЯЩИХ ПО ПЛАТФОРМЕ И ВОЗРАСТУ
def games_with_platform(args):
    platform = platforms[args['input']]
    result = pl.query(f"has_platform(X, {platform}), ({rating_query_filter(args['age'])})")
    return [f"Игры на платформе {args['input']}", list(result)]


# ОПИСАНИЕ ТИПОВ ДОСТУПНЫХ ЗАПРОСОВ (СДЕЛАНО ДЛЯ ВОЗМОЖНОСТИ РАСШИРЕНИЯ)
queries_types = [
    {
        'id': 0,
        'asked_arg': 'жанр',
        'string': r'я хочу поиграть в _ игру',
        'action': games_with_genre
    },
    {
        'id': 1,
        'asked_arg': 'платформа',
        'string': r'в какие игры я могу поиграть на _',
        'action': games_with_platform
    },
]


# ВЫВОД СООБЩЕНИЯ ПОМОЩИ
def help_message():
    allowed_queries = '\n'.join(list(map(
        lambda q_type: f"{q_type['string'].replace('_', '`' + q_type['asked_arg'] + '`').capitalize()}",
        queries_types
    )))
    message = f'''
Вы можете вводить запросы следующего формата:
{allowed_queries}    

Рекомендации будут выводиться с учетом вашего возраста

Также вы можете использовать следующие команды:
Стоп - для выхода из программы
Помощь - для отображения этого сообщения
    '''
    print(message)


# ПАРСИНГ СТРОКИ ВВОДА, ВОЗВРАЩАЕТ КОД КОММАНДЫ И АРГУМЕНТЫ
def parse_input(string):
    match string.lower():
        case 'стоп':
            return [0, {}]
        case 'помощь':
            return [1, {}]
        case _:
            for q_type in queries_types:
                matches = re.findall(q_type['string'].replace('_', '(.+)', 1), string.lower())
                if not matches:
                    continue
                return [2, {'type_id': q_type['id'], 'input': matches[0]}]
    return [-1, {}]


# ЗАПРОС ИЗ БАЗЫ ЗНАНИЙ
def ask_database(args):
    try:
        action = next((item for item in queries_types if item['id'] == args['type_id']), None)['action']
        [hint, response] = action(args)
        if len(response) == 0:
            raise Exception
        return f"{hint}: {', '.join(list(map(lambda x: games[x['X']], response)))}"
    except:
        return 'По вашему запросу ничего не найдено'


def main():
    print('Привет! Сколько тебе лет?')
    while True:
        try:
            value = int(input('> '))
            if value <= 0:
                raise Exception
            else:
                age = value
                break
        except:
            print('Введи целое положительное число :)')
    help_message()
    while True:
        inp = input('> ')
        code, args = parse_input(inp)
        args['age'] = age
        match code:
            case 0:
                exit(0)
            case 1:
                help_message()
            case 2:
                print(ask_database(args))
            case _:
                print('Не понял вас')


if __name__ == "__main__":
    main()
