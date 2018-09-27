#include <iostream>



class Calculator {
private:
    double x, y;

public:
    int iadd(int a, int b) {return a+b;}
    double dadd(double a, double b) {return a+b;}
    int isubtract(int a, int b) {return a-b;}
    double dsubtract(double a, double b) {return a-b;}
    int imultiply(int a, int b) {return a*b;}
    double dmultiply(double a, double b) {return a*b;}

    int idivide(int a, int b) {
        if (b == 0){
            throw std::logic_error("Can't divide by 0");
        }
        else{
            return a/b;
        }
    }

    double ddivide(double a, double b) {

        if (b == 0){
            throw std::logic_error("Can't divide by 0");
        }
        else{
            return a/b;
        }
    }

    int isquare(int a) {return a*a;}
    double dsquare(double a) {return a*a;}

};

int main() {
    int a = 2;
    int b = 3;
    Calculator calc;
    std::cout << calc.iadd(a, b);

}