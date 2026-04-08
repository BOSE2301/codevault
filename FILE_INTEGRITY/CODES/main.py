import subprocess
import sys

# Use the correct path to Python installation
PYTHON_PATH = '/Library/Frameworks/Python.framework/Versions/3.12/bin/python3'

def run_script(script_name):
    try:
        subprocess.run([PYTHON_PATH, script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_name}: {e}")
        sys.exit(1)

def main():
    print("Uploading file to S3...")
    run_script('upload_to_s3.py')
    
    print("Generating file hash...")
    run_script('add_hash.py')
    
    print("Storing file hash on blockchain...")
    run_script('blockchain.py')
    
    print("Saving hash to S3...")
    run_script('save_hash_s3.py')
    
    print("Retrieving file hash from blockchain...")
    run_script('view.py')
    
    print("All operations completed successfully!")

if __name__ == "__main__":
    main()
