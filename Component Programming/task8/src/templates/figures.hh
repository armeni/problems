template <class T>
class Circle {
    public:
        Circle(T radius);
        T area() const;
        T radius() const;
    private:
        T r;
};

template <class T>
class Rectangle {
    public:
        Rectangle(T a_, T b_);
        T area() const;
        T a_() const;
        T b_() const;
    private:
        T a;
        T b;
};
