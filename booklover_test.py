import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        test1 = BookLover("Chloe Merriweather", "chloem@outlook.com", "fiction")
        test1.add_book("Allegedly", 5)
        self.assertIn("Allegedly", test1.book_list['book_name'].values)

    def test_2_add_book(self):
        bl = BookLover("Sydney Merriweather", "sydm@outlook.com", "fiction")
        bl.add_book("Take my Hand", 5)
        bl.add_book("Take my Hand", 4)
        self.assertEqual(bl.book_list['book_name'].tolist().count("Take my Hand"),1)

    def test_3_has_read(self):
        bl = BookLover("Chanel", "chanel@outlook.com", "romance")
        bl.add_book("Reel", 5)
        self.assertTrue(bl.has_read("Reel"))

    def test_4_has_read(self):
        bl = BookLover("Mary", "mary@outlook.com", "fantasy")
        bl.add_book("the Hobbit",3)
        self.assertFalse(bl.has_read("Harry Potter"))

    def test_5_num_books_read(self):
        bl = BookLover("Jason", "jason@outlook.com", "sci-fi")
        bl.add_book("Dune", 5)
        bl.add_book("1984", 4)
        bl.add_book("Dune 2", 3)
        self.assertEqual(bl.num_books_read(), 3)

    def test_6_fav_books(self):
        bl = BookLover("Sheridan", "sheridan@outlook.com", "fiction")
        bl.add_book("688", 5)
        bl.add_book("The Boy in the Striped Pajamas", 4)
        bl.add_book("The White Tiger", 3)
        fav_books = bl.fav_books()
        self.assertTrue(all(rating>3 for rating in fav_books ['book_rating']))
        self.assertEqual(fav_books['book_name'].tolist(), ["688", "The Boy in the Striped Pajamas"])

if __name__ == '__main__':
    unittest.main(verbosity=3)