# задача-1
a = 50
b = 20
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

text = input('Видите текст: ')
print(text)

# задача-2
number = int(input('Видите число: '))
print(number + 2)

# задача-3
age = int(input('Сколько вам лет? '))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')

# normal
number = int(input('Видите число: '))
while number <= 0 or number >= 10:
    print('Попробуйте еще раз ')
    number = int(input('Видите число от 0 до 10: '))
print(number ** 2)

# Задача-2:
a = input('Ведите значение 1: ')
b = input('Ведите значение 2: ')
(b, a) = (a, b)
print(a, b)

#hard
print('Медицинская анкета')
name = input('Ваше имя: ')
surname = input('Ваша фамилия: ')
age = int(input('Ваш возраст: '))
weight = int(input('Ваш вес: '))
if age < 30 and weight >= 50 and weight < 120: #если ему до 30 лет и вес от 50 и до 120 кг,
    print('Вы в хорошем состоянии')
elif (age > 30 and age < 40) and (weight < 50 or weight > 120):  #если ему более 30 и вес меньше 50 или больше 120 кг
    print('Вам требуется начать вести правильный образ жизни Правильно')
elif age > 40 and (weight < 50 or weight > 120):  #если ему более 40 и вес менее 50 или больше 120 кг
    print('Вам требуется врачебный осмотр')
else:
    print('У Вас не стандартная ситуация')
print('Прием окончен')





