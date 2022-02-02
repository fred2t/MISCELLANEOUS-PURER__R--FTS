#include <iostream>
#include <bits/stdc++.h>

template <typename T>
T bigger(T n1, T n2) {
    return (n1 > n2) ? n1 : n2;
}

template <class T>
class Calculator {
    T num1;
    T num2;
    
    public:
    Calculator(T n1, T n2) {
        num1 = n1;
        num2 = n2;
    }

    void show() {
        std::cout << "add: " << num1 + num2 << '\n';
        std::cout << "sub: " << num1 - num2 << '\n';
        std::cout << "mul: " << num1 * num2 << '\n';
        std::cout << "div: " << num1 / num2 << '\n';
    }
};

int main() {
    std::cout << bigger(2, 9) << " bigger" << '\n';

    Calculator<int> exp(4, 8);
    exp.show();

    Calculator<float> exp2(2.4, 6.9);
    exp2.show();
}
