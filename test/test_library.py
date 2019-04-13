import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.libiary import Library
from snnusdk.exceptions import AuthenticationError, UnauthorizedError


class TestLibrary(unittest.TestCase):
    borrow_info_status = 200
    library_status = 200

    @classmethod
    def setUpClass(cls):
        try:
            borrow_info_status = urllib.request.urlopen(
                url=Library.URLs.BORROW_INFO, timeout=5).code
        except URLError:
            borrow_info_status = -1
        try:
            library_status = urllib.request.urlopen(
                url=Library.URLs.HOST, timeout=5).code
        except URLError:
            library_status = -1

    @unittest.skipIf(borrow_info_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_borrow_info(self):
        result = Library.get_borrow_info()
        self.assertTrue(result['success'])
        self.assertIsInstance(result['result'], list)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_login(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(AuthenticationError, test_user.login)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_info(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.get_info)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_borrowing_books(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.get_borrowing_books)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_reservation_books(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.get_reservation_books)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_cash(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.get_cash)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_lock_lib_card(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.lock_lib_card)

    @unittest.skipIf(library_status != 200, "状态码不等于200，就跳过该测试")
    def test_unlock_lib_card(self):
        test_user = Library(username='xxxx', password='xxx')
        self.assertRaises(UnauthorizedError, test_user.unlock_lib_card)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLibrary)
    unittest.TextTestRunner().run(suite)
