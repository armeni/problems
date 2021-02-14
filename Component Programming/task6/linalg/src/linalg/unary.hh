template <class E>
class MinusUnary: public Expression {
public:
    using value_type = typename E::value_type;
private:
    const E& _a;
public:
    explicit MinusUnary(const E& a): _a(a) {}
    value_type evaluate(int i) { return -this -> _a.evaluate(i); }
    value_type evaluate(int i) const { return -this -> _a.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "MinusUnary(" << this -> _a << ")";
    }
};

template <class E>
typename std::enable_if<std::is_base_of<Expression, E>::value, MinusUnary<E>>::type
operator-(const E& a) {
    return MinusUnary<E>(a);
}

template <class E>
class PlusUnary: public Expression {
public:
    using value_type = typename E::value_type;
private:
    const E& _a;
public:
    explicit PlusUnary(const E& a): _a(a) {}
    value_type evaluate(int i) { return this -> _a.evaluate(i); }
    value_type evaluate(int i) const { return this -> _a.evaluate(i); }
    int size() const { return this -> _a.size(); }
    void display(std::ostream& out) const {
        out << "PlusUnary(" << this -> _a << ")";
    }
};

template <class E>
typename std::enable_if<std::is_base_of<Expression, E>::value, PlusUnary<E>>::type
operator+(const E& a) {
    return PlusUnary<E>(a);
}
