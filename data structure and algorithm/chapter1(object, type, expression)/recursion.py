def test(high, low):
    while low<= high:
        print(low)
        low = low+1
        # test()
test(44,34)

def iterate(low, high):
    if low<= high:
        print(low)
        iterate(low+1,high)