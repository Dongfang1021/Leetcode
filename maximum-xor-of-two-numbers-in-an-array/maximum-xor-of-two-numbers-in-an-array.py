class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums))) - 2
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x  in nums]
        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in num:
                if not bit in node:
                    node[bit] = {}
                node =  node[bit]
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]
            max_xor = max(max_xor, curr_xor)
        return max_xor
        