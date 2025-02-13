# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class LegendaryItem(Item):

    def update(self):
        self.update_sell_in()

    def update_sell_in(self):
        self.sell_in -= 1


class GildedItem(Item):

    def update(self):
        self.update_sell_in()
        self.update_quality()

    def update_sell_in(self):
        self.sell_in -= 1

    def update_quality(self):
        if self.sell_in < 0:
            self.quality -= 2
        else:
            self.quality -= 1

        if self.quality < 0:
            self.quality = 0


class NormalItem(GildedItem):
    pass


class AgedBrie(GildedItem):

    def update_quality(self):
        if self.sell_in < 0:
            self.quality += 2
        else:
            self.quality += 1

        if self.quality > 50:
            self.quality = 50


class BackstagePass(GildedItem):

    def update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in < 5:
            self.quality += 3
            if self.quality > 50:
                self.quality = 50
        elif self.sell_in < 10:
            self.quality += 2
            if self.quality > 50:
                self.quality = 50
        else:
            self.quality += 1
            if self.quality > 50:
                self.quality = 50


class Sulfuras(LegendaryItem):

    def update_quality(self):
        pass


class Conjured(GildedItem):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)
        self.isConjured = True

    def update_quality(self):
        if self.sell_in < 0:
            self.quality -= 4
        else:
            self.quality -= 2

        if self.quality < 0:
            self.quality = 0


class GildedRose:
    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()

    def get_items(self):
        return [item.name for item in self.items]
