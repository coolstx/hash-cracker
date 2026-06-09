import sys
import argparse
import time
from multiprocessing import Pool, cpu_count
from utils import hash_text
from detect import detect_hash

def check_password(args):
    """Worker function to check a single password against the target hash."""
    password, target_hash, algo = args
    if hash_text(password, algo) == target_hash:
        return password
    return None

def main():
    parser = argparse.ArgumentParser(description="Professional Hash Cracker CLI")
    parser.add_argument("hash", help="The target hash to crack")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to the wordlist file")
    parser.add_argument("-a", "--algo", help="Hashing algorithm (md5, sha1, sha256, sha512). Auto-detects if omitted.")
    parser.add_argument("-t", "--threads", type=int, default=cpu_count(), help="Number of parallel processes (default: CPU count)")

    args = parser.parse_args()

    target_hash = args.hash.lower().strip()
    algo = args.algo or detect_hash(target_hash)

    if not algo:
        print(f"[-] Error: Could not detect algorithm for hash: {target_hash}")
        print("    Please specify it manually using -a/--algo.")
        sys.exit(1)

    print(f"[*] Target Hash: {target_hash}")
    print(f"[*] Detected Algorithm: {algo}")
    print(f"[*] Using {args.threads} parallel processes.")

    start_time = time.time()
    found_password = None

    try:
        with open(args.wordlist, 'r', encoding='utf-8', errors='ignore') as f:
            # Use a generator to save memory for large wordlists
            def password_generator():
                for line in f:
                    p = line.strip()
                    if p:
                        yield (p, target_hash, algo)

            print(f"[*] Starting attack...")
            
            with Pool(processes=args.threads) as pool:
                # Using imap_unordered with a generator is memory efficient
                for result in pool.imap_unordered(check_password, password_generator(), chunksize=1000):
                    if result:
                        found_password = result
                        pool.terminate()
                        break
    except FileNotFoundError:
        print(f"[-] Error: Wordlist file not found: {args.wordlist}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted by user.")
        sys.exit(0)

    duration = time.time() - start_time

    if found_password:
        print(f"\n[+] SUCCESS! Password found: {found_password}")
        print(f"[*] Time taken: {duration:.2f} seconds")
    else:
        print(f"\n[-] FAILED. Password not found in wordlist.")
        print(f"[*] Time taken: {duration:.2f} seconds")

if __name__ == "__main__":
    main()
