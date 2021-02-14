#include <ostream>
#include <vector>

class Expression {};

template <class T>
class Vector;

template <class E>
Vector<typename E::value_type> evaluate(const E& expr) {
    using value_type = typename E::value_type;
    const auto n = expr.size();
    Vector<value_type> result(n);
    for (int i=0; i<n; ++i) {
        result(i) = expr.evaluate(i);
    }
    return result;
}

template <class T>
class Vector: public Expression {
public:
    using U = std::conditional_t<std::is_same_v<T, bool>, char, T>;
    using value_type = U;

private:
    std::vector<U> _data;

public:
    Vector(std::initializer_list<U> rhs): _data(rhs) {}
    explicit Vector(int n): _data(n) {}
    template <class E>
    Vector(const E& expr,
           typename std::enable_if<std::is_base_of<Expression, E>::value, E>::type* dummy=nullptr):
    Vector(::evaluate(expr)) {}

    Vector() = default;
    ~Vector() = default;
    Vector(Vector&& rhs) = default;
    Vector(const Vector& rhs) = default;
    Vector& operator=(Vector&& rhs) = default;
    Vector& operator=(const Vector& rhs) = default;

    U& operator()(int i) { return this -> _data[i]; }
    const U& operator()(int i) const { return this -> _data[i]; }
    bool operator==(const Vector &other) const {
        if (size() != other.size()) return false;
        for (int i=0; i < size(); ++i)
            if (evaluate(i) != other.evaluate(i)) return false;
        return true;
    }
    U evaluate(int i) { return this -> _data[i]; }
    U evaluate(int i) const { return this -> _data[i]; }
    int size() const { return this -> _data.size(); }
    void display(std::ostream& out) const {
        out << "Vector(";
        const auto n = size();
        if (n != 0) { out << this -> _data.front(); }
        for (int i=1; i<n; ++i) { out << ',' << this -> _data[i]; }
        out << ')';
    }
};

template <class E>
typename std::enable_if<std::is_base_of<Expression, E>::value, std::ostream&>::type
operator<<(std::ostream& out, const E& expr) {
    expr.display(out); return out;
}

#include "unary.hh"
#include "binary.hh"
#include "ternary.hh"
#include "all.hh"
