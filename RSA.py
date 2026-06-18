import math as math
def generateKey(prime_one, prime_two):
    n = prime_one * prime_two #multiplies the primes 
    phi = (prime_one - 1) * (prime_two - 1)

    e = 3 #temporary assignment

    #finding a valid public exponent e 
    while math.gcd(e, phi) != 1:
        e += 2 #check odd numbers to find a coprime exponent efficiently

    #finding a valid private exponent d
    d = pow(e, -1, phi)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key


def encrypt(message, reciever_public_key):
    e, n = reciever_public_key
    return pow(message, e, n)

def decrypt(message, private_key):
    d, n = private_key
    return pow(message, d, n)

def addAuth(ciphered, private_key):
    d, n = private_key
    return pow(ciphered, d, n)

def checkAuth(cipheredAuthed, public_key):
    e, n = public_key
    return pow(cipheredAuthed, e, n)

if __name__ == "__main__":

    #peer A
    prime1A = 17
    prime2A = 19

    #peer B 
    prime1B = 5
    prime2B = 7

    #peer A 
    pub_keyA, priv_keyA = generateKey(prime1A, prime2A)

    #peer B 
    pub_keyB, priv_keyB = generateKey(prime1B, prime2B)
    print("Generated public key, peer A : {pub_key}", pub_keyA)
    print("Generated private key, peer A : {priv_key}", priv_keyA)

    print("Generated public key, peer B : {pub_key}", pub_keyB)
    print("Generated private key, peer B : {priv_key}", priv_keyB)

    # send a message to B 

    message_NUM = 9
    print("original message: ", message_NUM)
    cipher = encrypt(message_NUM, pub_keyB)
    print("Encrypted message: {cipher}", cipher)

    # B decrypts it 


    #decrypted = decrypt(cipher, priv_keyB)
    #print("Decrypted message: {decrypted}", decrypted)

    #Authentication adding

    authenticated = addAuth(cipher, priv_keyA)
    print("Authenticated by A: ", authenticated)

    #now B have to try to decrypt the message first using A's publick key to ensure the authenticity 

    authChecked = checkAuth(authenticated, pub_keyA)
    print("authentication checked: ", authChecked)

    decrypted = decrypt(authChecked, priv_keyB)
    print("Decrypted message: {decrypted}", decrypted)



