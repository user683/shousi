'''
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。

请你实现 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 

'''



class Trie:
    
    def __init__(self):
        self.childern = {}
        self.is_end= False
    
    def insert(self, word):
        # 像前缀树中插入一个字符
        node = self  
        for ch in  word:
            if ch not in node.childern:
                node.childern[ch] = Trie()
            node = node.childern[ch]
        node.is_end = True
        
    def _find(self, s):
        '''查找字符串s对应的节点，如果不存在则返回None'''
        node = self
        for ch in s:
            if ch not in node.childern:
                return None
            node = node.childern[ch]
        return node
    
    def search(self, word):
        node = self._find(word)
        return node is not None and node.is_end
    
    def startsWith(self, prefix):
        node = self._find(prefix)
        return node is not None
    

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # 返回 True
    print(trie.search("app"))     # 返回 False
    print(trie.startsWith("app")) # 返回 True
    trie.insert("app")
    print(trie.search("app"))     # 返回 True