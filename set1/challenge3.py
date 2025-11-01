def decrypt(hex_str):
    """Decrypt hex string that has been encrypted with a single byte xor."""

    raw_bytes = bytes.fromhex(hex_str)
    decrypted_msgs = []

    for i in range(256):
        xored = bytes([b ^ i for b in raw_bytes if b ^ i in range(32, 127)])
        if len(xored) == len(raw_bytes):
            msg = xored.decode()
            decrypted_msgs.append(msg)

    return decrypted_msgs


if __name__ == '__main__':
    m = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(decrypt(m))

# key is 88 and message is "Cooking MC's like a pound of bacon"
