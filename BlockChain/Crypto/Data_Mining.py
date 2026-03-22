import hashlib
import json
import random
from datetime import datetime


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount
        }


class Block:

    def __init__(self, index, transaction, previous_hash, miner):

        self.index = index
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction = transaction
        self.previous_hash = previous_hash
        self.miner = miner
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):

        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transaction": self.transaction.to_dict(),
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "miner": self.miner
        }, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:

    difficulty = 4

    def __init__(self):

        self.chain = []

        self.balances = {
            "Alice": 100,
            "Bob": 80,
            "Charlie": 60
        }

        self.miners = [f"Miner{i}" for i in range(1, 11)]

        for m in self.miners:
            self.balances[m] = 0

        self.create_genesis_block()

    def create_genesis_block(self):
        genesis = Block(0, Transaction("Genesis","Network",0), "0", "Genesis")
        self.chain.append(genesis)

    def get_latest_block(self):
        return self.chain[-1]


    def validate_transaction(self, tx):

        if self.balances[tx.sender] < tx.amount:
            return False

        return True


    def proof_of_work(self, block):

        while block.hash[:Blockchain.difficulty] != "0" * Blockchain.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()

        return block


    def mine_transaction(self, tx):

        miner = random.choice(self.miners)

        block = Block(
            len(self.chain),
            tx,
            self.get_latest_block().hash,
            miner
        )

        block = self.proof_of_work(block)

        self.chain.append(block)

        fee = tx.amount * 0.10   # 10% fee
        receiver_amount = tx.amount - fee

        self.balances[tx.sender] -= tx.amount
        self.balances[tx.receiver] += receiver_amount
        self.balances[miner] += fee

        self.print_block(block)


    def print_block(self, block):

        print("\n====================================")

        print("Block Number:", block.index)
        print("Timestamp:", block.timestamp)
        print("Miner:", block.miner)
        print("Nonce (Proof):", block.nonce)

        print("\nTransactions")
        print(f"{block.transaction.sender} → {block.transaction.receiver} : {block.transaction.amount}")
        fee = block.transaction.amount * 0.10

        print("Transaction Amount:", block.transaction.amount)
        print("Miner Fee (10%):", fee)
        print("Receiver Gets:", block.transaction.amount - fee)
        print("Balances After Transaction:")
        for user, balance in self.balances.items():
            print(f"  {user}: {balance}")

        print("\nPrevious Hash:", block.previous_hash)
        print("Block Hash:", block.hash)

        print("====================================\n")


# -----------------------
# Simulation
# -----------------------

blockchain = Blockchain()

users = ["Alice","Bob","Charlie"]

# Mine 10 transactions → 10 blocks
for i in range(10):

    sender = random.choice(users)
    receiver = random.choice([u for u in users if u != sender])

    amount = random.randint(1,10)

    tx = Transaction(sender,receiver,amount)

    blockchain.mine_transaction(tx)