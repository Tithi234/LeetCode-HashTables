class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        seen = set()       # To store characters in the current window
        left = 0           # Left pointer for the sliding window
        max_len = 0        # Track the maximum length found

        for right in range(len(s)):  # Expand the window using 'right'
            # If character already seen, shrink window from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])  # Add the new character
            max_len = max(max_len, right - left + 1)

        return max_len
