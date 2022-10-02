import unittest
from . import shopping


class TestShopping(unittest.TestCase):
    def test_that_we_have_a_shopping_cart(self):
        shop1 = shopping.ShoppingCart(2)
        self.assertIsNotNone(shop1)

    def test_that_shopping_cart_have_a_len(self):
        shop1 = shopping.ShoppingCart(2)
        self.assertEqual(2, shop1.limit)

    def test_that_we_can_have_items_in_the_shopping_cart(self):
        shop1 = shopping.ShoppingCart(2)
        self.assertEqual([], shop1.item)

    def test_that_we_can_add_items_to_the_shopping_cart(self):
        shop1 = shopping.ShoppingCart(2)
        shop1.add_item("bread")
        shop1.add_item("butter")
        self.assertEqual(["bread", "butter"], shop1.item)

    def test_that_the_shopping_cart_will_not_be_more_than_limit(self):
        shop1 = shopping.ShoppingCart(2)
        shop1.add_item("bread")
        shop1.add_item("butter")
        shop1.add_item("milk")
        self.assertEqual(["milk", "butter"], shop1.item)
