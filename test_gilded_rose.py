# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # test that sulfuras should decrease sell_in (logical)
    def test_sulfuras_should_decrease_sell_in(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(4, sulfuras_item.sell_in)

    # item quality should never be more than 50 (logical)
    def test_item_quality_not_over_50(self):
        items = [Item("item", 30, 80)]
        item = items[0]
        maxQuality = 50
        self.assertGreaterEqual(maxQuality, item.quality)

    # conjured item should degrade twice as fast (logical)
    def test_conjured_item_should_degrade_quality_twice_as_fast(self):
        items = [Item("Conjured Item", 5, 80)]
        conjured_item = items[0]
        conjured_item.update_quality()
        normal_degradation_rate = 1
        self.assertEqual(normal_degradation_rate * 2, conjured_item.quality)

    # conjured item does not exist (syntax error)
    def test_conjured_item(self):
        items = [Item("Conjured Item", 5, 80)]
        conjured_item = items[0]
        self.assertEqual(True, conjured_item.isConjured)


if __name__ == '__main__':
    unittest.main()
