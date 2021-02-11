class LC1738 {
public:
    int kthLargestValue(vector<vector<int>>& a, int k) {
        vector<int> all;
        int n = a.size(), m = a[0].size();
        vector< vector<int> > t(n, vector<int>(m, 0));
        for(int i=0; i<n; i++) //O(n*m)
        {
            for(int j=0; j<m; j++)
            {
                if(i==0 && j==0)
                    t[0][0] = a[0][0];
                else if(i==0)
                    t[i][j] = t[i][j-1] ^ a[i][j];
                else if(j==0)
                    t[i][j] = t[i-1][j] ^ a[i][j];
                else
                    t[i][j] = t[i][j-1] ^ t[i-1][j] ^ t[i-1][j-1] ^ a[i][j];
                all.push_back(t[i][j]);
            }
        }
        //(n*m) => sorting O(n*m*log(n*m))
        sort(all.begin(), all.end());
        return all[n*m-k];
    }
};