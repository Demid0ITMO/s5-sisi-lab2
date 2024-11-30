import unittest

from main import *


class Test(unittest.TestCase):
    def test_parse_input(self):
        inputs = [
            'Стоп',
            'СТОП',
            '',
            'аааа',
            'поМОщь',
            'Я хочу поиграть в ЖАНР игру',
            'в какие игры я могу поиграть на ПЛАТФОРМА'
        ]
        outputs = [
            [0, {}],
            [0, {}],
            [-1, {}],
            [-1, {}],
            [1, {}],
            [2, {'type_id': 0, 'input': 'жанр'}],
            [2, {'type_id': 1, 'input': 'платформа'}],
        ]
        for i in range(len(inputs)):
            parsed = parse_input(inputs[i])
            self.assertEqual(parsed[0], outputs[i][0])
            self.assertEqual(parsed[1].get('type_id'), outputs[i][1].get('type_id'))
            self.assertEqual(parsed[1].get('input'), outputs[i][1].get('input'))


if __name__ == '__main__':
    unittest.main()
