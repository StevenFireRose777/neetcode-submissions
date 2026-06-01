class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> my_set;

        for(const auto &num : nums)
        {
            if(my_set.contains(num))
            {
                return true;
            }else
            {
                my_set.insert(num);
            }
        }
        return false;
    }
};