import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.exceptions import DepartmentNotSupportedError
from snnusdk.message import News
from snnusdk.configs import SPIDER_CONFIG as links

class TestNews(unittest.TestCase):
    code_status = 200

    def setUp(self):
        try:
            for link in links:
                code_status = urllib.request.urlopen(url=link['url'], timeout=5).code
                if code_status != 200:
                    return
        except URLError:
            code_status = -1

    @unittest.skipIf(code_status != 200, "状态码不是200,就跳过改测试")
    def test_get_count(self):
        pass

    @unittest.skipIf(code_status != 200, "状态码不是200,就跳过该测试")
    def test_get_news(self):
        test = News(dep='计算机科学学院')
        test_result = test.get_news()
        self.assertIsInstance(test_result, list)

        test = News(dep='xxx')
        with self.assertRaises(DepartmentNotSupportedError):
            test_result = test.get_news()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestNews)
    unittest.TextTestRunner().run(suite)
