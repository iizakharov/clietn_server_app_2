import sys
sys.path.append('../')
import unittest
from client import create_presence, process_answer
from config.dict import *
from config.errors import ReqFieldMissingError, ServerError


# Класс с тестами
class TestClass(unittest.TestCase):
    # тест коректного запроса
    def test_def_presense(self):
        test = create_presence('Guest')
        test[TIME] = 1.1  # время необходимо приравнять принудительно иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    # тест корректтного разбора ответа 200
    def test_200_ans(self):
        self.assertEqual(process_answer({RESPONSE: 200}), '200 : OK')

    # тест корректного разбора 400
    def test_400_ans(self):
        self.assertRaises(ServerError, process_answer, {RESPONSE: 400, ERROR: 'Bad Request'})

    # тест исключения без поля RESPONSE
    def test_no_response(self):
        self.assertRaises(ReqFieldMissingError, process_answer, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
