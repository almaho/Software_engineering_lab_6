import unittest
from abc import ABC, abstractmethod
from your_module import *


class AbstractFactoryTest(unittest.TestCase):

    def test_abstract_factory(self):
        factory1 = ConcreteFactory1()
        factory2 = ConcreteFactory2()

        productA1 = factory1.create_product_a()
        productB1 = factory1.create_product_b()

        productA2 = factory2.create_product_a()
        productB2 = factory2.create_product_b()

        # Test ConcreteProductA1
        self.assertEqual("The result of the product A1.", productA1.useful_function_a())

        # Test ConcreteProductB1
        self.assertEqual("The result of the product B1.", productB1.useful_function_b())
        self.assertEqual("The result of the B1 collaborating with the (The result of the product A1.)", productB1.another_useful_function_b(productA1))

        # Test ConcreteProductA2
        self.assertEqual("The result of the product A2.", productA2.useful_function_a())

        # Test ConcreteProductB2
        self.assertEqual("The result of the product B2.", productB2.useful_function_b())
        self.assertEqual("The result of the B2 collaborating with the (The result of the product A2.)", productB2.another_useful_function_b(productA2))


if __name__ == '__main__':
    unittest.main()
