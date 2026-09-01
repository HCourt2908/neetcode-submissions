class Solution {
    public int[] productExceptSelf(int[] nums) {

        int[] lefts = new int[nums.length];
        int[] rights = new int[nums.length];
        int[] results = new int[nums.length];

        lefts[0] = 1;
        rights[nums.length-1] = 1;
        for (int i = 1; i < nums.length; i++) {
            lefts[i] = lefts[i-1] * nums[i-1];
        }
        for (int i = nums.length-2; i >= 0; i--) {
            rights[i] = rights[i+1] * nums[i+1];
        }
        for (int i = 0; i < nums.length; i++) {
            results[i] = lefts[i] * rights[i];
        }

        return results;
        
    }
}  
