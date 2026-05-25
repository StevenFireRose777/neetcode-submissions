class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded_string;

        for(int i = 0; i < strs.size(); ++i)
        {
            encoded_string += to_string(strs[i].size()) + "#" + strs[i];
        }
        return encoded_string;
    }

    vector<string> decode(string s) {
        vector<string> strs;
        int i = 0;
        while(i < s.size())
        {
            int pos = s.find('#', i);
            int length = stoi(s.substr(i, pos - i));
            strs.push_back(s.substr(pos + 1, length));
            i = pos + 1 + length;
        }

        return strs;
    }
};
