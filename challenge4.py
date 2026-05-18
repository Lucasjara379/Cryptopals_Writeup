from challenge3 import decrypt_single_byte_xor


with open("challenge4.txt", 'r') as f:
    best_score = float('inf')
    best_line = ''
    for line in f:
        line = line.strip()
        decrypted_line, score = decrypt_single_byte_xor(line)
        if score < best_score:
            best_line = decrypted_line
            best_score = score
print(repr(best_line))
    