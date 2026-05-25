class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
   
        unordered_map<int,int> freq; // hashmap
        vector<int> res; // vector to hold results
        for(int i = 0; i < nums.size(); ++i){
            freq[nums[i]]++; // increment freq of every element
        }

        priority_queue<pair<int,int>>pq; // priority queue to store values
        for(auto it = freq.begin(); it != freq.end(); ++it)
        {
            pq.push({it->second, it->first}); // {freq: 10, element: 2}
        }
        for(int i = 0; i < k; ++i)
        {
            res.push_back(pq.top().second); // IT would get the element of with the most frequencies k allows
            pq.pop(); // get rid of that pair and move on
        }
        return res;

    }
};
