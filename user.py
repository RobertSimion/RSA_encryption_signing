import random
def computeGcd(a,b):

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

class User:

    def __init__(self,p,q,name):

        self.p = p
        self.q = q
        self.name  = name
        self.N  = p * q
        self.fi  = (p - 1) * (q - 1)
        self.publicKey = [0, 0]
        self.privateKey = [0, 0, 0]

    def printP(self):

        print("p parameter: ",self.p)

    def printQ(self):

        print("q parameter: ",self.q)

    def printN(self):

        print("N parameter: ",self.N)

    def printFi(self):

        print("fi parameter: ",self.fi)

    def printName(self):

        print("Name is: ",self.name)

    def printParams(self):

        self.printName()
        self.printP()
        self.printQ()
        self.printN()
        self.printFi()

    def printPublicKey(self):

        print("Public Key for " + self.name + " is: ", self.publicKey)

    def printPrivateKey(self):

        print("Private Key for " + self.name + " is: ", self.privateKey)

    def generatePairOfKeys(self):

        self.computeE()
        self.computeD()
    def computeE(self):


        while True:

            aux = random.randrange(2, self.fi)
            if( computeGcd(aux, self.fi) == 1):
                self.e = aux
                self.publicKey[0] = self.N
                self.publicKey[1] = self.e
                break

    def getPublicKey(self):

        return self.publicKey

    def computeD(self):

         for i in range(2,self.fi):
             if  (i * self.e) % self.fi == 1:
                 self.d = i
                 self.privateKey = [ self.d, self.p, self.q]
                 break

    def encrypt(self, message, publicKey):

        return (message ** publicKey[1]) % publicKey[0]

    def decrypt(self,encrypted):

        return (encrypted ** self.privateKey[0]) % self.N

    def sign(self,message):

        return (message ** self.privateKey[0]) % self.N

    def verify(self,signed,publicKey):

        return (signed ** publicKey[1]) % publicKey[0]