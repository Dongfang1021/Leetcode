class Solution {
public:
    vector<int> recoverArray(vector<int>& nums) {
        const int n = nums.size()/2;

        sort(nums.begin(), nums.end());

        for(int ii = 1; ii < 2*n; ii++) {
            int k = nums[ii] - nums[0];
            if (k == 0 || k % 2 != 0) continue;
            k /= 2;
            
            vector<int> res;
            vector<int> used(2*n);
            int j = 1;
            bool fail = false;
            for (int i = 0; i < 2*n-1; i++) {
                if (used[i]) continue;
                res.push_back(nums[i] + k);
                used[i] = true;
                for (; j < 2*n; j++) {
                    if (used[j]) continue;
                    if (nums[j] >= nums[i] + 2*k) break;
                }
                if (j >= 2*n || nums[j] > nums[i] + 2*k) { fail = true; break;}
                else used[j] = true;
            }
            
            if (!fail) return res;
        }
        
        return vector<int>();
    }
};