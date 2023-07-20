import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]  # [a,p] inclusive


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


# split character into top 4 and bottom 4 bits, as X and Y
# append ALPHABET[X] then ALPHABET[Y]
def b16_decode(enc):
    plain = ""
    for i in range(0, len(enc), 2):
        c = enc[i]
        c2 = enc[i + 1]

        dec1 = ALPHABET.index(c)
        dec1_binary = "{0:04b}".format(dec1)

        dec2 = ALPHABET.index(c2)
        dec2_binary = "{0:04b}".format(dec2)

        comb = dec1_binary + dec2_binary
        char = chr(int(comb, 2))

        plain += char
    return plain


# enc = b16_encode('abcde')
# print(f"enc: {enc}")

# dec = b16_decode(enc)
# print(f"dec: {dec}")


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def unshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    ans = (t1 + len(ALPHABET) - t2 + 1)

    ans = ans % len(ALPHABET)

    return ALPHABET[ans]


def shift_all(s, k):
    return ''.join([shift(c, key) for c in flag])


def unshift_all(s, k):
    return ''.join([unshift(c, key) for c in flag])

# flag = 'abcd'
# key = 'b'

# print(unshift_all(shift_all(flag, key), key))


for i in range(97, 96 + 17):
    flag = 'mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj'
    key = chr(i)
    assert all([k in ALPHABET for k in key])
    assert len(key) == 1

    print(f'key: {key}')
    print(
        # ''.join([
            # '{:02x}'.format(ord(c)) for c in
            b16_decode(unshift_all(flag, key))
        # ])
    )
    print()
