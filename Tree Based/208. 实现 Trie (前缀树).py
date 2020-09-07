"""
实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");
trie.search("app");     // 返回 true
说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

题目分析

Trie 树，又叫字典树、前缀树（Prefix Tree）、单词查找树或键树，是一种多叉树结构。如下图
上图是一棵 Tie 树，表示了关键字集合“a""to", "tea""ted", "ten“，“T", "in"inn“。从上图可以归纳出 Trie 树的基本性质：

根节点不包含字符，除根节点外的每一个子节点都包含一个字符

2. 从根节点到某一个节点，路径上经过的字符连接起来，为该节点对应的字符串。3. 每个节点的所有子节点包含的字符互不相同

通常在实现的时候，会在节点结构中设置一个标志，用来标记该结点处是否构成一个单词（关键字）。

可以看出，Trie 树的关键字一般都是字符串，而且 Trie 树把每个关键字保存在一条路径上，而不是一个结点中。另外，两个有公共前缀的关键字，在 Trie 树中前缀部分的路径相同，所以 Trie 树又叫做前缀树（Prefix Tree）。

优点

插入和查询的效率很高，都为 O (m），其中 m 是待插入査询的字符串的长度。

2. 关于查询，会有人说 hash 表时间复杂度是 O (1) 不是更快？但是，哈希搜索的效率通常取决于
Hash 函数的好坏，若一个坏的 hash 函数导致很多的冲突，效率并不ー一定比 Trie 树高。
Tie 树中不同的关键字不会产生冲突

3.Trie 树只有在允许一个关键字关联多个值的情下才有类似 hash 碰撞发生

4.Trie 树不用求 hash 值，对短字符串有更快的速度。通常，求 hash 值也是需要遍历字符串的。
5.Trie 树可以对关键字按字典序排序。

缺点

1. 当 hash 函数很好时，Trie 树的查找效率会低于哈希搜索。
2. 空间消耗比较大。

应用

字符串检索词频统计字符串排序前缀匹配

作为其他数据结构和算法的辅助结构，如后缀树，AC 自动机等。
"""

"""
本题解析

作为本体来说，还是很简单的，只是构建一颗简单的 Trie 树，其中有三个操作，分别是 nsert

 search、startwith, insert 很好理解，search 是查询输入的单词是不是插入 Tie 树过，startwith 是看看有没有相同的前缀，比如插入了 apple，那么 app 就是它的一个前缀

我们为了直观展示，申请一颗 Node 类，作为一个辅助类，这样虽然耗费空间大一点，但是更加直观
"""

class Node:
    def _init_(self):
        self.children = {}
        self.is_leaf= False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.is_leaf = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_leaf


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
