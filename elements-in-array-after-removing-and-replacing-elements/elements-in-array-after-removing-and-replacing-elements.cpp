class Solution {
public:
    vector<int> elementInNums(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> ret;
        buildMap(nums);
        for (vector<int> query : queries) {
            int val = findVal (nums, query[0], query[1]); // nums, minute, pos
            ret.push_back(val);
        }
        
        return ret;
    }
    
    int findVal(const vector<int>& nums, int minute, int pos) {
        int len = nums.size();
        int ith = minute % (2*len);
        int odd = (minute / len) & 0x1; // odd or even
        int cur_len = m[ith];
        
        // int cur_len = odd ? ith - len : len - ith;

        return pos <= cur_len - 1 ? nums[odd ? pos : len - cur_len + pos] : -1;          
    }
    
    void buildMap(vector<int>& nums) {
        // min 0: len
        // min 1: len - 1, 
        // ...
        // min len-1: 1
        // min len  : 0
        // min len+1: 1
        // min len+2: 2
        // ....
        // min 2*len-1 : len -1    5:2
        int len = nums.size();
        for (int i = 0; i < 2*len; i++) {
            if (i <= len) m[i] = len - i;
            else m[i] = i - len;
        }
    }
    
private:
    unordered_map<int, int> m;    
};