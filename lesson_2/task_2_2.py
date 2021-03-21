"""""""""
2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и 
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

Сформировать из обработанного списка строку:
в "05" часов "17" минут температура воздуха была "+05" градусов

Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для чисел 
со знаком?
3. *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place). Эта задача намного серьёзнее, 
чем может сначала показаться.
"""""""""

sentence_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# print(sentence_words)
sentence_words_with_quotes = []

for word in sentence_words:
    sentence_words_with_quotes.append(word)
    if word.isdigit() or '+' in word or '-' in word:
        if '+' in word:
            sentence_words_with_quotes[len(sentence_words_with_quotes) - 1] = word.zfill(3)
        else:
            sentence_words_with_quotes[len(sentence_words_with_quotes) - 1] = word.zfill(2)
        sentence_words_with_quotes.insert(len(sentence_words_with_quotes) - 1, '"')
        sentence_words_with_quotes.append('"')
# print(sentence_words_with_quotes)

#  НЕ ВЫШЛО ДОДУМАТЬСЯ :(
# sentence = ''.join([('' if '+' in elm or elm.isdigit() or '"' in elm else ' ') + elm for elm in
#                    sentence_words_with_quotes])

sentence = ' '.join(sentence_words_with_quotes)
for elm in '+-0123456789':
    sentence = sentence.replace('" ' + elm, '"' + elm)
sentence = sentence.replace(' " ', '" ')
print(f'С новым списком. {sentence}')

# реализация без нового списка, с изменением текущего
index_numbers = []

for index_word, word in enumerate(sentence_words):
    # new_list.append(word)
    if word.isdigit() or '+' in word:
        if '+' in word:
            sentence_words[index_word] = word.zfill(3)
            index_numbers.append(index_word)
        else:
            sentence_words[index_word] = word.zfill(2)
            index_numbers.append(index_word)
step_added_quote = 1
for index_number in index_numbers:
    if step_added_quote == 1:
        sentence_words.insert(index_number, 'g')
        sentence_words.insert(index_number + 2, 'g')
        step_added_quote += 1
    elif 1 < step_added_quote < 4:
        index_number += 2
        sentence_words.insert(index_number, 'g')
        sentence_words.insert(index_number + 2, 'g')
        step_added_quote += 2
    else:
        index_number += 4
        sentence_words.insert(index_number, 'g')
        sentence_words.insert(index_number + 2, 'g')

sentence = ' '.join(sentence_words_with_quotes)
for elm in '+-0123456789':
    sentence = sentence.replace('" ' + elm, '"' + elm)

sentence = sentence.replace(' " ', '" ')
print(f'Без нового списка. {sentence}')

# print(sentence_words[1:4])
# print(sentence_words[5:8])
# print(sentence_words[12:15])
