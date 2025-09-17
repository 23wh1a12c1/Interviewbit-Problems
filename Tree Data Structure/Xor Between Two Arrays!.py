###     PYTHON3


class TrieNode:
    def __init__(self):
        self.child = [None, None]

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        # Build trie with all numbers of B
        root = TrieNode()
        
        def insert(num):
            node = root
            for i in range(31, -1, -1):  # 32-bit traversal
                bit = (num >> i) & 1
                if not node.child[bit]:
                    node.child[bit] = TrieNode()
                node = node.child[bit]
        
        def query(num):
            node = root
            xor_val = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                opposite = 1 - bit
                if node.child[opposite]:
                    xor_val |= (1 << i)
                    node = node.child[opposite]
                else:
                    node = node.child[bit]
            return xor_val
        
        for b in B:
            insert(b)
        
        max_xor = 0
        for a in A:
            max_xor = max(max_xor, query(a))
        
        return max_xor













