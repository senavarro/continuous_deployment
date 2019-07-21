"""

Unit test for the calculator library

"""

import calculator


class TestCalculator:

	def test_addition(self):
		assert 4 == calculator.add(2,2)

	def test_substraction(self):
		assert 2 == calculator.substract(4,2)

	def test_multiplication(self):
		assert 4 == calculator.multiply(6,2)

	def test_substraction(self):
		assert 2 == calculator.divide(8,2)
