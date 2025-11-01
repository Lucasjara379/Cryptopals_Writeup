def xor(x, y):
    """xor equal length hex strings x and y and get back a hex string."""
    raw_x, raw_y = bytes.fromhex(x), bytes.fromhex(y)
    return "".join([hex(x ^ y)[2:] for x, y in zip(raw_x, raw_y)])


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
c = "746865206b696420646f6e277420706c6179"


if __name__ == "__main__" and xor(a, b) == c:
    print("Test Passed")

elif xor(a, b) != c:
    print("Test failed.")
