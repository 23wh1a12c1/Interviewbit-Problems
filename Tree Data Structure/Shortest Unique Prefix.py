####    PYTHON3


class TrieNode:
    def __init__(self):
        self.next = {}
        self.count = 0

class Solution:
    def prefix(self, A):
        root = TrieNode()
        
        def insert(s):
            node = root
            for c in s:
                if c not in node.next:
                    node.next[c] = TrieNode()
                node = node.next[c]
                node.count += 1
        
        def get_prefix(s):
            node = root
            res = []
            for c in s:
                node = node.next[c]
                res.append(c)
                if node.count == 1:
                    break
            return "".join(res)
        
        for word in A:
            insert(word)
        
        return [get_prefix(word) for word in A]







#########     JAVA


import java.util.*;

class TrieNode {
    TrieNode[] next = new TrieNode[26];
    int count = 0;
}

public class Solution {
    // Inserts a word into the Trie
    private void insert(TrieNode root, String s) {
        TrieNode node = root;
        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            if (node.next[idx] == null) node.next[idx] = new TrieNode();
            node = node.next[idx];
            node.count++;
        }
    }
    
    // Finds prefix for a word
    private String getPrefix(TrieNode root, String s) {
        TrieNode node = root;
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            int idx = c - 'a';
            node = node.next[idx];
            sb.append(c);
            if (node.count == 1) break;
        }
        return sb.toString();
    }

    public ArrayList<String> prefix(ArrayList<String> A) {
        TrieNode root = new TrieNode();
        for (String word : A) insert(root, word);
        ArrayList<String> res = new ArrayList<>();
        for (String word : A) res.add(getPrefix(root, word));
        return res;
    }
}








#####   C++



struct Trie {
    unordered_map<char, Trie*> next;
    int count;
    Trie():count(0) {}
    void insert(string& s, int p = 0) {
        count += 1;
        if(s.length() != p) {
            if(!next.count(s[p])) next[s[p]] = new Trie();
            next[s[p]]->insert(s,p+1);
        }
    }
};
string query(string s, Trie* t) {
    Trie* runner = t;
    int p = 0;
    string res = "";
    while(runner->count > 1) {
        runner = runner->next[s[p]];
        res.push_back(s[p++]);
    }
    return res;
}
vector<string> Solution::prefix(vector<string> &A) {
    Trie* t = new Trie();
    for(auto a : A) t->insert(a);
    vector<string> res;
    for(auto a : A) res.push_back(query(a,t));
    return res;
}




