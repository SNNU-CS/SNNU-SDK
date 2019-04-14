import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.campus import Campus


class TestCampus(unittest.TestCase):
    consumption_status = 200
    photo_status = 200

    def setUp(self):
        try:
            consumption_status = urllib.request.urlopen(
                url=Campus.URLs.CONSUMPTION, timeout=5).code
        except URLError:
            consumption_status = -1

    @unittest.skipIf(consumption_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_list_1(self):
        test = Campus('201608735')
        test_result = test.get_list()
        self.assertIsInstance(test_result, dict)
        self.assertTrue(test_result['success'])
        self.assertEqual(test_result['msg'], '查询成功')
        self.assertIsInstance(test_result['result'], list)

        test = Campus('xxxxxx')
        test_result = test.get_list()
        self.assertIsInstance(test_result, dict)
        self.assertFalse(test_result['success'])
        self.assertEqual(test_result['msg'], '请核对校园卡号')
        self.assertListEqual(test_result['result'], [])

    @unittest.skipIf(consumption_status == 200, "状态码等于200，就跳过该测试")
    def test_get_list_2(self):
        test = Campus('201608735')
        test_result = test.get_list()
        self.assertIsInstance(test_result, dict)
        self.assertTrue(test_result['success'])
        self.assertEqual(test_result['msg'], '网络连接失败')
        self.assertIsInstance(test_result['result', list])
        self.assertListEqual(test_result['result'], [])

    @unittest.skipIf(consumption_status == 200, "状态码等于200，就跳过该测试")
    def test_get_photo_1(self):
        test = Campus('201608735')
        test_result = test.get_photo()
        self.assertIsInstance(test_result, dict)
        self.assertEqual(test_result['msg'], '网络连接失败')
        self.assertTrue(test_result['success'])
        self.assertIsInstance(test_result['data'], bytes)

    @unittest.skipIf(consumption_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_photo_2(self):
        test = Campus('201608714')
        test_result = test.get_photo()
        self.assertIsInstance(test_result, dict)
        self.assertEqual(test_result['msg'], '获取成功')
        self.assertTrue(test_result['success'], False)

        test = Campus('xxxxxx')
        test_result = test.get_photo()
        self.assertIsInstance(test_result, dict)
        self.assertEqual(test_result['msg'], '获取成功')
        self.assertTrue(test_result['success'], False)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCampus)
    unittest.TextTestRunner().run(suite)
