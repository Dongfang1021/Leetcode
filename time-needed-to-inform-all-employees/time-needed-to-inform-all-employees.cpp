class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int, vector<int>> m;
        
        for (int i = 0; i < n; i++) {
            m[manager[i]].push_back(i);
        }

        queue<int> q;
        q.push(headID);
        vector<int> t(n, 0);
        
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            
            for ( auto sub : m[node]) {
                t[sub] = informTime[node] + t[node];
                q.push(sub);
            }             
        }
        
        return *max_element(t.begin(), t.end());
    }
};