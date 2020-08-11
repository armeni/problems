Методичка: http://www.apmath.spbu.ru/ru/structure/depts/is/task6-2013.pdf

Во вложении тесты для ваших решений задачи аппроксимации.

* `test_approximation.py`:
    * `test_polynomial()` - тест полиномиальной аппроксимации.
    * `test_harmonic()` - тест гармонической аппроксимации.

* `approximation.py` содержит классы методов аппроксимации.
Нужно переписать методы `__init__()` (инициализация) и  `__call__()` (вызов)
без использования встроенных методов аппроксимации NumPy/SciPy:
    * `Approximation()` - базовый класс (ничего не меняем).
    * `Algebraic()` - аппроксимация семейством алгебраических полиномов.
    * `Legendre()` - аппроксимация семейством полиномов Лежандра.
    * `Harmonic()` - аппроксимация рядом Фурье (см. ссылку в докстринге).