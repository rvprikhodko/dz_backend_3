# Домашнее задание №3

## Задача №1

### Условие
Реализуйте функцию, которая переводит число из десятичной системы счисления
в двоичную. Встроенные методы языка программирования использовать
нельзя!

### Решение
Задача решалась при помощи реализации метода сокращенного деления с остатком.
На каждой итерации цикла while присваиваем остаток от деления на 2 к двоичному числу и делим изначальное число на 2.
После выполнения цикла, возвращаем перевернутую строку при помощи среза [::-1], либо, если изначальное число равнялось нулю, 0,
так как цикл не может начать работу при изначальном числе, равном нулю.

## Задача №2

### Условие
Определите, является ли строка палиндромом. Учитываются только буквы и
цифры, заглавные и строчные буквы считаются одинаковыми.Буквы могут быть
только латинские. Фраза может состоять из строчных и прописных латинских букв,
цифр, знаков препинания.
Функция возвращает True, если фраза является палиндромом, иначе - False

### Решение
Задача решалась при помощи создания новой строки, которая состоит только из строчных английских букв (где заглавные преобразованы в строчные).
Для этого использовался цикл for, где каждый символ проверялся на принадлежность к латинскому алфавиту при помощи метода isalpha() и, если символ
являлся буквой латинского алфавита, то он присваивался к новой строке в строчном варианте при помощи метода islower().
Далее новая строка сравнивалась со своей перевернутой версией при помощи среза [::-1].

# Python 3.10
