from collections import defaultdict

class TrieNode:
    """Node of the trie"""

    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Dictionary:
    """
    Dictionary is built on trie. The main reason is to get partial match which is currently
    unimplemented and reduce time complexity for search.
    """

    def __init__(self, words):
        """
        Root is inialized and all words in the iterable are inserted
        :param words: Iterable, words iterable
        """
        self.root = self.get_node()
        for word in words:
            self.insert(word)

    def get_node(self):
        """
        Creates a void Node
        :return: TrieNode
        """
        return TrieNode()

    def _char_to_index(self, ch):
        """
        Converts character to ord value. This is currently only for small case letters since
        the dictionary is comprised of lowercase letters. Going forward we need to expand that
        :param ch: char, character
        :return: int, index
        """
        return ord(ch) - ord('a')

    def insert(self, key):
        """
        Inserts a word into the trie
        :param key: word to be inserted
        :return:
        """
        p1 = self.root
        key_len = len(key)
        for level in range(key_len):
            index = self._char_to_index(key[level])
            if not p1.children[index]:
                p1.children[index] = self.get_node()
            p1 = p1.children[index]
        p1.end = True

    def search(self, key):
        """
        Searches a word in the trie. Returns True if found else False
        :param key: str, word to be searched
        :return:
        """
        p1 = self.root
        key_len = len(key)
        for level in range(key_len):
            index = self._char_to_index(key[level])
            # TODO: This try-catch should be removed. We need to check alphabets outside
            try:
                if not p1.children[index]:
                    return False
            except:
                return False
            p1 = p1.children[index]
        return p1 != None and p1.end

    @classmethod
    def from_txt(cls, textFile):
        """
        Initializes a dictionary given a text file where every line contains a word.
        Reads from corpus directory. Only filename is required.
        :param textFile: str, filename of dictionary to be read present in corpus
        :return: Dictionary, Trie after inserting all words from file
        """
        f = open("../corpus/" + textFile).read().split("\n")
        return cls(f)

    def __contains__(self, item):
        """
        Operator overriding for in
        :param item: str, text to lookup in trie
        :return: boolean, text present in trie
        """
        return self.search(item)


class Dictionary_old:

    def __init__(self, words):
        """
        Root is inialized and all words in the iterable are inserted
        :param words: Iterable, words iterable
        """
        self.root = set()
        for word in words:
            self.insert(word)

    @classmethod
    def from_txt(cls, textFile):
        """
        Initializes a dictionary given a text file where every line contains a word.
        Reads from corpus directory. Only filename is required.
        :param textFile: str, filename of dictionary to be read present in corpus
        :return: Dictionary, Trie after inserting all words from file
        """
        f = open("../corpus/" + textFile).read().split("\n")
        return cls(f)

    def insert(self, key):
        p1 = self.root
        p1.add(key)

    def search(self, key):
        p1 = self.root
        return key in p1


if __name__ == '__main__':
    # TODO:Remove after writing test cases
    words = ["the", "a", "there", "anaswe", "any", "by", "their"]
    t = Dictionary.from_txt("english-20k-words.txt")
    print(t.search("bye"))
    print(t.search("keepoop"))
    print("bytte" in t)
