import hashlib
import random

# ------------------------------
# Transaction Class
# ------------------------------
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return f"{self.sender} -> {self.receiver} : {self.amount}"


# ------------------------------
# Proof of Work
# ------------------------------
def proof_of_work(data, difficulty=3):
    nonce = 0

    while True:
        text = data + str(nonce)
        hash_result = hashlib.sha256(text.encode()).hexdigest()

        if hash_result.startswith('0' * difficulty):
            return nonce, hash_result

        nonce += 1


# ------------------------------
# Proof of Stake
# ------------------------------
def proof_of_stake(validators):
    total_stake = sum(validators.values())

    rand = random.uniform(0, total_stake)

    current = 0
    for validator, stake in validators.items():
        current += stake
        if current > rand:
            return validator


# ------------------------------
# Main Program
# ------------------------------

transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    sender = input("Sender: ")
    receiver = input("Receiver: ")
    amount = input("Amount: ")

    t = Transaction(sender, receiver, amount)
    transactions.append(t)

print("\nTransactions:")
for t in transactions:
    print(t)

# Proof of Work
data = "".join(str(t) for t in transactions)

nonce, hash_value = proof_of_work(data)

print("\nProof of Work Result")
print("Nonce:", nonce)
print("Hash:", hash_value)


# Proof of Stake
validators = {
    "Satwik": 50,
    "Sanya": 30,
    "Hardik": 20
}

selected = proof_of_stake(validators)

print("\nProof of Stake Validator Selected:", selected)