def hex2base64(s: str) -> str:
    """convert hex string into base64 string"""
    import base64
    return base64.b64encode(bytes.fromhex(s))


if __name__ == '__main__':
    answer = hex2base64('49276d206b696c6c696e6720'
                        '796f757220627261696e206c69'
                        '6b65206120706f69736f6e6f757'
                        '3206d757368726f6f6d')
    print(answer)
    print(answer == b'SSdtIGtpbGxpbmcgeW91ciBic'
          b'mFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')
