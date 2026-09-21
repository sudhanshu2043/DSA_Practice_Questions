class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {

        vector<vector<int>> ans;

        sort(nums.begin(), nums.end());

        for (int h = 0; h < nums.size(); h++) {

            // Skip duplicate first element
            if (h > 0 && nums[h] == nums[h - 1])
                continue;

            for (int i = h + 1; i < nums.size(); i++) {

                // Skip duplicate second element
                if (i > h + 1 && nums[i] == nums[i - 1])
                    continue;

                int j = i + 1;
                int k = nums.size() - 1;

                while (j < k) {

                    long long sum = (long long)nums[h]+ nums[i]+ nums[j]+ nums[k];

                    if (sum == target) {

                        ans.push_back({nums[h],nums[i],nums[j],nums[k]});

                        j++;
                        k--;

                        // Skip duplicate third element
                        while (j < k && nums[j] == nums[j - 1])
                            j++;

                        // Skip duplicate fourth element
                        while (j < k && nums[k] == nums[k + 1])
                            k--;
                    }

                    else if (sum < target) {
                        j++;
                    }

                    else {
                        k--;
                    }
                }
            }
        }

        return ans;
    }
};