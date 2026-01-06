import hashlib
import time

#creating a class for block
class Block :
    def __init__(self,index,data,timestamp,prevhash):
        self.index=index
        self.data=data
        self.prevhash=prevhash
        self.timestamp=timestamp
        self.hash=self.mining
        self.nonce=0
#for hash value ->
    def hashingvalue(self):
        blockdata=str(self.index)+str(self.data)+str(self.timestamp)+str(self.prevhash)+str(self.nonce)
        return hashlib.sha256(blockdata.encode()).hexdigest()
    def mining(self):
        while True:
            if self.hashingvalue.startwith("00"):
                return self.hashingvalue
            else:
                self.nonce=self.nonce+1


class Blockchain:
    def __init__(self):
        self.chain=[self.createblock()]

        #method to get the first block
    def createblock(self):
            # first block so taking prevhash =0
        return Block(1,"origin block",time.time(),"0")
        
        #to create a new block
    def addblock(self,data):
        prevblock=self.chain[-1]
        new_block = Block(
                prevblock.index+1,
                data,
                time.time(),
                prevblock.hash
            )
        self.chain.append(new_block)
       
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.hashingvalue():
                return False

            if current.prevhash!= previous.hash:
                return False

        return True

blockchain = Blockchain()

blockchain.addblock("second block")
blockchain.addblock("third block")
blockchain.addblock("fourth block")

print("Blockchain valid:", blockchain.is_valid())


for block in blockchain.chain:
    print("Index=", block.index)
    print("Data=", block.data)
    print("Timestamp=", block.timestamp)
    print("Hash=", block.hash)
    print("Previous Hash=", block.prevhash)
    print("")
   




