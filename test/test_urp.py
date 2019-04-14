import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.urp import Urp

from snnusdk.exceptions import AuthenticationError, UnauthorizedError, YearNotExistError


class TestUrp(unittest.TestCase):
    Urp_status = 200

    def setUp(self):
        try:
            Urp_status = urllib.request.urlopen(
                url=Urp.URLs.HOST, timeout=5).code
        except URLError:
            Urp_status = -1

    @unittest.skipIf(Urp_status != 200, "状态码不等于200，就跳过该测试")
    def test_login(self):
        test = Urp('xxx', 'xxx')
        self.assertRaises(AuthenticationError, test.login)

    @unittest.skipIf(Urp_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_gpa(self):
        test = Urp('xxx', 'xxx')
        self.assertRaises(UnauthorizedError, test.get_gpa)
