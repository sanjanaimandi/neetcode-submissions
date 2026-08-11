class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> ana;
        unordered_map<char, int> ana2;

        for (int i = 0; i < s.size(); i++) {
            ana[s[i]]++;
            ana2[t[i]]++;
        }
        if (ana == ana2) {
            return true;
        }
        return false;
    }
};