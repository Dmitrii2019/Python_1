# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.
import re
name = input('Ваше имя: ')
surname = input('Фамилия: ')
email = input('email: ')
pattern = '([A-Z][a-z]+)'
pattern_email = '([a-z_0-9]+@[a-z0-9]+\.(ru|org|org))'
print('Имя указаноне не верно') if re.match(pattern, name) == None else print('Имя указаноне  верно')
print('Фамилия указаноне не верно') if re.match(pattern, surname) == None else print('Фамилия указаноне  верно')
print('email указаноне не верно') if re.match(pattern, email) == None else print('email указаноне  верно')

# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

import re
pattern = '([.]+)'
print(re.findall(pattern, some_str))
