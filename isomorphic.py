class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_st = {}
        map_ts = {}

        for ch_s, ch_t in zip(s, t):
            # Check if mapping from s → t exists and matches
            if ch_s in map_st and map_st[ch_s] != ch_t:
                return False

            # Check if mapping from t → s exists and matches
            if ch_t in map_ts[ch_t] != ch_s:
                return False

            # Store the mapping
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s

        return True
