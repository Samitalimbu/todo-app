import unittest
import dbhandler as db


class MyTestCase(unittest.TestCase):

    def test_login(self):
        self.assertEqual(1, db.login("Samita", "samita1"))

    def test_register(self):
        self.assertEqual(1, db.register("Test User", "testuser", "B+", "25", "samita1"))

    def test_add_task(self):
        self.assertEqual(1, db.add_task("Task Title", "Category", "This is a description",
                                        1, "1"))

    def test_delete_task(self):
        self.assertEqual(True, db.delete_task("1"))


if __name__ == '__main__':
    unittest.main()
