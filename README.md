# Professional Hash Cracker

A high-performance, multi-threaded hash cracking tool written in Python. It supports multiple hashing algorithms and uses parallel processing to maximize speed.

## Features

- **Multi-Algorithm Support:** MD5, SHA-1, SHA-256, and SHA-512.
- **Auto-Detection:** Automatically identifies the hashing algorithm based on the hash length.
- **High Performance:** Utilizes Python multiprocessing to leverage all available CPU cores.
- **CLI Interface:** Easy-to-use command-line interface with customizable settings.

## Installation

Ensure you have Python 3.x installed.

`ash
git clone https://github.com/coolstx/hash-cracker.git
cd hash-cracker
`

## Usage

Basic usage with auto-detection:

`ash
python cracker.py <target_hash> -w wordlist.txt
`

Specify algorithm and number of processes:

`ash
python cracker.py <target_hash> -w wordlist.txt -a sha256 -t 8
`

## Project Structure

- cracker.py: Main entry point and CLI logic.
- detect.py: Hash algorithm identification.
- utils.py: Hashing utility functions.
- wordlist.txt: Sample wordlist.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Do not use it for illegal activities.
