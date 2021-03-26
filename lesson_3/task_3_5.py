"""""""""
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков 
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Например:
get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]

Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках 
(когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?
"""""""""""
from random import choice

NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count_joke=2):
    """
    Generating a given number of jokes from random word lists, possible repeats words
    :param count_joke: numbers of needed jokes
    :return: entered number of jokes
    """
    jokes = []
    while count_joke != 0:
        words = [choice(NOUNS), choice(ADVERBS), choice(ADJECTIVES)]
        joke = ' '.join(words)
        if words not in jokes:
            jokes.append(f"\"{joke}\"")
            count_joke -= 1
    return jokes


def get_jokes_choose_repeat(count_joke=2, flag_repeat=True):
    """
    Generating a given number of jokes from random word lists with or without repeats words
    :param count_joke: needed count jokes
    :param flag_repeat: possibility of repeating words
    :return: entered number of jokes with or without repeating the words
    """
    words = []
    jokes = []
    if flag_repeat:
        while count_joke != 0:
            noun = choice(NOUNS)
            adverb = choice(ADVERBS)
            adjective = choice(ADJECTIVES)
            if noun not in words and adverb not in words and adjective not in words:
                words.append(noun)
                words.append(adverb)
                words.append(adjective)
                count_joke -= 1
                continue
        index_start = 0
        index_stop = 3
        while index_stop <= len(words):
            joke = ' '.join(words[index_start:index_stop])
            jokes.append(joke)
            index_start += 3
            index_stop += 3
    else:
        jokes = get_jokes(count_joke)
    return jokes


print(get_jokes(count_joke=3))
print(get_jokes_choose_repeat(count_joke=4, flag_repeat=True))
