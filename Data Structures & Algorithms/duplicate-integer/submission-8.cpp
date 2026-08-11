class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dupl;
        for (int n : nums) {
            if (dupl.count(n)) {
                return true;
            }
            dupl.insert(n);
        }
        return false;

        }
};
