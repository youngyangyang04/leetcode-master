/* ************************************************************************
> File Name:     section_3.cpp
> Author:        sunxiuyang
> Mail:          sunxiuyang04@gmail.com 
> Created Time:  Sat Feb  8 22:00:32 2020
> Description:   
 ************************************************************************/

#include<iostream>
using namespace std;

int function1(int x, int n) {
    int result = 1;  // 注意 任何数的0次方等于1 
    for (int i = 0; i < n; i++) {
        result = result * x;
    }
    return result;
}

int function2(int x, int n) {
    if (n == 0) {
        return 1; // return 1 同样是因为0次方是等于1的
    }
    return function2(x, n - 1) * x;
}

int function3(int x, int n) {
    if (n == 0) {
        return 1;
    }
    // if (n == 1) { // 这里如果不作处理就会陷入死循环
    //     return x;
    // }
    if (n % 2 == 1) {
        return function3(x, n/2) * function3(x, n/2) * x;
    } 
    return function3(x, n/2) * function3(x, n/2);
}

int function4(int x, int n) {
    if (n == 0) {
        return 1;
    }
    int t = function4(x, n/2);
    if (n % 2 == 1) {
        return t*t*x;
    } 
    return t*t;
}
int main() {
    int x, n;
    while (cin >> x >> n) {
        cout << function3(x, n) << endl;
    }
}
