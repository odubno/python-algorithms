"""

"""


class TrieNode:

    def __init__(self, char=''):
        # set char to default to '' i.e. empty string to represent root
        # store pointers to the children
        self.children = {}
        # true if the node represents the end of word
        self.is_end_word = False
        # store the value of a particular key
        self.char = char


class Trie:

    """
    1. use a dictionary of children to track common prefixes
    2. create child nodes when one doesn't exist
    3. if all the letters of the word are already present, mark the end letter as the end word

    Time: O(n) since we need to make n iterations over n characters.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> bool:
        if word is None:
            return False

        curr_node = self.root

        for letter in word.lower():
            # get the child node
            children = curr_node.children.get(letter)

            if not children:
                # if children don't exist add them
                curr_node.children[letter] = TrieNode(letter)

            curr_node = curr_node.children[letter]

        curr_node.is_end_word = True

        return True

    def search(self, word: str) -> bool:
        """
        Use BFS to search
        """
        if not word:
            return False

        curr_node = self.root
        for letter in word.lower():
            children = curr_node.children.get(letter)
            if not children:
                return False
            curr_node = children
        else:
            if curr_node.is_end_word:
                return True
        return False


def main():
    t = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    for word in words:
        t.insert(word)

    assert t.search('answer')
    assert not t.search('amp')
    print('ok')


main()
