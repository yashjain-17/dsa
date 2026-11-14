import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_example(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


borrowing = load_example("1.py", "borrowing_example")
searching = load_example("3.py", "searching_example")
sorting = load_example("4.py", "sorting_example")
hashing = load_example("5.py", "hashing_example")


class DSAExamplesTests(unittest.TestCase):
    def test_average_and_empty_input(self):
        self.assertEqual(borrowing.average([2, 0, 2, 1, 0]), 1)
        with self.assertRaises(ValueError):
            borrowing.average([])

    def test_mode_tie_uses_first_occurrence(self):
        self.assertEqual(borrowing.mode([4, 2, 4, 2]), 4)
        self.assertIsNone(borrowing.mode([]))

    def test_search_algorithms(self):
        values = [10, 20, 30, 40, 50]
        self.assertEqual(searching.linear_search(values, 30), 2)
        self.assertEqual(searching.binary_search(values, 30), 2)
        self.assertEqual(searching.binary_search(values, 99), -1)

    def test_sorts_return_sorted_copy(self):
        values = [4, 1, 3, 2]
        self.assertEqual(sorting.selection_sort(values), [1, 2, 3, 4])
        self.assertEqual(sorting.bubble_sort(values), [1, 2, 3, 4])
        self.assertEqual(values, [4, 1, 3, 2])

    def test_hash_table_collision_update_and_delete(self):
        for bucket in hashing.table:
            bucket.clear()
        hashing.insert(10, "A")
        hashing.insert(20, "B")
        hashing.insert(10, "Updated")
        self.assertEqual(hashing.search(10), "Updated")
        self.assertEqual(hashing.search(20), "B")
        self.assertTrue(hashing.delete(10))
        self.assertIsNone(hashing.search(10))


if __name__ == "__main__":
    unittest.main()
