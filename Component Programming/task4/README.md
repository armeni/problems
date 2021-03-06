# Клаcc вектор

При выполнении заданий должны быть соблюдены следующие условия.
- Сборка кода должна быть сделана с помощью Meson.
- Тесты должны быть прописаны в Meson и запускаться с помощью meson test.
- Все нижеперечисленные задания должны быть в одном проекте Meson.
- Структура проекта Meson должна быть похожа на следующую.
```
src
└── myproject # название произвольное
├── vector.hh # основной код
├── vector_test.cc # код модульных тестов
└── ...
```
Код тестов в отдельном файле. Все файлы находятся в директории с названием проекта.
- Включение заголовочных файлов в код всегда делается с указанием имени проекта: ``#include <myproject/vector.hh>``

1. Создайте упрощенный класс Vector по образу и подобию std::vector. Класс должен иметь следующие методы и конструкторы.
- push_back(const T&),
- push_back(T&&),
- pop_back, erase,
- begin, end, size,
- swap (а также функцию swap вне класса для совместимости с STL алгоритмами),
- Vector(const Vector&),
- Vector(Vector&&),
- Vector& operator=(const Vector&),
- Vector& operator=(Vector&&).
Класс должен быть шаблоном, единственный аргумент которого является типом элемента контейнера. Класс не должен использовать другие контейнеры STL (использовать std::unique_ptr можно). Оператор присваивания и конструкторы должны быть реализованы с помощью метода swap.

2. Проверьте корректность работы класса Vector, заменив в модульных тестах std::vector из предыдущего задания на него. Для этого скопируйте код модульных тестов в отдельный файл, чтобы код предыдущих заданий не изменился.

3. Проверьте, что в вашем классе отсутствуют ошибки работы с памятью. Для этого соберите проект с флагом ``-Db_sanitize=address`` и запустите тесты:
```meson
meson configure -Db_sanitize=address
ninja test
meson configure -Db_sanitize=none # отключение санитайзера
```
