import base64

def base16():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    b16转码 = base64.b16encode(encoded) #b16转码 the encoded string
    print(b16转码)
    print(base64.b16decode(b16转码).decode('utf-8'))  # decoded it
    
def base32():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    b32encoded = base64.b32encode(encoded) #b32encoded the encoded string
    print(b32encoded)
    print(base64.b32decode(b32encoded).decode('utf-8'))#decoded it
    
def base85():
    inp = input('->')
    encoded = inp.encode('utf-8') #encoded the input (we need a bytes like object)
    a85encoded = base64.a85encode(encoded) #a85encoded the encoded string
    print(a85encoded)
    print(base64.a85decode(a85encoded).decode('utf-8'))#decoded it

if __name__ == '__main__':
    base16()
    base32()
    base85()
