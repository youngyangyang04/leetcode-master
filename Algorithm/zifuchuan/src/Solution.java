class Solution {
    public boolean repeatedSubstringPattern(String s) {
        //字符串为空直接返回
        if(s.equals("")) return false;
        //获取字符串的长度
        int len = s.length();
        //把字符串s转换为数组进行操作
        char[] chars = s.toCharArray();
        //新建next数组
        int[] next = new int[len];
        int j = 0;
        next[0] = 0;
        //为next数组赋值
        for(int i = 1; i < chars.length; i++){
            while(j > 0 && chars[i] != chars[j]){
                j = next[j - 1];
            }
            if(chars[i] == chars[j]){
                j++;
            }
            next[i] = j;
        }
        //判断是否是重复的子字符串
        if(next[len - 1] > 0 && len % (len - next[len - 1]) == 0){
            return true;
        }
        return false;



    }
}