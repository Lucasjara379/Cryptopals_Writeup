letter_frequencies = {
            "a": 0.08497,
            "b": 0.01492,
            "c": 0.02202,
            "d": 0.04253,
            "e": 0.11162,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.07546,
            "j": 0.00153,
            "k": 0.01292,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.07587,
            "s": 0.06327,
            "t": 0.09356,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02560,
            "x": 0.00150,
            "y": 0.01994,
            "z": 0.00077,
        }

def hex_to_base64(s: str) -> str:
    """convert hex string into base64 string"""
    import base64
    return base64.b64encode(bytes.fromhex(s))


def hex_xor(x, y):
    """xor equal length hex strings x and y and get back a hex string."""
    raw_x, raw_y = bytes.fromhex(x), bytes.fromhex(y)
    return "".join([hex(x ^ y)[2:] for x, y in zip(raw_x, raw_y)])


def single_byte_xor(bytes_input: bytes, key: int) -> bytes:
    return bytes(b ^ key for b in bytes_input)


def is_printable(data: bytes) -> bool:
    return all(32 <= b < 127 for b in data)


def score_english(message: str) -> float:
    text = message.lower()
    letters = [letter for letter in text if 'a' <= letter <= 'z']
    if not len(text):
        return float('inf')
    alphabet_proportion = len(letters) / len(text)
    if (not letters) or alphabet_proportion < 0.8:
        return float('inf')
    chi_squared = 0 
    for letter in letter_frequencies:
        n = letters.count(letter)
        expected = len(letters) * letter_frequencies[letter]
        chi_squared += (n - expected)**2 / expected
    return chi_squared

