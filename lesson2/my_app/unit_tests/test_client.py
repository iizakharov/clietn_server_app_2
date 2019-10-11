import unittest
from client import create_presence, process_answer
from config.dict import *
from errors import ReqFieldMissingError


class TestClient(unittest.TestCase):
    response_ok = '200 : OK'
    bad_response = '400 : Bad Request'

    def test_correct_presence(self):
        defer = create_presence()
        defer[TIME] = 2.995  # присвоение обязательно из-за рандомного времени
        self.assertEqual(defer, {ACTION: PRESENCE, TIME: 2.995, USER: {ACCOUNT_NAME: 'User'}})

    def test_response_200(self):
        self.assertEqual(process_answer({RESPONSE: 200}), self.response_ok)

    def test_response_400(self):
        self.assertEqual(process_answer({RESPONSE: 400, ERROR: 'Bad Request'}), self.bad_response)

    def test_err_msg(self):
        msg= 'testtest'
        self.assertRaises(ReqFieldMissingError, process_answer, msg)


if __name__ == '__main__':
    unittest.main()
