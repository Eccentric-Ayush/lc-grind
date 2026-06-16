#include <vector>
#include <unordered_map>

class Solution {
public:
    int fourSumCount(std::vector<int>& nums1, std::vector<int>& nums2, std::vector<int>& nums3, std::vector<int>& nums4) {
        std::unordered_map<int, int> sum_counts;
        int count = 0;
        
        // Step 1: Store all possible sums of nums1 and nums2 into the hash map
        for (int u : nums1) {
            for (int v : nums2) {
                sum_counts[u + v]++;
            }
        }
        
        // Step 2: Find complementary sums using nums3 and nums4
        for (int w : nums3) {
            for (int z : nums4) {
                int target = -(w + z);
                if (sum_counts.contains(target)) {
                    count += sum_counts[target];
                }
            }
        }
        
        return count;
    }
};