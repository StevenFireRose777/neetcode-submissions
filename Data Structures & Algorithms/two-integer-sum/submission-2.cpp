class Solution {
public:


    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hash_map; // key: index, value: val
        int n = nums.size();
        int complement;
        int curr_val;
        for(int i = 0; i < n; ++i)
        {
            curr_val = nums[i];
            complement = target - curr_val;
            if(hash_map.find(complement) != hash_map.end())
            {
                return {hash_map[complement], i};
            }else
            {
                hash_map[nums[i]] = i;   
            }
        }
        return {};
        // return [i, hash_map[complement]];


        
    }
};
