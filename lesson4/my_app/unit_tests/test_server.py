import unittest
from server import process_client_message
from config.dict import *


class TestServer(unittest.TestCase):  # {ACTION: PRESENCE, TIME: 2.995, USER: {ACCOUNT_NAME: 'User'}}
    err_massage = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    msg_ok = {RESPONSE: 200}

    def test_no_user_name(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 2.995}), self.err_massage)

    def test_not_correct_name(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 2.995, USER: {ACCOUNT_NAME: 'Guest'}}),
                         self.err_massage)

    def test_no_time(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'User'}}), self.err_massage)

    def test_no_action(self):
        self.assertEqual(process_client_message({TIME: 2.995, USER: {ACCOUNT_NAME: 'User'}}), self.err_massage)

    def test_msg_ok(self):
        self.assertEqual(process_client_message({ACTION: PRESENCE, TIME: 2.995, USER: {ACCOUNT_NAME: 'User'}}),
                         self.msg_ok)

    def test_empty_msg(self):
        msg = {}
        self.assertEqual(process_client_message(msg), self.err_massage)


if __name__ == '__main__':
    unittest.main()
