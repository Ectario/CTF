xor_key = 'd3cRYp7_k3Y'
hostname = [31, 117, 47, 21, 99, 32, 88, 110, 5, 71, 54, 2, 112, 12, 60, 45, 2, 7, 51, 69, 80, 52, 25]

def decrypt_hostname():
    plain_host = []
    for i in range(len(hostname)):
        c1 = hostname[i]
        c2 = ord(xor_key[(i % len(xor_key))])
        plain_host.append(chr(c1 ^ c2))
    return plain_host
print(''.join(decrypt_hostname()))