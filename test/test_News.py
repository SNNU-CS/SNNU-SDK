import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.exceptions import DepartmentNotSupportedError
from snnusdk.message import News
from snnusdk.configs import SPIDER_CONFIG as links


class TestNews(unittest.TestCase):
    code_status = dict(zip(list(set([i['department_CN'] for i in links])), [
                       200 for _ in range(int(len(links)/2))]))

    def setUp(self):
        for link in links:
            if link['type'] is '新闻':
                dep = link['department_CN']
                try:
                    code_status[dep] = urllib.request.urlopen(
                        url=link['url'], timeout=5).code
                except URLError:
                    code_status[dep] = -1

    def test_get_count(self):
        test = News(dep='计算机科学学院')
        test_result = test.get_count()
        self.assertEqual(test_result, 0)
        test_result = test.get_news()
        self.assertIsInstance(test_result, list)

    def test_get_news(self):
        for link in links:
            if link['type'] is '新闻' and code_status[link['department_CN']] is 200:
                test = News(link['department_CN'])
                test_result = test.get_news()
                self.assertIsInstance(test_result, list)
                self.assertGreater(len(test_ressult), 0)

        test = News(dep='xxx')
        self.assertRaises(DepartmentNotSupportedError, test.get_news)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestNews)
    unittest.TextTestRunner().run(suite)
