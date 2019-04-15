import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.message import Notice
from snnusdk.configs import SPIDER_CONFIG as links
from snnusdk.exceptions import DepartmentNotSupportedError


class TestNotice(unittest.TestCase):
    code_status = dict(zip(list(set([i['department_CN'] for i in links])), [
                       200 for _ in range(int(len(links)/2))]))

    @classmethod
    def setUpClass(cls):
        for link in links:
            if link['type'] is '通知':
                dep = link['department_CN']
                try:
                    code_status[dep] = urllib.request.urlopen(
                        url=link['url'], timeout=5).code
                except URLError:
                    code_status[dep] = -1

    def test_get_count(self):
        test = Notice(dep='计算机科学学院')
        test_result = test.get_count()
        self.assertEqual(test_result, 0)
        test_result = test.get_notice()
        self.assertIsInstance(test_result, list)

    def test_get_notice(self):
        for link in links:
            if link['type'] is '通知' and code_status[link['department_CN']] is 200:
                test = Notice(link['department_CN'])
                test_result = test.get_notice()
                self.assertIsInstance(test_result, list)
                self.assertGreater(len(test_ressult), 0)

        test = Notice(dep='xxx')
        with self.assertRaises(DepartmentNotSupportedError):
            test_result = test.get_notice()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestNotice)
    unittest.TextTestRunner().run(suite)
