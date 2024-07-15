

本题和[代码随想录：两个字符串的删除操作](https://www.programmercarl.com/0583.%E4%B8%A4%E4%B8%AA%E5%AD%97%E7%AC%A6%E4%B8%B2%E7%9A%84%E5%88%A0%E9%99%A4%E6%93%8D%E4%BD%9C.html) 思路基本是一样的。 


```CPP 
#include <iostream>
#include <vector>
using namespace std;
int main() {
    string s1, s2;
    cin >> s1 >> s2;
    vector<vector<int>> dp(s1.size() + 1, vector<int>(s2.size() + 1, 0));

    // s1 如果变成空串的最小删除ASCLL值综合
    for (int i = 1; i <= s1.size(); i++) dp[i][0] = dp[i - 1][0] + s1[i - 1];
    // s2 如果变成空串的最小删除ASCLL值综合
    for (int j = 1; j <= s2.size(); j++) dp[0][j] = dp[0][j - 1] + s2[j - 1];

    for (int i = 1; i <= s1.size(); i++) {
        for (int j = 1; j <= s2.size(); j++) {
            if (s1[i - 1] == s2[j - 1]) dp[i][j] = dp[i - 1][j - 1];
            else dp[i][j] = min(dp[i - 1][j] + s1[i - 1], dp[i][j - 1] + s2[j - 1]);
        }
    }
    cout << dp[s1.size()][s2.size()] << endl;

}
```

