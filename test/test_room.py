import unittest
import urllib.request
from urllib.error import URLError

import snnusdk.room as room
from snnusdk.exceptions import (BuildingNotFoundError,
                                DepartmentNotSupportedError, RoomNotFoundError)
from snnusdk.room import Room


class TestRoom(unittest.TestCase):
    Rooms_status = 200
    @classmethod
    def setUpClass(cls):
        try:
            Rooms_status = urllib.request.urlopen(
                url=room.host, timeout=5).code
        except URLError:
            Rooms_status = -1
        except Exception:
            Rooms_status = -1

    @unittest.expectedFailure
    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_query_all(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.query_all()
        self.assertIsInstance(test_result, list)

        test = Room(3, 'xxxxx')
        self.assertRaises(BuildingNotFoundError, test.query_all)

    @unittest.expectedFailure
    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_get_all_room(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.get_all_rooms()
        self.assertIsInstance(test_result, list)

    @unittest.expectedFailure
    @unittest.skipIf(Rooms_status != 200, "状态码不等于200，就跳过该测试")
    def test_query_one_room(self):
        test = Room(3, '雁塔教学八楼')
        test_result = test.query_one_room('8101')
        self.assertIsInstance(test_result, dict)
        self.assertRaises(RoomNotFoundError, test.query_one_room, '8104')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestRoom)
    unittest.TextTestRunner().run(suite)
