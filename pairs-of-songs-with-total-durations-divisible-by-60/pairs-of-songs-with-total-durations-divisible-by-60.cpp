class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> rem;
        
        for (auto t: time) {
            rem.push_back(t % 60);
        }
        
        unordered_map<int, int> m;
        for (auto r : rem) {
            m[r]++;
        }
        
        int ret = 0;
        for (int i = 1; i <= 29; i++) {
            ret += m[i]*m[60-i];
        }
        
        ret += (m[0]*(m[0]-1)) / 2;
        ret += (m[30]*(m[30]-1)) /2;
        
        return ret;
    }
};