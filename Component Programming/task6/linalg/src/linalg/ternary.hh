template <class E1, class E2, class E3>
class Ternary: public Expression {
public:
    using value_type = typename std::common_type<typename E2::value_type, typename E3::value_type>::type;
private:
    const E1& _a;
    const E2& _b;
    const E3& _c;
public:
    explicit Ternary(const E1& a, const E2& b, const E3& c): _a(a), _b(b), _c(c) {}
    value_type evaluate(int i) { return _a.evaluate(i) ? _b.evaluate(i) : _c.evaluate(i); }
    value_type evaluate(int i) const { return _a.evaluate(i) ? _b.evaluate(i) : _c.evaluate(i); }
    int size() const { return _b.size(); }
    void display(std::ostream& out) const {
        out << "Ternary(" << this -> _a << ", " << this -> _b << ", " << this -> _c << ")";
    }
};

template <class E1, class E2, class E3>
auto where(const E1& a, const E2& b, const E3& c) {
    return Ternary<E1, E2, E3>(a, b, c);
}
