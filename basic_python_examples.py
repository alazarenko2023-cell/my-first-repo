# ===== Основні типи даних =====
a = "змінна з текстом"
b = 1
b1 = 1.1
c = ["a", 1, 1.25, "Слово", a]  # list
d = {"a": "Слово", "b": 1, a: b}  # dict
e = ("a", a)  # tuple
f = {"ss", a + str(b)}  # set

print("String:", a)
print("Integer:", b)
print("Float:", b1)
print("List:", c)
print("Dict:", d)
print("Tuple:", e)
print("Set:", f)

print("\n===== Вбудовані константи =====")
print("True:", True)
print("False:", False)
print("None:", None)

print("\n===== Зарезервовані слова Python =====")
import sys
help("keywords")

print("\n===== Вбудовані функції =====")
print("abs(-12.5) =", abs(-12.5))
print("len(c) =", len(c))
print("type(a) =", type(a))

print("\n===== Цикли =====")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
else:
    print("Цикл завершено")

print("\n===== Розгалуження =====")
from random import randint
A = randint(0, 1)
if A:
    print(f"A = {A}")
else:
    print(f"Але може бути що A = {A}")

print("\n===== try / except / finally =====")
A = 0
try:
    print(10 / A)
except Exception as e:
    print("Помилка:", e)
finally:
    print("Блок finally виконався")

print("\n===== Контекст-менеджер with =====")
with open("README.md", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"{i}) {line.strip()}")

print("\n===== Lambda =====")
def a_b_func(a, b):
    return a, b

this_is_lambda = lambda name, age: f"Цей код написав: {name}, мені {age} років"

print(this_is_lambda("Анастасія", 17))
print(this_is_lambda(*a_b_func("Анастасія", 17)))
