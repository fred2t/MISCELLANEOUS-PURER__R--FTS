#include <iostream>

class Complex {
public:
    int real;
    int imag;

    Complex() : real(0), imag(0) {}

    void input() {
        std::cout << "real then imag: ";
        std::cin >> real >> imag;
    }

    Complex operator + (Complex& exp) {
        Complex temp;
        temp.real = real + exp.real;
        temp.imag = imag + exp.imag;

        return temp;
    }

    void print() {
        if (imag < 0) { std::cout << real << " - " << abs(imag) << 'i' << '\n';}
        else { std::cout << real << " + " << imag << 'i' << '\n'; }
    }
};

int main() {
    Complex comp1, comp2, sum;
    
    comp1.input();
    comp2.input();

    sum = comp1 + comp2;
    sum.print();
}
