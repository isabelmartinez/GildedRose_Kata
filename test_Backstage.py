from GildedRose_Kata import*

if __name__ == '__main__':

    item = Backstage("Backstage passes to a TAFKAL80ETC concert", 15, 20)

    print(item)

    for dia in range(1, 10):
        item.update_quality()
        print(item)
