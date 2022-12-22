"""
implement the find_words() function which will return a sorted list of all
the words stored in a trie.
"""
from trie import Trie
from typing import List
import bisect
from collections import deque


def find_words(root: Trie, word=None, words=None) -> List[str]:
    """
    1. Use DFS to search through the trie
    2. maintain a queue of all preceding letters
    2. Check if node is end of word and maintain a list of results
    3. recursively call find_words until all nodes are visited
    """
    if words is None:
        words = []
    if word is None:
        word = deque()

    for letter, child in root.children.items():

        # track each word
        word.append(letter)
        if child.is_end_word:
            # insert item into a sorted list
            # O(N) b/c insertion is slow
            bisect.insort(words, ''.join(word))

        # recursively visit all nodes
        find_words(child, word, words)

        # pop the last seen letter off the queue
        word.pop()

    return words


def main():
    t = Trie()
    words = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
    for word in words:
        t.insert(word)

    result = find_words(t.root)
    assert result == ["a", "abc", "answer", "any", "by", "bye", "the", "their", "there"]


main()
