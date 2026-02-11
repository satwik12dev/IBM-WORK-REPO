import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash,hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash

    def calculate_hash(index, timestamp, data, previous_hash): # type: ignore
        value = str(index) + str(timestamp) + str(data) + str(previous_hash)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()
    
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0", hashlib.sha256(b"Genesis Block").hexdigest()) # type: ignore

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash, latest_block.hash)
        self.chain.append(new_block)

# Example usage
if __name__ == "__main__":
    my_blockchain = Blockchain()
    for i in range(1, 5):
         my_blockchain.add_block(f"#{i} block after genesis")

    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}\n")