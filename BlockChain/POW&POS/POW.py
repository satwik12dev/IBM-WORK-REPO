import hashlib
import time
import matplotlib.pyplot as plt

'''
Proof of Work requires miners to find a number (called a nonce) that, when hashed along with the 
block's data, produces a hash value that meets a certain condition (e.g., starts with a certain number 
of zeros).
Proof of Work (PoW): This is a consensus mechanism that ensures the integrity of the blockchain by 
requiring computational work (hashing) to be performed before adding a new block.
Difficulty: This defines how hard it is to find a valid hash. Higher difficulty means more 
computational work is required, making the network more secure but also requiring more processing power.
'''

class Block:
    def __init__(self, index, previous_hash, timestamp, data, difficulty):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.difficulty = difficulty
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Combine the block attributes to create a hash
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self):
        # Adjust the nonce until the hash meets the required difficulty
        target = '0' * self.difficulty
        while self.hash[:self.difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        print(f"Block mined: {self.hash}")

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # The genesis block is the first block in the chain
        return Block(0, "0", time.time(), "Genesis Block", difficulty=2)  # Default difficulty for the genesis block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block()  # Mine the block to meet the proof of work requirement
        self.chain.append(new_block)

# Testing the Proof of Work implementation
def main():
    difficulty_levels = [1, 2, 3, 4, 5]  # Different levels of difficulty
    mining_times = []

    for difficulty in difficulty_levels:
        blockchain = Blockchain()
        print(f"\nMining with difficulty level: {difficulty}")

        start_time = time.time()

        print("Mining block 1...")
        block1 = Block(1, "", time.time(), "Block 1 Data", difficulty)
        blockchain.add_block(block1)

        print("Mining block 2...")
        block2 = Block(2, "", time.time(), "Block 2 Data", difficulty)
        blockchain.add_block(block2)

        end_time = time.time()
        mining_times.append(end_time - start_time)

    # Plot the mining times
    plt.figure(figsize=(10, 6))
    plt.plot(difficulty_levels, mining_times, marker='o')
    plt.title('Mining Time vs. Difficulty Level')
    plt.xlabel('Difficulty Level')
    plt.ylabel('Time (seconds)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
'''
Mining Simulation: The script simulates the mining of blocks at different difficulty levels. The time 
taken to mine each block is recorded and plotted.
Visualization: After running the script, you will see a plot showing how the time taken to mine 
blocks increases with difficulty, illustrating the concept of computational difficulty in Proof of 
Work.
'''