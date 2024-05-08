import unittest

from .task1 import discriminant, solution
from .task2 import vote
from .task3 import get_name, get_directory, add, documents, directories


class Task1Test(unittest.TestCase):
    def test_discriminant(self):
        test_cases = [
            # Положительные коэффициенты
            (1, 5, 6, 1),
            (2, 4, 2, 0),
            (1, 2, 1, 0),
            # Отрицательные коэффициенты
            (-1, -5, -6, 1),
            (-2, -4, -2, 0),
            (-1, -2, -1, 0),
            # Нулевые коэффициенты
            (0, 5, 6, 25),
            (1, 0, 6, -24),
            (1, 5, 0, 25),
            # Дискриминант отрицателен
            (1, 2, 3, -8),
            (2, 4, 7, -40),
            (3, 6, 9, -72),
        ]

        for num, (a, b, c, expected) in enumerate(test_cases):
            with self.subTest(num):
                actual = discriminant(a, b, c)
                self.assertEqual(expected, actual)

    def test_solution(self):
        test_cases = [
            ((1, 8, 15), (-3.0, -5.0)),
            ((1, -13, 12), (12.0, 1.0)),
            ((-4, 28, -49), 3.5),
            ((1, 1, 1), "корней нет")
        ]

        for num, (input_values, expected_output) in enumerate(test_cases):
            with self.subTest(num):
                self.assertEqual(solution(*input_values), expected_output)


class Task2Test(unittest.TestCase):
    def test_vote_equal(self):
        test_cases = [
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
            ([1], 1),
            ([], 0),
            ([2, 2, 2, 2, 2], 2)
        ]
        for num, (input_list, expected_output) in enumerate(test_cases):
            with self.subTest(num):
                self.assertEqual(vote(input_list), expected_output)


class Task3Test(unittest.TestCase):
    def test_get_name_existing_document(self):
        self.assertEqual(get_name("10006"), "Аристарх Павлов")

    def test_get_name_nonexistent_document(self):
        self.assertEqual(get_name("101"), "Документ не найден")

    def test_get_directory_existing_document(self):
        self.assertEqual(get_directory("11-2"), "1")

    def test_get_directory_nonexistent_document(self):
        self.assertEqual(get_directory("101"), "Полки с таким документом не найдено")

    def test_add_document(self):
        add('international passport', '311 020203', 'Александр Пушкин', '3')
        self.assertIn({'type': 'international passport', 'number': '311 020203', 'name': 'Александр Пушкин'}, documents)
        self.assertIn('311 020203', directories['3'])
