from utils import single_byte_xor, is_printable, letter_frequencies, score_english


def decrypt_single_byte_xor(hex_str: str) -> str:
    """Decrypt hex string that has been encrypted with a single byte xor."""


    raw_bytes = bytes.fromhex(hex_str)
    best_msg = ''
    best_score = float('inf')
    for key in range(256):
        xored = single_byte_xor(raw_bytes, key)
        try:
            msg = xored.decode()
        except UnicodeDecodeError:
            continue
        score = score_english(msg)
        if score < best_score:
            best_msg, best_score = msg, score
    return best_msg, best_score


if __name__ == '__main__':
    m = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    print(decrypt_single_byte_xor(m)[0])

# key is 88 and message is "Cooking MC's like a pound of bacon"
