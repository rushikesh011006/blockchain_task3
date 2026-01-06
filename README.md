# blockchain_task3

Simple Blockchain Implementation

Block Structure
Each block contains an index, timestamp, data, previous hash, nonce, and its own hash.
The hash is generated using SHA-256 by combining all block fields.
The previous hash links each block to the one before it, forming a chain.

Validation Logic
The blockchain validates integrity by recalculating each block’s hash and comparing it with the stored hash. It also checks whether each block’s previous hash matches the hash of the previous block. Any modification in block data breaks the hash linkage and is detected as tampering.

Proof-of-Work
A basic Proof-of-Work mechanism is implemented using a nonce.
The nonce is incremented repeatedly until the generated hash satisfies a target condition (leading zeros). This simulates mining by making block creation computationally expensive.
