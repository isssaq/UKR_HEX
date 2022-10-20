s = 'FFFFFFFF'

def to_little(s):    
    sq = bytearray.fromhex(s)
    sq.reverse()

    sq_little = ''.join(format(x, '02x') for x in sq)

    return int(sq_little, 16)

def to_big(s):
    sq = bytearray.fromhex(s)
    sq_big = ''.join(format(x, '02x') for x in sq)

    return int(sq_big, 16)

def from_big_to_hex(big_en):
    return hex(big_en)

def from_little_to_hex(little_en, n):
    filling_zero = (n - len(hex(little_en)[2:]) // 2) * 2
    return hex(little_en) + '0' * filling_zero



d = to_little(s)
b = to_big(s)

print(from_big_to_hex(b))
print(from_little_to_hex(d, 4))
    

