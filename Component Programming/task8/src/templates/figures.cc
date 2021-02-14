#include "figures.hh"
#include <numbers>

template <class T>
Circle<T>::Circle(T radius): r(radius) {}

template <class T>
T Circle<T>::area() const {
    return std::numbers::pi * r * r;
}

template <class T>
T Circle<T>::radius() const {
    return r;
}

template <class T>
Rectangle<T>::Rectangle(T a_, T b_):
    a(a_),
    b(b_)
{}

template <class T>
T Rectangle<T>::area() const {
    return a * b;
}

template <class T>
T Rectangle<T>::a_() const {
    return a;
}

template <class T>
T Rectangle<T>::b_() const {
    return b;
}

template class Circle<float>;
template class Circle<double>;
template class Rectangle<float>;
template class Rectangle<double>;
