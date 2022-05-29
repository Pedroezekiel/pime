import unittest
from calculate import Calculate


class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(5, self.calc.add(3, 2))

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.calc = Calculate()
        self.assertRaises(TypeError, self.calc.add, "hello", "world")


if __name__ == "__main__":
    unittest.main()
