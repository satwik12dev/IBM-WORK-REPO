import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(value.encode("utf-8")).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)

# Example usage
if __name__ == "__main__":
    my_blockchain = Blockchain()

    for i in range(1, 5):
        my_blockchain.add_block(f"#{i} block after genesis")

    for block in my_blockchain.chain:
        print("Timestamp:", block.timestamp)
        print("Data:", block.data)
        print("Hash:", block.hash)
        print()
    
    my_blockchain.get_latest_block().data = "Tampered Data"
