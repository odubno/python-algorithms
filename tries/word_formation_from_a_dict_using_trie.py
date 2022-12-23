"""
implement the is_formation_possible() function which will find whether a
given word can be formed by combining two words from a dictionary. We assume
that all words are in lower case.
"""

from trie import Trie


def get_word(root):
    pass


def is_formation_possible(dictionary, target_word):
    """
    1. turn dictionary into a trie
    2. loop over the letters in the word
        1. use each letter to check if the letter exists in the trie
        2. if the letter exists continue otherwise break
        3. check if node is end word, if it is then add our word to a result list
        4. start search from the root again for the rest of the letters in word
    Time: O(N^2) for each letter in word we look at each node in trie
        leading to a nested loop causing quadratic time
    """

    # create a Trie
    curr_trie = Trie()
    for word in dictionary:
        curr_trie.insert(word)

    curr_node = curr_trie.root

    for target_letter in target_word:  # h ... o, w
        child = curr_node.children.get(target_letter)  # h ... o, w
        if not child:
            return False
        if child.is_end_word:
            # we found one word, continue search for next word by resetting curr_node
            # start trie search all over while continuing word search
            child = curr_trie.root
        curr_node = child
    else:
        return True


def main():
    dictionary = ["the", "hello", "there", "answer", "any", "by", "world", "their", "abc"]
    assert is_formation_possible(dictionary, "helloworld")


main()
