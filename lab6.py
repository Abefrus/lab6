def galois_mul02(byte):
    byte <<= 1
    if byte & 0x100:
        byte ^= 0x1B
    return byte & 0xFF

def galois_mul03(byte):
    return galois_mul02(byte) ^ byte

def galois_mul(byte1, byte2):
    result = 0
    for i in range(8):
        if byte2 & 1:
            result ^= byte1
        carry = byte1 & 0x80
        byte1 <<= 1
        if carry:
            byte1 ^= 0x1B
        byte2 >>= 1
    return result & 0xFF

print(f"D4 * 02 = {galois_mul02(0xD4):02X}")
print(f"BF * 03 = {galois_mul03(0xBF):02X}")
print(f"57 * 83 = {galois_mul(0x57, 0x83):02X}")
