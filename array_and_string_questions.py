from collections import defaultdict


class ArrayAndStringQuestions:
    @staticmethod
    def is_unique(test_string: str):
        """
        Question 1.1
        Is Unique: Implement an algorithm to determine if a string has all unique characters.
        What if you cannot use additional data structures?
        :param test_string: String to be tested
        :return: Whether or not the test_string has all unique characters
        """

        char_dict = defaultdict(int)
        for char in test_string:  # We don't care about case, u and U are different characters and therefore unique
            char_dict[char] += 1

        for char, char_count in char_dict.items():
            if char_count > 1:
                return False

        return True

    @staticmethod
    def is_permutation(string1: str, string2: str):
        """
        Question 1.2
        Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
        :return: True if string 2 is a permutation of string 1.
        """
        str1_char_dict = defaultdict(int)
        for char in string1:
            str1_char_dict[char] += 1

        str2_char_dict = defaultdict(int)
        for char in string2:
            str2_char_dict[char] += 1

        for char, count in str1_char_dict.items():
            if char not in str2_char_dict or count != str2_char_dict[char]:
                return False

        return True

    @staticmethod
    def urlify(string: str, count: int):
        """
        Question 1.3
        Write a method to replace all spaces in a string with '%20: You may assume that the string
        has sufficient space at the end to hold the additional characters, and that you are given the "true"
        length of the string.
        :param string: String to 'urlify'
        :param count: The "true" length of the string.
        :return: URLified string
        """
        result = ''

        # Mr%20John%20Smith
        for i in range(count):
            result += '%20' if string[i] == ' ' else string[i]

        return result

    @staticmethod
    def palindrome_permutation(string: str):
        """
        Question 1.4
        Given a string, write a function to check if it is a permutation of a palindrome.
        A palindrome is a word or phrase that is the same forwards and backwards. A permutation
        is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
        :param string: String to check
        :return: True if it is a permutation of a palindrome, false otherwise
        """
        char_count = defaultdict(int)
        for char in string:
            char_count[char] += 1

        odd_count_hit = False  # There can only be one instance of a character that occurs only once, in a palindrome.
        for char, count in char_count.items():
            if count % 2 != 0 and odd_count_hit is False:  # If we've found a char with a count of one and it is the first occurrence found
                one_count_hit = True
            elif count % 2 != 0:  # We've already found an instance of a character with an odd count
                return False

        return True

    @staticmethod
    def one_away(string: str, edited_string: str):
        """
        Question 1.5
        There are three types of edits that can be performed on strings: insert a character,
        remove a character, or replace a character. Given two strings, write a function to check if they are
        one edit (or zero edits) away.
        :param string: Original string
        :param edited_string: Modified string
        :return: Whether or not the modified string is at most one edit away
        """
        num_differences = 1 if len(edited_string) == len(string) - 1 or len(edited_string) == len(string) + 1 else 0
