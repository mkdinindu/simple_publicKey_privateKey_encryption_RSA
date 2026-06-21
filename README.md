# RSA Encryption & Authentication Tool

An educational Python implementation of RSA public-key cryptography and digital signatures, featuring a graphical user interface built with `tkinter`.

## Features

- **RSA Key Generation** — Generates public/private key pairs from any two prime numbers
- **Encryption & Decryption** — Textbook RSA using modular exponentiation
- **Digital Signatures** — Sign a ciphertext with the sender's private key; verify with the sender's public key
- **Graphical Interface** — Step-by-step visualization of the full RSA pipeline: key generation → encryption → signing → verification → decryption

## How It Works

Two peers (A and B) each generate an RSA key pair:

1. **A encrypts** a message for B using B's public key
2. **A signs** the ciphertext with A's private key
3. **B verifies** the signature using A's public key
4. **B decrypts** the verified ciphertext using B's private key

All intermediate values — public/private keys, ciphertext, authenticated value, and the final decrypted message — are displayed in the results panel.

## Getting Started

### Requirements

- Python 3.8 or later (uses `pow(x, -1, mod)` for modular inverse)
- `tkinter` (included with most Python distributions)

### Run the GUI

```bash
python3 GUI.py
```

### Run the CLI demo

```bash
python3 RSA.py
```

## Usage

1. Enter two prime numbers for Peer A (sender) and Peer B (recipient)
2. Enter a numeric message
3. Click **Encrypt & Sign** to see the full pipeline

Toggle **Decryption mode** to verify and decrypt an already-signed message using the recipient's public key `(e, n)`.

## Project Structure

```
RSA.py   — Core RSA library (key generation, encrypt, decrypt, sign, verify)
GUI.py   — tkinter graphical user interface
```

## Disclaimer

This project is **for educational purposes only**. It uses textbook RSA without padding (OAEP/PSS), no large prime generation, and no secure random number generation. **Do not use it for real-world cryptography.**
