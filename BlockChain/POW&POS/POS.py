import random

class ProofOfStake:
    def __init__(self):
        self.validators = {}

    def add_validator(self, validator_id, stake):
        """Adds a validator with an initial stake."""
        self.validators[validator_id] = self.validators.get(validator_id, 0) + stake

    def remove_validator(self, validator_id):
        """Removes a validator from the list."""
        if validator_id in self.validators:
            del self.validators[validator_id]

    def select_validator(self):
        """Select a validator based on their stake proportion."""
        total_stake = sum(self.validators.values())
        if total_stake == 0:
            raise ValueError("Total stake must be greater than zero to select a validator.")

        selection_point = random.uniform(0, total_stake)
        current_sum = 0

        for validator, stake in self.validators.items():
            current_sum += stake
            if current_sum >= selection_point:
                return validator
        return None

    def reward_validator(self, validator_id, reward=10):
        """Rewards a validator by increasing their stake."""
        if validator_id in self.validators:
            self.validators[validator_id] += reward

pos_system = ProofOfStake()

pos_system.add_validator("Validator_A", 50)
pos_system.add_validator("Validator_B", 30) 
pos_system.add_validator("Validator_C", 20)

rounds = 10
for i in range(rounds):
    print(f"\nRound {i + 1}")
    selected_validator = pos_system.select_validator()
    print(f"Selected Validator: {selected_validator}")

    pos_system.reward_validator(selected_validator, reward=5)

    for validator, stake in pos_system.validators.items():
        print(f"{validator} - Stake: {stake}")

print("\nFinal Validator Stakes:")
for validator, stake in pos_system.validators.items():
    print(f"{validator} - Final Stake: {stake}")
