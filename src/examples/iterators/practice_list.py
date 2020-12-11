import unittest

class ListTestCase(unittest.TestCase):
    """Set up a group of tests"""
    # These tests will see just how good you are with Lists. You can see some supporting material here if you
    # think you'll need it https://docs.python.org/3/tutorial/datastructures.html

    def test_sort_list_in_reverse_alphabetical_order(self):
        """Take the list below and return it in alphabetical order"""
        yak_breeds = ["Jiulong yak", "Sibu yak", "Huanhu yak", "Plateau yak", "Jiali yak"]

        sorted_list = [] #Make this value have the list in alphabetical order

        self.assertEqual(sorted_list, ["Sibu yak", "Plateau yak", "Jiulong yak",  "Jiali yak", "Huanhu yak"])

    def test_get_tenth_from_last_item(self):
        """Go through the list and return the item that is tenth from the last"""

        long_list = ["Jame", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William",
                     "Elizable", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica", "Thomas", "Sarah",
                     "Charles", "Karen", "Christopher", "Nancy"]

        tenth_from_last = "?" #make this return the 10th item from the last in the list

        self.assertEqual("Richard", tenth_from_last)

    def test_remove_words_longer_than_four_letters(self):
        """Go through the list and remove any word that has more than 4 letters"""

        original_list = ['apple', 'apple', 'pear', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
        better_list = [] # make this list only have words that have 4 letters or less

        self.assertEqual(['pear', 'kiwi', 'pear'], better_list)

    def test_combine_two_lists(self):
        """Combine the two lists and return the 3rd, 4th and 5th largest numbers"""

        first_list = [1, 3, 5, 67, 98, 13, 35, 36]
        second_list = [35, 3263, 20, 15, 10, 158]

        third_fourth_fifth_largest = [] #make this list have the 3rd, 4th, and 5th largest across both lists

        self.assertEqual([98, 67, 36], third_fourth_fifth_largest)

    def test_find_the_most_common_pet(self):
        """Return the single word that occurs the most in the list"""
        word_list = ['cat', 'dog', 'cat', 'hamster', 'cat', 'dog', 'dog', 'dog', 'cat', 'parrot', 'dog', 'cat',
                     'hamster', 'parrot', 'hamster', 'goldfish', 'dog', 'dog', 'goldfish', 'monkey', 'camel', 'yak',
                     'cat', 'parrot', 'hamster', 'hamster', 'goldfish', 'monkey', 'shark', 'yak', 'yak', 'yak',
                     'parrot', 'dog', 'parrot', 'monkey', 'scorpion', 'shark', 'dog', 'goldfish', 'goldfish', 'cat']

        most_common_pet = "?" # set this variable according to the single animal that shows up most often in the list

        self.assertEqual('dog', most_common_pet)


if __name__ == '__main__':
    unittest.main()