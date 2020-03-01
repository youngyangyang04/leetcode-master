/* ************************************************************************
> File Name:     section_5.cpp
> Author:        sunxiuyang
> Mail:          sunxiuyang04@gmail.com 
> Created Time:  Mon Feb 24 18:44:56 2020
> Description:   
 ************************************************************************/

#include <iostream>
#include <chrono>
#include <thread>
using namespace std;
using namespace chrono;

int fibonacci_1(int n) {
    if (n <= 0) {
        return 0;
    }
    if (n == 1 || n == 2) {
        return 1;
    }
    int first = 1, second = 1; 
    int sum = first + second; 
    for (int i = 2; i < n; i++) {
        sum = first + second;
        first = second;
        second = sum;
    }
    return sum;
}


int fibonacci_2(int i) {
       if(i <= 0) return 0;
       if(i == 1) return 1;
       return fibonacci_2(i - 1) + fibonacci_2(i - 2);
}

int fibonacci_3(int first, int second, int n) {
    if (n <= 0) {
        return 0;
    }
    if (n < 3) {
        return 1;
    }
    else if (n == 3) {
        return first + second;
    }
    else {
        return fibonacci_3(second, first + second, n - 1);
    }
}


void test_fibonacci() {
    int n;
    while(cin >> n) {
        cout << fibonacci_1(n) << endl;
        cout << fibonacci_2(n) << endl;
        cout << fibonacci_3(1, 1, n) << endl;
    } 
}

int binary_search(int arr[], int l, int r, int n) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == n)
            return mid;
        if (arr[mid] > n)
            return binary_search(arr, l, mid - 1, n);
        return binary_search(arr, mid + 1, r, n);
    }
    return -1;
}
int arr[] = {2, 3, 4, 5, 8, 10, 15, 17, 20};
int binary_search(int l, int r, int n) {
    if (r >= l) {
        int mid = l + (r - l) / 2;
        if (arr[mid] == n)
            return mid;
        if (arr[mid] > n)
            return binary_search(l, mid - 1, n);
        return binary_search(mid + 1, r, n);
    }
    return -1;
}

void test_binary_search(void) {
    int arr[] = {2, 3, 4, 5, 8, 10, 15, 17, 20};
    int x = 17;
    int n = sizeof(arr) / sizeof(arr[0]);
    // int result = binary_search(arr, 0, n - 1, x);
    int result = binary_search(0, n - 1, x);
    (result == -1) ? cout << "Element is not present in array"
                   : cout << "Element is present at index " << result;
}

int main()
{
    // test_binary_search();
    // test_fibonacci();
    return 0;
}

