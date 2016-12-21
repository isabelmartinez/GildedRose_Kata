from GildedRose_Kata import*

if __name__ == '__main__':

    item = Conjured("Conjured Mana Cake", 3, 6)

    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)
