# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, Conjured, Sulfuras


class GildedRoseTest(unittest.TestCase):

    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Sulfuras("Sulfuras", 5, 80)]
        sulfuras_item = items[0]
        sulfuras_item.update()
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Sulfuras("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_items()
        self.assertEqual(["Sulfuras"], all_items)

    # test that sulfuras should decrease sell_in (logical)
    def test_sulfuras_should_decrease_sell_in(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros", 5, 50)]
        sulfuras_item = items[0]
        sulfuras_item.update()
        self.assertEqual(4, sulfuras_item.sell_in)

    # item quality should never be more than 50 (logical)
    def test_item_quality_not_over_50(self):
        quality = 50
        items = [Item("item", 30, quality)]
        item = items[0]
        maxQuality = 50
        self.assertGreaterEqual(maxQuality, item.quality)

    # conjured item should degrade twice as fast (logical)
    def test_conjured_item_should_degrade_quality_twice_as_fast(self):
        quality = 80
        items = [Conjured("Conjured Item", 5, quality)]
        conjured_item = items[0]
        conjured_item.update()
        normal_degradation_rate = 1
        self.assertEqual(quality - (normal_degradation_rate * 2), conjured_item.quality)

    # conjured item does not exist (syntax error)
    def test_conjured_item(self):
        items = [Conjured("Conjured Item", 5, 80)]
        conjured_item = items[0]
        self.assertEqual(True, conjured_item.isConjured)


if __name__ == '__main__':
    unittest.main()
