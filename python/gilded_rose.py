# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        passes_backstage="Backstage passes to a TAFKAL80ETC concert"
        sulfuras="Sulfuras, Hand of Ragnaros"
        for item in self.items:
            if item.name != "Aged Brie" and item.name != passes_backstage:
                if item.quality > 0 and item.name != sulfuras:
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == passes_backstage:
                        if item.sell_in < 11 and item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6 and item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != sulfuras:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != passes_backstage:
                        if item.quality > 0:
                            if item.name != sulfuras:
                                item.quality = item.quality - 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
