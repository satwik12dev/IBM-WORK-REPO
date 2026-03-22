import hashlib
import time

class Transaction:
    #Represents a simple transaction with a sender, receiver, and amount.
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

class Block:
    #Contains the index, previous block's hash, timestamp, list of transactions, proof (for PoW), and its hash.
    def __init__(self, index, previous_hash, timestamp, transactions, proof, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.proof = proof
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, transactions, proof):
    transaction_details = ''.join([f'{tx.sender}->{tx.receiver}:{tx.amount}' for tx in transactions])
    value = f'{index}{previous_hash}{timestamp}{transaction_details}{proof}'
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.current_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        #The first block in the blockchain, created manually.
        return Block(0, "0", time.time(), [], 0, calculate_hash(0, "0", time.time(), [], 0))

    def get_latest_block(self):
        #Stores pending transactions in a list (current_transactions).
        return self.chain[-1]

    def add_transaction(self, sender, receiver, amount):
        #Provides a reward for mining a new block, credited to the miner's address.
        self.current_transactions.append(Transaction(sender, receiver, amount))

    def proof_of_work(self, previous_proof):
        #Implements a simple proof of work where the hash must start with "0000".
        proof = 0
        while not self.is_valid_proof(previous_proof, proof):
            proof += 1
        return proof

    def is_valid_proof(self, previous_proof, proof):
        guess = f'{previous_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def mine_block(self, miner_address):
        # Adds a reward transaction, finds a valid proof, creates a new block, and appends it to the blockchain.
        self.add_transaction(sender="Network", receiver=miner_address, amount=self.mining_reward)
        
        latest_block = self.get_latest_block()
        proof = self.proof_of_work(latest_block.proof)
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            timestamp=time.time(),
            transactions=self.current_transactions,
            proof=proof,
            hash=calculate_hash(latest_block.index + 1, latest_block.hash, time.time(), self.current_transactions, proof)
        )
        self.chain.append(new_block)
        self.current_transactions = []

        print(f"Block #{new_block.index} mined successfully!")
        print(f"Hash: {new_block.hash}\n")
        return new_block

def main():
    #Simulates Transactions: Adds a few transactions between different users.
    #Mines Blocks: Mines blocks to confirm transactions, awarding the miner.
    #Prints the Blockchain: Outputs the details of each block in the chain, including transactions.
    blockchain = Blockchain()
    
    # Simulate transactions and mining
    blockchain.add_transaction("Alice", "Bob", 50)
    blockchain.mine_block("Miner1")

    blockchain.add_transaction("Bob", "Alice", 25)
    blockchain.mine_block("Miner2")

    blockchain.add_transaction("Alice", "Charlie", 40)
    blockchain.add_transaction("Charlie", "Bob", 15)
    blockchain.mine_block("Miner1")

    # Print the blockchain
    for block in blockchain.chain:
        print(f"Block #{block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block.timestamp))}")
        print("Transactions:")
        for tx in block.transactions:
            print(f"  {tx.sender} -> {tx.receiver}: {tx.amount}")
        print(f"Proof: {block.proof}")
        print(f"Hash: {block.hash}\n")

if __name__ == "__main__":
    main()
