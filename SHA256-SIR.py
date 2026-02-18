import struct

# Initial hash values (first 32 bits of the fractional parts of the square roots of the first 8 primes 2..19)
H = [
    0x6a09e667,
    0xbb67ae85,
    0x3c6ef372,
    0xa54ff53a,
    0x510e527f,
    0x9b05688c,
    0x1f83d9ab,
    0x5be0cd19,
]

#The initial hash values (H) are defined by the SHA-256 standard as the first 32 bits of the fractional parts of the 
# square roots of the first eight prime numbers. These values are used to initialize the hash state before processing 
# any data and are a part of the algorithm's design to ensure security and randomness.

#The first eight prime numbers are 2, 3, 5, 7, 11, 13, 17, and 19. The initial hash values are calculated as follows:

#Square Root Calculation: For each prime number, compute the square root.
#Fractional Part Extraction: Extract the fractional part of the square root (i.e., the part after the decimal point).
#First 32 Bits: Convert the fractional part to a 32-bit word (by multiplying by 2^32 and taking the integer part).


# Constants for SHA-256 (first 32 bits of the fractional parts of the cube roots of the first 64 primes 2..311)
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
    0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
    0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
    0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
    0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
    0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
    0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
    0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
    0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Helper functions
def right_rotate(value, amount):
    return ((value >> amount) | (value << (32 - amount))) & 0xffffffff

def sha256(message):
    # Pre-processing: padding the input
    message = bytearray(message)  # Copy input to bytearray for mutability
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8
    message.append(0x80)  # Append '1' bit
    # Append '0' bits until message length is 448 mod 512
    while len(message) % 64 != 56:
        message.append(0)
    # Append original message length as a 64-bit big-endian integer
    message += original_bit_len.to_bytes(8, byteorder='big')
    '''
    The message is converted to a bytearray and appended with a 1 bit (0x80). The 
    message is then padded with 0 bits 
    until its length is 448 bits modulo 512. Finally, the length of the original 
    message (in bits) is appended as a
    64-bit big-endian integer. 
'''
    # Process the message in successive 512-bit chunks
    hash_pieces = H[:]
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        w = list(struct.unpack('>16L', chunk)) + [0] * 48
        # Message schedule
        for i in range(16, 64):
            s0 = right_rotate(w[i - 15], 7) ^ right_rotate(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = right_rotate(w[i - 2], 17) ^ right_rotate(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w[i] = (w[i - 16] + s0 + w[i - 7] + s1) & 0xffffffff
            '''
        The message is processed in 512-bit chunks (64 bytes). Each chunk is 
        expanded into 64 words (w), where each word is 32 bits.
        A series of bitwise operations, rotations, and modular additions are 
        performed for 64 rounds, updating the hash values.
          '''  
        a, b, c, d, e, f, g, h = hash_pieces        
        # Compression function main loop
        for i in range(64):
            S1 = right_rotate(e, 6) ^ right_rotate(e, 11) ^ right_rotate(e, 25)
            ch = (e & f) ^ (~e & g)
            temp1 = (h + S1 + ch + K[i] + w[i]) & 0xffffffff
            S0 = right_rotate(a, 2) ^ right_rotate(a, 13) ^ right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xffffffff
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xffffffff
            d = c
            c = b         
            b = a
            a = (temp1 + temp2) & 0xffffffff
        # Add the compressed chunk to the current hash value
        hash_pieces = [(x + y) & 0xffffffff for x, y in zip(hash_pieces, [a, b, c, d, e, f, g, h])]

    # Produce the final hash value (big-endian) as a hex digest
    return ''.join(f'{piece:08x}' for piece in hash_pieces)

# Example usage
input_string = "Hello"
hash_result = sha256(input_string.encode())
print(f"SHA-256 hash of '{input_string}': {hash_result}")
