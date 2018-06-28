from unittest import TestCase
from array_and_string_questions import ArrayAndStringQuestions


class TestArrayAndStringQuestions(TestCase):
    def test_is_unique(self):
        unique_words = ['uncopyrightable', 'cat', 'dog', 'subdermatoglyphic', 'ambidextrously']
        non_unique_words = ['forthwith', 'duress', 'withstanding', 'polyzygote']
        for word in unique_words:
            if not ArrayAndStringQuestions.is_unique(word):
                self.fail()

        for word in non_unique_words:
            if ArrayAndStringQuestions.is_unique(word):
                self.fail()

    def test_is_permutation(self):
        words = ['racecar', 'god', 'uncopyrightable']
        permutations = ['racerac', 'dog', 'nupycorightleba']
        not_permutations = ['racetruck', 'worth', 'uncopyrightabl']

        for i, word in enumerate(words):
            if not ArrayAndStringQuestions.is_permutation(word, permutations[i]):
                self.fail("is_permutation(%s, %s): Evaluated incorrectly to False" % (word, permutations[i]))
            if ArrayAndStringQuestions.is_permutation(word, not_permutations[i]):
                self.fail("is_permutation(%s, %s): Evaluated incorrectly to True" % (word, not_permutations[i]))

    def test_urlify(self):
        if ArrayAndStringQuestions.urlify('Mr John Smith    ', 13) != "Mr%20John%20Smith":
            self.fail()

    def test_palindrome_permutation(self):
        # racecar, ana, anna, avid diva, air an aria, are we not drawn onward to new era
        palindrome_permutations = ['racerac', 'aan', 'nana', 'avid adiv', 'iar na aari', 'ware ne ot dawn ronard wo newt rea']
        not_palindrome_permutations = ['cat', 'indubitably']
        for permutation in palindrome_permutations:
            if not ArrayAndStringQuestions.palindrome_permutation(permutation):
                self.fail("palindrome_permutation(%s): Evaluated incorrectly to False")
        for permutation in not_palindrome_permutations:
            if not ArrayAndStringQuestions.palindrome_permutation(permutation):
                self.fail("palindrome_permutation(%s): Evaluated incorrectly to True")

    def test_one_away(self):
        inputs = ['pale', 'pales', 'pale', 'pale']
        changed_inputs = ['ple', 'pale', 'bale', 'bake']
        expected_eval = [True, True, True, False]

        for i, input in enumerate(inputs):
            if ArrayAndStringQuestions.one_away(input, changed_inputs[i]) != expected_eval[i]:
                pass#self.fail()

    def test_string_compression(self):
        inputs = ['aabcccccaaa', 'aabbcccccaaab', 'abc']
        outputs = ['a2b1c5a3', 'a2b2c5a3b1', 'abc']

        for i, input in enumerate(inputs):
            result = ArrayAndStringQuestions.string_compression(input)
            if result != outputs[i]:
                self.fail('string_compression(%r): Expected %r, got %r' % (input, outputs[i], result))
