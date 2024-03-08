import hashlib
import argparse

parser = argparse.ArgumentParser(description='Hash Algorithm Identifier')
parser.add_argument('-t', '--target-hash', help='The target hash you want to match against', required=True)
parser.add_argument('-r', '--result-of-hash', help='The plaintext result to hash', required=True)
parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help='Show program\'s version number and exit.')

args = parser.parse_args()


target_hash = args.target_hash
plaintext = args.result_of_hash

# add algos as needed
algos = [    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
    'blake2b', 'blake2s'
]

def hash_with_algo(algo, plaintext):
    if algo in ['blake2b', 'blake2s']:
        hasher = getattr(hashlib, algo)(digest_size=32)
        hasher.update(plaintext.encode())
        return hasher.hexdigest()
    else:
        hasher = getattr(hashlib, algo)()
        hasher.update(plaintext.encode())
        return hasher.hexdigest()

# check each algo
for algo in algos:
    result = hash_with_algo(algo, plaintext)
    print(f"{algo}: {result}")
    if result == target_hash:
        print(f"Match found with {algo}!")
        break
else:
    print("No match found with the tested algos.")
