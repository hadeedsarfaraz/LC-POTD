class Solution {
    public int maximumScore(int[] nums, int k) {
    int n = nums.length;
    int[] leftMin = new int[n];
    int[] rightMin = new int[n];
    leftMin[k] = nums[k];
    rightMin[k] = nums[k];

    for (int i = k - 1; i >= 0; i--) {
        leftMin[i] = Math.min(nums[i], leftMin[i + 1]);
    }
    
    for (int i = k + 1; i < n; i++) {
        rightMin[i] = Math.min(nums[i], rightMin[i - 1]);
    }

    int ans = nums[k];
    int l = k, r = k;

    while (r - l < n - 1) {
        if (l > 0 && ((r + 1 < n && leftMin[l - 1] > rightMin[r + 1]) || r == n - 1)) {
            l--;
            ans = Math.max(ans, leftMin[l] * (r - l + 1));
        } else {
            r++;
            ans = Math.max(ans, rightMin[r] * (r - l + 1));
        }
    }
    
    return ans;
    }
}
