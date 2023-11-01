class Solution {
    public boolean canPartition(int[] nums) {
        int len = nums.length;
        if (len < 2) return false;
        int max = 0;
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += nums[i];
            max = Math.max(max, nums[i]);
        }
        if (sum % 2 == 1) return false;
        int target = sum/2;
        if (target < max) return false;

        /*
        易知背包容量 = sum/2
        
        与常规背包问题不同,常规背包中要求 重量<=背包容量
        本题可以看作是要求 重量==背包容量 时,能否使用给出的数字填满

		采用int滚动数组或boolean滚动数组判断即可
		int数组中0代表false,正数代表true
         */
        
        
        int[] dp = new int[target+1];
        dp[nums[0]] = 1;

        for (int i = 1; i < len; i++) {
            for (int j = target; j >= nums[i]; j--) {
            	//1.dp[j]或dp[j-nums[i]]有一个为正数即可说明dp[j]成立
            	//2.如果使用Boolean数组只需要把+换成|即可
            	//3.注意到当题目给的数据较大时,我们在动态递归中数字可能会超出限制
            	//那么使用取模的方式保证不超限即可(当然可以使用long数组或BigInteger等)
                dp[j] = (dp[j] + dp[j - nums[i]])%1011;
            }
        }
        return dp[target] > 0;
    }
}