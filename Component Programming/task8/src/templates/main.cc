#include <iostream>
#include <figures.hh>

using namespace std;

int main() {
    Circle<float> float_circle(1.0f);
    Circle<double> double_circle(2.0);

    Rectangle<float> float_rect(1.0f, 2.0f);
    Rectangle<double> double_rect(3.0, 4.0);

    cout << float_circle.area() << endl;
    cout << double_circle.area() << endl;
    cout << float_rect.area() << endl;
    cout << double_rect.area() << endl;
    return 0;
}
