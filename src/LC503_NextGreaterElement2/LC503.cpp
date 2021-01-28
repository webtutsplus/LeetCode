class LC503 {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        for(int i=0; i<n; i++)
            nums.push_back(nums[i]);
        vector<int> ans(2*n, -1);
        stack<int> st;
        st.push(0);
        for(int i=1; i<2*n; i++)
        {
            while(!st.empty() && nums[st.top()] < nums[i]) {
                int index = st.top();
                st.pop();
                ans[index] = nums[i];
            }
            st.push(i);
        }
        return vector<int> (ans.begin(), ans.begin()+n);
    }
};