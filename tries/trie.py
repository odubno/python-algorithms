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

        Time: O(w), w being the word. We check the presence of each letter.
        Look up time is O(1) b/c we're using a dictionary
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

    def delete_recursive(self, word, current_node, length=None, level=0):
        """
        1. start at the root and at each level check if next letter is present
        2. if last letter of the word has more children, don't delete, un-mark it as the end word
        3. if no children, delete, keep moving up and doing the same checks
        """
        delete_node = False
        if not current_node:
            return delete_node

        if length is None:
            length = len(word)

        # full word is reached
        if level == length:
            # if there are no child nodes, we could delete the node
            if not current_node.children:
                delete_node = True
            else:
                current_node.is_end_word = False
                delete_node = False
        else:
            # use level to index out each letter
            letter = word[level]
            child = current_node.children.get(letter)
            level += 1
            delete_child = self.delete_recursive(word, child, length, level)
            if delete_child:
                # child has been deleted, set child value to None
                # remove children from current node
                current_node.children = {}

                # if current node is a leaf node, then its part of another key
                if current_node.is_end_word:
                    # can't delete this node it's parent nodes
                    delete_node = False
                # if current node has children it cannot be deleted
                elif current_node.children:
                    delete_node = False
                else:
                    # we reached the end, we could delete this node
                    delete_node = True

        return delete_node

    def delete(self, word) -> bool:
        if not word:
            return False
        return self.delete_recursive(word, self.root)


def main():
    t = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    for word in words:
        t.insert(word)

    # test assert
    assert t.search('answer')
    assert not t.search('amp')
    assert t.search("abc")

    # test delete with 2 letter to be removed
    t.delete("abc")
    assert not t.search("abc")
    assert t.root.children['a'].children == {}

    # test delete with word that doesn't exist
    assert not t.search('california'), "california does not exist, and nothing should be deleted"
    t.delete('california')

    # test word that is a subset of existing word
    assert t.search('the')
    t.delete('the')
    assert not t.search('the')
    assert t.search('there'), "'there' should still be present after 'the' is delete"
    print('l')


main()
