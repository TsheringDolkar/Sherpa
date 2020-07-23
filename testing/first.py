import unittest
from testing.new import Operations
from classes.Item import *
from classes.Order import*


class MyTest(unittest.TestCase):
    item = Item()
    order=Order()

    def test_add_item(self):
        result = self.item.add_item('test_item', 'test_type', 100)
        self.assertTrue(result)

    def test_add_item_view(self):
        result = self.item.add_item('', '', 100)
        self.assertFalse(result)

    def test_add_item_view_1(self):
        result = self.item.add_item('test', 'type', 'asd')
        self.assertFalse(result)

    def test_add_item_view_2(self):
        result = self.item.add_item('', '', -100)
        self.assertFalse(result)

    def test_show_items(self):
        data = self.item.show_item()
        actual_result = len(data)
        expected_result = 9
        self.assertEqual(expected_result, actual_result)

    def test_search_item(self):
        data = self.item.search_item('momo')
        actual_result = len(data)
        expected_result = 2
        self.assertEqual(expected_result, actual_result)

    def test_search_items1(self):
        data = self.item.search_item('noodle')
        actual_result = len(data)
        expected_result = 0
        self.assertEqual(expected_result, actual_result)

    def test_update_item(self):
        result=self.item.update_item(5,"Masu", "veg", 600)
        self.assertTrue(result)

    def test_delete_item(self):
        result=self.item.delete_item(5)
        self.assertTrue(result)

    def test_delete_item_1(self):
        result=self.item.delete_item("aa")
        self.assertFalse(result)

    def test_add_order(self):
        result=self.order.add_order(5,("burger","chicken","150") )
        self.assertTrue(result)

