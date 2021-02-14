template <class E1, class E2>
class MinusBin: public Expression {
public:
    using value_type = typename std::common_type<typename E1::value_type, typename E2::value_type>::type;
private:
    const E1& _a;
    const E2& _b;
public:
    explicit MinusBin(const E1& a, const E2& b): _a(a), _b(b) {}
    value_type evaluate(int i) { return this -> _a.evaluate(i) - this -> _b.evaluate(i); }
    value_type evaluate(int i) const { return this -> _a.evaluate(i) - this -> _b.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "MinusBin(" << this -> _a << ", " << this -> _b << ")";
    }
};

template <class E1, class E2>
typename std::enable_if<std::is_base_of<Expression, E1>::value &&
                        std::is_base_of<Expression, E2>::value, MinusBin<E1, E2>>::type
operator-(const E1& a, const E2& b) {
    return MinusBin<E1, E2>(a, b);
}

template <class E1, class E2>
class Multiply: public Expression {
public:
    using value_type = typename std::common_type<typename E1::value_type, typename E2::value_type>::type;
private:
    const E1& _a;
    const E2& _b;
public:
    explicit Multiply(const E1& a, const E2& b): _a(a), _b(b) {}
    value_type evaluate(int i) { return this -> _a.evaluate(i) * this -> _b.evaluate(i); }
    value_type evaluate(int i) const { return this -> _a.evaluate(i) * this -> _b.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "Multiply(" << this -> _a << ", " << this -> _b << ")";
    }
};

template <class E1, class E2>
typename std::enable_if<std::is_base_of<Expression, E1>::value &&
                        std::is_base_of<Expression, E2>::value, Multiply<E1, E2>>::type
operator*(const E1& a, const E2& b) {
    return Multiply<E1, E2>(a, b);
}

template <class E1, class E2>
class Div: public Expression {
public:
    using value_type = typename std::common_type<typename E1::value_type, typename E2::value_type>::type;
private:
    const E1& _a;
    const E2& _b;
public:
    explicit Div(const E1& a, const E2& b): _a(a), _b(b) {}
    value_type evaluate(int i) { return this -> _a.evaluate(i) / this -> _b.evaluate(i); }
    value_type evaluate(int i) const { return this -> _a.evaluate(i) / this -> _b.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "Div(" << this -> _a << ", " << this -> _b << ")";
    }
};

template <class E1, class E2>
typename std::enable_if<std::is_base_of<Expression, E1>::value &&
                        std::is_base_of<Expression, E2>::value, Div<E1, E2>>::type
operator/(const E1& a, const E2& b) {
    return Div<E1, E2>(a, b);
}

template <class E1, class E2>
class Less: public Expression {
public:
    using value_type = bool;
private:
    const E1& _a;
    const E2& _b;
public:
    explicit Less(const E1& a, const E2& b): _a(a), _b(b) {}
    value_type evaluate(int i) { return this -> _a.evaluate(i) < this -> _b.evaluate(i); }
    value_type evaluate(int i) const { return this -> _a.evaluate(i) < this -> _b.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "Less(" << this -> _a << ", " << this -> _b << ")";
    }
};

template <class E1, class E2>
typename std::enable_if<std::is_base_of<Expression, E1>::value &&
                        std::is_base_of<Expression, E2>::value, Less<E1, E2>>::type
operator<(const E1& a, const E2& b) {
    return Less<E1, E2>(a, b);
}
