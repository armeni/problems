template <class E>
class All: public Expression {
public:
    using value_type = bool;
private:
    const E& _a;
public:
    explicit All(const E& a): _a(a) {}
    value_type evaluate(int i) {
        return _a.evaluate(i);
    }
    value_type evaluate(int i) const {
        return _a.evaluate(i);
    }
    int size() const { return _a.size(); }
    void display(std::ostream& out) const {
        out << "All(" << this -> _a << ")";
    }
};

template <class E>
bool evaluate(const All<E>& b) {
    for (int i = 0; i < b.size(); ++i)
        if (!b.evaluate(i))
		return false;
    return true;
}

template <class E>
All<E> all(const E& a) {
    return All<E>(a);
}
