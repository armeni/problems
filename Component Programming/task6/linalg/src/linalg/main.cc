#include <iostream>
#include <linalg/linalg.hh>

int main(int argc, char* argv[]) {
    using T = float;
    Vector<T> a{1, 2, 3}, b{4, 5, 6};
    Vector<T> d(a * b);
    std::cout << (a * b) << std::endl;
    std::cout << evaluate(a * b) << std::endl;
    std::cout << d << std::endl;
    return 0;
}
