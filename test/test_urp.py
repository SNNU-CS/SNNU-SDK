import unittest
import urllib.request
from urllib.error import URLError

from snnusdk.urp import Urp

from snnusdk.exceptions import AuthenticationError, UnauthorizedError, YearNotExistError

class TestUrp(unittest.TestCase):
    Urp_status = 200
    SelectedCourses_status = 200
    OldCourses_status = 200

    def setUp(self):
        try:
            Urp_status = urllib.request.urlopen(
                url=Urp.URLs.HOST, timeout=5).code
        except URLError:
            Urp_status = -1

        try:
            Urp_status = urllib.request.urlopen(
                url=Urp.URLs.SELECTED_COURSES, timeout=5).code
        except URLError:
            Urp_status = -1

        try:
            Urp_status = urllib.request.urlopen(
                url=Urp.URLs.OLD_COURSES, timeout=5).code
        except URLError:
            Urp_status = -1

    @unittest.skipIf(Urp_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_course(self):
        test = Urp('41612123', 'jjy19980415')
        test_result = test.get_courses()
        self.assertIsInstance(test_result , list)

        test = Urp('xxx', 'xxx')
        with self.assertRaises(UnauthorizedError):
            test.get_courses()





