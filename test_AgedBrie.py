from GildedRose_Kata import *

if __name__ == '__main__':

    item = AgedBrie("Aged Brie", 2, 0)

    print(item)

    for dia in range(1, 5):
        item.update_quality()
        print(item)
