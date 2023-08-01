#第1引数 = price
#第2引数 = tax

def add_two_arguments(price, tax):
    total = price + (price * tax)
    print(f"{total}円")

add_two_arguments(1000, 0.1)