import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.libiary import Library


class TestLibrary(unittest.TestCase):
    borrow_info_status = 200

    def setUp(self):
        try:
            borrow_info_status = urllib.request.urlopen(
                url=Library.URLs.BORROW_INFO, timeout=5).code
        except URLError:
            borrow_info_status = -1

    @unittest.skipIf(borrow_info_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_borrow_info(self):
        result = Library.get_borrow_info()
        self.assertTrue(result['success'])
        self.assertEqual(result['msg'], '查询成功')
        self.assertIsInstance(result['result'], list)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLibrary)
    unittest.TextTestRunner().run(suite)
