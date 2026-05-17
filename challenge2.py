from utils import hex_xor


a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
c = "746865206b696420646f6e277420706c6179"

if hex_xor(a, b) == c:
    print("Test Passed")
elif hex_xor(a, b) != c:
    print("Test failed.")
