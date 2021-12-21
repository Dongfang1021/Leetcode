class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        This program uses a sliding window and a dictionary
        implemented as an array to search for a permutation
        of s1 within s2.

        :param s1: target string is permutation of s1
        :type s1: str
        :param s2: string being searched for s1 permutation
        :type s2: str
        :return: True if s1 permutation found in s2, else False
        :rtype: bool
        """
        len_s1 = len(s1)
        len_s2 = len(s2)

        """
        s1_dict contains the frequency counts for each letter in s1
        """
        s1_dict = [0] * 26
        for s in s1:
            s1_dict[ord(s) - ord('a')] += 1

        """
        Use a sliding window within s2 which is the same size as s1 to
        search for a permutation of s1 within s2.
        - Maintain s2_window_dict, which contains frequency counts for each
          letter in the current s2 window.
        - If a permutation of s1 is found in s2, return True.
        - Return False if a permutation is not found by the time the end of
          s2 is reached.
        """
        s2_window_dict = [0] * 26
        for lo in range(len_s2 - len_s1 + 1):
            hi = lo + len_s1 - 1
            if lo == 0:
                """
                First time special case: build sliding window dictionary
                """
                for k in range(len_s1):
                    s2_window_dict[ord(s2[k]) - ord('a')] += 1
            else:
                """
                Add newest letter to existing sliding window dictionary
                """
                s2_window_dict[ord(s2[hi]) - ord('a')] += 1
            if s1_dict == s2_window_dict:
                return True
            """
            Remove oldest letter from sliding window dictionary
            """
            s2_window_dict[ord(s2[lo]) - ord('a')] -= 1
        return False