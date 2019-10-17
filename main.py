import user
import math
import random

def isPrime(number):

    if number == 0 or number == 1 :
        return False
    for i in range(2,int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def nthPrimeNumber(n):

    if(n == 0 or n == 1):
        return 2

    result = 1
    count = 1

    while(count < n):

        result += 2
        if isPrime(result) == True:
            count += 1
    return result

def main():

    p = nthPrimeNumber(int((input("Enter the nth prime number wanted for p: "))))
    q = nthPrimeNumber(int((input("Enter the mth prime number wanted for q: "))))

    Alice = user.User(p , q, "Alice")
    Bob = user.User(p , q, "Bob")

    Alice.printParams()
    Alice.computeE()
    Alice.printPublicKey()
    Alice.computeD()
    Alice.printPrivateKey()

    Bob.printParams()
    Bob.computeE()
    Bob.printPublicKey()
    Bob.computeD()
    Bob.printPrivateKey()

    #    0<plaintext <N
    plaintext = random.randrange(1, p * q)

    print("Plaintext is: ",plaintext)
    ############## Encryption
    # Alice-----Bob
    # Bob encrypts with Alice's public key
    # Then Alice decrypts with her private key
    cipher = Bob.encrypt(plaintext,Alice.getPublicKey())

    print("Encrypted RSA message: ",cipher)

    deciphered = Alice.decrypt(cipher)

    print("Decripted RSA message: ",deciphered)

    ############### Digital Sign

    # Alice-----Bob
    # Bob signs with his private key
    # Then Alice decrypts with Bob's public key

    signed = Bob.sign(plaintext)

    print("Signed RSA message: ",signed)

    verified = Alice.verify(signed, Bob.getPublicKey())

    print("Verified digital RSA sign: ", verified)

if __name__ == "__main__":
    main()
