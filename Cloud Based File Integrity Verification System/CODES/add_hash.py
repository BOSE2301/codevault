import hashlib

def generate_file_hash(file_path):
    hasher = hashlib.sha256()  # can use other hashing algorithms as well
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()

if __name__ == "__main__":
    csv_file_path = 'weather.csv'  # Ensure this path matches uploaded file
    file_hash = generate_file_hash(csv_file_path)
    print(f'Generated hash: {file_hash}')
