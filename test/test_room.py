import unittest
import urllib.request
from urllib.error import URLError

import snnusdk.room as room
from snnusdk.room import Room

from snnusdk.exceptions import RoomNotFoundError

class TestRoom(unittest.TestCase):
    Rooms_status = 200

    def setUp(self):
        try:
            consumption_status = urllib.request.urlopen(
                url=room.host, timeout=5).code
        except URLError:
            consumption_status = -1

    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_query_all(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.query_all()
        self.assertIsInstance(test_result, list)

    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_all_room(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.get_all_rooms()
        self.assertIsInstance(test_result, list)

    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_query_one_room(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.query_one_room('8101')
        self.assertIsInstance(test_result, dict)
        with self.assertRaises(RoomNotFoundError):
            test.query_one_room('8014')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRoom)
    unittest.TextTestRunner().run(suite)