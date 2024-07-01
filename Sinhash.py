import hashlib
import argparse
import sys
import time
import logging
from colorama import Fore, Style, init
from multiprocessing import Pool, cpu_count
from tqdm import tqdm
import pyfiglet
from termcolor import colored

init(autoreset=True)

logging.basicConfig(filename='hashcrack.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Display 3D Banner
def display_banner():
    banner = pyfiglet.Figlet(font='slant').renderText('SINISTER X')
    print(colored(banner, 'red', attrs=['bold']))
    shadow = pyfiglet.Figlet(font='slant').renderText('SINISTER X')
    print(colored(shadow, 'green'))

display_banner()

def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Hash Cracker - Crack hashed passwords using various techniques.")
    parser.add_argument("target_hash", help="Target hash to crack")
    parser.add_argument("wordlist", help="Path to the wordlist file")
    parser.add_argument("-t", "--hash-type", choices=hashlib.algorithms_available, default="sha256", help="Hash algorithm (default: sha256)")
    parser.add_argument("-s", "--salt", help="Optional salt value")
    parser.add_argument("-r", "--rainbow-table", help="Path to precomputed rainbow table")
    parser.add_argument("-b", "--benchmark", action="store_true", help="Display benchmarking information")
    return parser.parse_args()

def load_wordlist(wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            words = [line.strip() for line in file]
        return words
    except FileNotFoundError:
        print(Fore.RED + "Wordlist file not found.")
        logging.error("Wordlist file not found.")
        sys.exit(1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProcess interrupted by user while loading wordlist. Exiting gracefully...")
        logging.warning("Process interrupted by user while loading wordlist.")
        sys.exit(0)

def hash_word(word, hash_type, salt=None):
    hasher = hashlib.new(hash_type)
    if salt:
        hasher.update(salt.encode('utf-8'))
    hasher.update(word.encode('utf-8'))
    return hasher.hexdigest()

def crack_hash(target_hash, wordlist, hash_type, salt=None, rainbow_table=None):
    if rainbow_table:
        return check_rainbow_table(target_hash, rainbow_table)
    
    words = load_wordlist(wordlist)
    try:
        with Pool(cpu_count()) as pool:
            args = [(word, hash_type, salt) for word in words]
            with tqdm(total=len(words), desc="Cracking hash") as pbar:
                for word, hashed in zip(words, pool.starmap(hash_word, args)):
                    pbar.update(1)
                    if hashed == target_hash:
                        print(Fore.GREEN + f"Password found: {word}")
                        logging.info(f"Password found: {word}")
                        return word
        print(Fore.RED + "Password not found in wordlist.")
        logging.info("Password not found in wordlist.")
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProcess interrupted by user. Exiting gracefully...")
        logging.warning("Process interrupted by user.")
        sys.exit(0)
    return None

def check_rainbow_table(target_hash, rainbow_table):
    try:
        with open(rainbow_table, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                word, precomputed_hash = line.strip().split(':')
                if precomputed_hash == target_hash:
                    print(Fore.GREEN + f"Password found in rainbow table: {word}")
                    logging.info(f"Password found in rainbow table: {word}")
                    return word
        print(Fore.RED + "Password not found in rainbow table.")
        logging.info("Password not found in rainbow table.")
        return None
    except FileNotFoundError:
        print(Fore.RED + "Rainbow table file not found.")
        logging.error("Rainbow table file not found.")
        sys.exit(1)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProcess interrupted by user. Exiting gracefully...")
        logging.warning("Process interrupted by user.")
        sys.exit(0)

def benchmark(func):
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(Fore.YELLOW + f"Time taken: {elapsed_time:.2f} seconds")
            logging.info(f"Time taken: {elapsed_time:.2f} seconds")
            return result
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\nProcess interrupted by user. Exiting gracefully...")
            logging.warning("Process interrupted by user.")
            sys.exit(0)
    return wrapper

@benchmark
def run_cracker(args):
    crack_hash(args.target_hash, args.wordlist, args.hash_type, args.salt, args.rainbow_table)

if __name__ == "__main__":
    try:
        args = parse_args()
        run_cracker(args)
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\nProcess interrupted by user. Exiting gracefully...")
        logging.warning("Process interrupted by user.")
        sys.exit(0)
