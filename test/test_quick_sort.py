import unittest
import utils.sort as sort
import random

class TestQuickSort(unittest.TestCase):

    def test_quick_sort_conjunto_vacio(self):
        input_data = []
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_un_elemento(self):
        input_data = [42]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_orden_ascendente(self):
        input_data = [1, 2, 3, 4, 5]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_orden_descendente(self):
        input_data = [5, 4, 3, 2, 1]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_aleatorio(self):
        input_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_gran_conjunto_aleatorio(self):
        input_data = [random.randint(1, 1000000000) for _ in range(100000)]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

    def test_quick_sort_con_duplicados(self):
        input_data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.assertEqual(sort.quick_sort(input_data), sorted(input_data))

if __name__ == '__main__':
    unittest.main()