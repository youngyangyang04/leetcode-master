### 0x01 数组中两个数相加等于目标数字

[Two Sum](https://leetcode.com/problems/two-sum/)

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

**Code：**

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i};
      i      }
            map.put(nums[i], i);
        }
        return null;
    }
}
```

### 0x02 回文数a判断：

[Palindrome Number](https://leetcode.com/problems/palindrome-number/)

**Example 1:**

```
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
```

**Example 2:**

```
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
```

**Example 3:**

```
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

**Code：**

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

### 0x03 罗马数字转化为整数

[Roman to Integer](https://leetcode.com/problems/palindrome-number/)

**Example 1:**

```
Input: s = "III"
Output: 3
Explanation: III = 3.
```

**Example 2:**

```
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
```

**Example 3:**

```
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
```

**Code**:

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        values = { "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = values[s[len(s)-1]]
        for i in range(len(s)-2, -1, -1):
            if values[s[i]] >= values[s[i+1]]:
                result += values[s[i]]
            else:
                result -= values[s[i]]
        return result
```

### 0x04 Longest Common Prefix

**Description:**

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Example 1:**

```
Input: strs = ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**

```
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
```

**Code:**

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        prefix = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y:
                prefix += x
            else:
                break
        return prefix
```

**Reference**

[字符串的常见算法问题总结（LIS、LCS、LCP、LPS、ED、KMP）](https://blog.csdn.net/Deeven123/article/details/82930354)



### 0x05 Valid Parentheses

**Description**

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

**Example 1:**

```
Input: s = "()"
Output: true
```

**Example 2:**

```
Input: s = "()[]{}"
Output: true
```

**Example 3:**

```
Input: s = "(]"
Output: false
```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of parentheses only `'()[]{}'`.

**Code:**

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.append(i)
            elif (not stack):   #排除"["
                return False
            else:
                tail = stack.pop()
                if i == '}' and tail != '{':
                    return False
                elif i == ']' and tail != '[':
                    return False
                elif i == ')' and tail != '(':
                    return False
        return len(stack) == 0
```



### 0x06 Merge Two Sorted Lists

**Description**

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one **sorted** list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list*.

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

**Example 2:**

```
Input: list1 = [], list2 = []
Output: []
```

**Example 3:**

```
Input: list1 = [], list2 = [0]
Output: [0]
```

**Constraints:**

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in **non-decreasing** order.

**Code:**

```C++
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
//        while(list1 != nullptr) {
//            printf("%d ", list1->val);
//            list1 = list1->next;
//        }
//        printf("\n");
//        while(list2 != nullptr) {
//            printf("%d ", list2->val);
//            list2 = list2->next;
//        }
        ListNode *res = new ListNode();
        ListNode *t = new ListNode();
        t = res;
        res->val = 0xffff;
        while(list1 != nullptr || list2 != nullptr) {
            if (list1 != nullptr && list2 != nullptr) {
                ListNode *n = new ListNode();
                if (list1->val <= list2->val) {
                    n->val = list1->val;
                    t->next = n;
                    t = n;
                    list1 = list1->next;
                }
                else {
                    n->val = list2->val;
                    t->next = n;
                    t = n;
                    list2 = list2->next;
                }
            }
            else {
                if (list1 != nullptr) {
                    ListNode *n = new ListNode();
                    n->val = list1->val;
                    t->next = n;
                    t = n;
                    list1 = list1->next;
                }
                else if (list2 != nullptr) {
                    ListNode *n = new ListNode();
                    n->val = list2->val;
                    t->next = n;
                    t = n;
                    list2 = list2->next;
                }
            }
        }
        return res->next;
    }
};
```



### 0x07 Remove Duplicates from Sorted Array

**Description**

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Example 1:**

```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**

- `1 <= nums.length <= 3 * 104`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing** order.

```c++
class Solution {
public:
    int removeDuplicates(std::vector<int>& nums) {
        if (nums.size() == 0)   return 0;
        int i = 0;
        for (int j = 1; j < nums.size(); j++) {
            if (nums[i] != nums[j]) {
                i++;
                nums[i] = nums[j];
            }
        }
        return i + 1;
    }
};
```



### 0x08 Remove Element

**Description**

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k` *after placing the final result in the first* `k` *slots of* `nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array [in-place](https://en.wikipedia.org/wiki/In-place_algorithm)** with O(1) extra memory.

**Example 1:**

```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Example 2:**

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
```

**Constraints:**

- `0 <= nums.length <= 100`
- `0 <= nums[i] <= 50`
- `0 <= val <= 100`

**Code:**

```C++
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size() == 0)   return 0;
        int i = 0;
        for (int j = 0; j < nums.size(); j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};
```



### 0x09 Search Insert Position

**Description**

Given a sorted array of distinct integers and a target value, return the index if the  target is found. If not, return the index where it would be if it were  inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

 

**Example 1:**

```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

**Example 2:**

```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

**Example 3:**

```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

**Constraints:**

- `1 <= nums.length <= 104`
- `-104 <= nums[i] <= 104`
- `nums` contains **distinct** values sorted in **ascending** order.
- `-104 <= target <= 104`

**Code(Binary Search):**

```C++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1, pivot = ((unsigned int)left  + (unsigned int)right) >> 1;
        while(left <= right) {
            pivot = ((unsigned int)left + (unsigned int)right) >> 1;
            if (nums[pivot] == target)  return pivot;
            else if (nums[pivot] < target)  left = pivot + 1;
            else    right = pivot - 1;
        }
        return left;
    }
};
```



### 0x0a Length of Last Word

**Description**

Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

A **word** is a maximal substring consisting of non-space characters only.

**Example 1:**

```
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
```

**Example 2:**

```
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
```

**Example 3:**

```
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
```

**Constraints:**

- `1 <= s.length <= 104`
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

**Code:**

```C++
class Solution {
public:
    int lengthOfLastWord(string s) {
        int res = 0, flag = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                res++;
                flag = 1;
            }
            if (i - 1 >= 0 && s[i-1] == ' ' && flag == 1) {
                break;
            }
        }
        return res;
    }
};
```



### 0x0b Plus One

**Description**

You are given a **large integer** represented as an integer array `digits`, where each `digits[i]` is the `ith` digit of the integer. The digits are ordered from most significant to  least significant in left-to-right order. The large integer does not  contain any leading `0`'s.

Increment the large integer by one and return *the resulting array of digits*.

**Example 1:**

```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**

```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**

```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

**Constraints:**

- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- `digits` does not contain any leading `0`'s.

**Code:**

```C++
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();

        for (int i = len - 1; i >= 0; i--) {
            if (digits[i] == 9) {
                digits[i] = 0;
            }
            else {
                digits[i]++;
                return digits;
            }
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
```

