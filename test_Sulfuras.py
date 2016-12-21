from GildedRose_Kata import *

if __name__ == '__main__':

    item = Sulfuras("Sulfuras, Hand of Ragnaros", 0, 80)

    print(item)

    for dia in range(1, 5):
        item.update_quality()
        print(item)
