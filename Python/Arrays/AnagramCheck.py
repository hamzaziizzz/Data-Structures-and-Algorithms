class Anagram:
    """
    PROBLEM: Given two strings, check to see if they are anagrams. An anagram is when two strings can be written
    using the exact same letters (so you can just rearrange the letters to get a different phrase or word).

    For example:
        "public relations" is an anagram of "crap built on lies."
        "clint eastwood" is anagram of "old west action"

    Note: Ignore spaces and capitalization. So "d go" is an anagram of "God" and "dog" and "od g".
    """

    def __init__(self, string1, string2):
        self.string1 = string1.lower()
        self.string2 = string2.lower()

    def anagram(self):
        list1 = []
        for x in self.string1:
            if x == ' ':
                continue
            list1.append(x)
        list1 = sorted(list1)

        list2 = []
        for y in self.string2:
            if y == ' ':
                continue
            list2.append(y)
        list2 = sorted(list2)

        if list1 == list2:
            return True

        return False


if __name__ == '__main__':
    anagram1 = Anagram("dog", "god")
    print(anagram1.anagram())

    anagram2 = Anagram("clint eastwood", "old west action")
    print(anagram2.anagram())

    anagram3 = Anagram("aa", "bb")
    print(anagram3.anagram())

    anagram4 = Anagram("HAMZA", "hamza aziz")
    print(anagram4.anagram())
