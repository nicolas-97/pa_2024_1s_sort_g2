import unittest
import utils1.sort as sort
import random

class TestShellSort(unittest.TestCase):

    def test_shell_sort_conjunto_vacio(self):
        input_data = []
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_un_elemento(self):
        input_data = [42]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_orden_ascendente(self):
        input_data = [1, 2, 3, 4, 5]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_orden_descendente(self):
        input_data = [5, 4, 3, 2, 1]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_aleatorio(self):
        input_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_gran_conjunto_aleatorio(self):
        input_data = [random.randint(1, 1000000) for _ in range(1000)]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))

    def test_shell_sort_con_duplicados(self):
        input_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(sort.shell_sort(input_data), sorted(input_data))


    if __name__ == '__main__':
        unittest.main()