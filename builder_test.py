import unittest
from your_module import *


class BuilderTest(unittest.TestCase):

    def test_build_minimal_viable_product(self):
        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder

        director.build_minimal_viable_product()
        product = builder.product

        # Verify that the product is an instance of Product1
        self.assertIsInstance(product, Product1)

        # Verify that the product contains the expected parts
        self.assertEqual(product.parts, ["PartA1"])

    def test_build_full_featured_product(self):
        director = Director()
        builder = ConcreteBuilder1()
        director.builder = builder

        director.build_full_featured_product()
        product = builder.product

        # Verify that the product is an instance of Product1
        self.assertIsInstance(product, Product1)

        # Verify that the product contains the expected parts
        self.assertEqual(product.parts, ["PartA1", "PartB1", "PartC1"])

    def test_custom_product(self):
        builder = ConcreteBuilder1()

        builder.produce_part_a()
        builder.produce_part_b()
        product = builder.product

        # Verify that the product is an instance of Product1
        self.assertIsInstance(product, Product1)

        # Verify that the product contains the expected parts
        self.assertEqual(product.parts, ["PartA1", "PartB1"])


if __name__ == "__main__":
    unittest.main()
