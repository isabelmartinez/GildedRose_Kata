from GildedRose_Kata import *

if __name__ == '__main__':

    item = NormalItem("Elixir of the Mongoose", 5, 7)

    print(item)

    for dia in range(1, 5):
        item.update_quality()
        print(item)
