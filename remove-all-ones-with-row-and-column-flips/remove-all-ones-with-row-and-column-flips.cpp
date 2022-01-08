class Solution {
public:
    bool removeOnes(vector<vector<int>>& grid) {
        vector<int> r0 = grid[0];
        vector<int> r0_flip = grid[0];
        for(auto& x : r0_flip) x = 1-x;
        
        for (int i = 1; i < grid.size(); i++) {
            if (grid[i] != r0 && grid[i] != r0_flip)
                return false;
        }
        
        return true;
    }
};