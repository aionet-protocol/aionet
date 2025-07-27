
# agent_validator.py
# Simulates AI-like logic to score and validate mock transactions

import random

def score_transaction(tx):
    # Very simple mock AI scoring logic
    if tx['amount'] <= 0:
        return 0  # invalid
    if "contract" in tx and tx["contract"] == "suspicious":
        return 0.2
    if tx["amount"] > 10000:
        return 0.4
    return 1.0

def validate(tx):
    score = score_transaction(tx)
    return score >= 0.5

# Example transactions
txs = [
    {"from": "Alice", "to": "Bob", "amount": 50},
    {"from": "Eve", "to": "Mallory", "amount": 20000},
    {"from": "User", "to": "Contract", "amount": 0, "contract": "suspicious"}
]

for tx in txs:
    print(f"TX: {tx} => VALID: {validate(tx)}")
