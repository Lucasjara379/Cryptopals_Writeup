def decrypt(hex_str: str) -> str:
    """Decrypt hex string that has been encrypted with a single byte xor."""
    letter_frequency = {'E': 12.0,
                        'T': 9.10,
                        'A': 8.12,
                        'O': 7.68,
                        'I': 7.31,
                        'N': 6.95,
                        'S': 6.28,
                        'R': 6.02,
                        'H': 5.92,
                        'D': 4.32,
                        'L': 3.98,
                        'U': 2.88,
                        'C': 2.71,
                        'M': 2.61,
                        'F': 2.30,
                        'Y': 2.11,
                        'W': 2.09,
                        'G': 2.03,
                        'P': 1.82,
                        'B': 1.49,
                        'V': 1.11,
                        'K': 0.69,
                        'X': 0.17,
                        'Q': 0.11,
                        'J': 0.10,
                        'Z': 0.07}
    raw_bytes = bytes.fromhex(hex_str)
    decrypted_msgs = {}

    for key in range(256):
        xored = bytes([b ^ key for b in raw_bytes
                       if b ^ key in range(32, 127)])
        if len(xored) == len(raw_bytes):
            msg = xored.decode()
            msg_upper = msg.upper()
            observed = {letter: msg_upper.count(letter)
                        for letter in letter_frequency}
            chi_squared = 0
            for letter in letter_frequency:
                predicted = letter_frequency[letter]/100*len(msg)
                chi_squared += (observed.get(letter) - predicted)**2/predicted  # noqa E501
            decrypted_msgs[msg] = chi_squared

    return min(decrypted_msgs, key=decrypted_msgs.get)


if __name__ == '__main__':
    m = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(decrypt(m))

# key is 88 and message is "Cooking MC's like a pound of bacon"
