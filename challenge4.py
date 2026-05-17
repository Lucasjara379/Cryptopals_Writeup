from challenge3 import decrypt_single_byte_xor
from utils import score_english


decrypted_lines = {}
with open("challenge4.txt", 'r') as f:
    best_score = float('inf')
    best_line = ''
    for line in f:
        line = line.strip()
        decrypted_line = decrypt_single_byte_xor(line)
        score = score_english(decrypted_line)
        if score < best_score:
            best_line = decrypted_line
            best_score = score
print(best_line)
    