
原理：[0239.滑动窗口最大值](https://github.com/youngyangyang04/leetcode/blob/master/problems/0239.滑动窗口最大值.md) |滑动窗口/队列 |困难| **单调队列**|

```
class Solution {
public:
    class MyQueue { //单调队列（从大到小）
    public:
        deque<int> que; // 使用deque来实现单调队列
        void pop(int value) {
            if (!que.empty() && value == que.front()) {
                que.pop_front();
            }
        }
        void push(int value) {
            while (!que.empty() && value > que.back()) {
                que.pop_back();
            }
            que.push_back(value);

        }
        int front() {
            return que.front();
        }
    };
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        MyQueue que;
        vector<int> result;
        if (nums.empty()) {
            return result;
        }
        for (int i = 0; i < k; i++) { // 先将前k的元素放进队列
            que.push(nums[i]);
        }
        result.push_back(que.front()); // result 记录前k的元素的最大值
        for (int i = k; i < nums.size(); i++) {
            que.pop(nums[i - k]); // 模拟滑动窗口的移动
            que.push(nums[i]); // 模拟滑动窗口的移动
            result.push_back(que.front()); // 记录对应的最大值
        }
        return result;
    }
};

```
