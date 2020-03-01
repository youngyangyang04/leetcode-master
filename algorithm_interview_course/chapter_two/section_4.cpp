/* ************************************************************************
> File Name:     section_4.cpp
> Author:        sunxiuyang
> Mail:          sunxiuyang04@gmail.com 
> Created Time:  Tue Feb 18 23:34:08 2020
> Description:   
 ************************************************************************/

#include<iostream> 
using namespace std;

struct node{
   int num;
   char cha;
}st;

int main() {
    int a[100];
    char b[100];
    cout << sizeof(int) << endl;
    cout << sizeof(char) << endl;
    cout << sizeof(a) << endl;
    cout << sizeof(b) << endl;
    cout << sizeof(st) << endl;
}
