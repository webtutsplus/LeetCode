class LC442 {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        int n = nums.size();
        for(int num : nums)
        {
            int temp = num;
            while(temp > n) temp -= n;
            int index = temp-1;
            nums[index] += n;
        }
        vector<int> ans;
        for(int i=0; i<n; i++)
            if(nums[i] > 2*n)
                ans.push_back(i+1);
        return ans;
    }
};