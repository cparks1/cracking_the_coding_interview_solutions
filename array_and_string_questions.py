from collections import defaultdict
from typing import List


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

    @staticmethod
    def string_compression(string: str):
        """
        Question 1.6
        Implement a method to perform basic string compression using the counts
        of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
        "compressed" string would not become smaller than the original string, your method should return
        the original string. You can assume the string has only uppercase and lowercase letters (a - z).
        :param string: String to be compressed
        :return: Compressed string
        """
        compress_char = ''  # Holds the current character being compressed
        compress_count = 0  # Holds the number of characters of compress_char that have been found so far
        result = ''  # Holds the compression result.

        for i, char in enumerate(string):
            if i == len(string) - 1:  # End of string.
                if compress_char != char:
                    result += '%s%d' % (compress_char, compress_count)
                    result += '%s1' % char
                else:
                    result += '%s%d' % (compress_char, compress_count + 1)
            elif compress_char != char:
                if compress_count > 0:
                    result += '%s%d' % (compress_char, compress_count)
                compress_char = char
                compress_count = 1
            else:
                compress_count += 1

        return result if len(result) < len(string) else string

    @staticmethod
    def rotate_matrix():
        """
        Question 1.7
        Given an image represented by an NxN matrix, where each pixel in the image is 4
        bytes, write a method to rotate the image by 90 degrees. (an you do this in place?
        :return: Image rotated by 90 degrees.
        """

    @staticmethod
    def zero_matrix(matrix: List(list)):
        """
        Question 1.8
        Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
        column are set to 0.
        :return: Matrix that has been operated on.
        """

    @staticmethod
    def string_rotation():
        """
        Question 1.9
        Assume you have a method isSubstring which checks if one word is a substring of another.
        Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
        call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
        :return:
        """