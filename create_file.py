import os
import random
import string

# --- CONFIGURATION ---
FOLDER_NAME = "real_world_stress_data"
NUM_FILES = 5  # Change this to your desired N
TARGET_SIZE_MB = 9.9
# ---------------------

# A pool of words to simulate "real" text data (less compressible than single chars)
WORD_POOL = ["status", "error", "request_id", "timestamp", "payload", "metadata", 
             "transaction", "gateway", "cluster", "node", "reconcile", "active"]

def create_stress_folder(folder, n, size_mb):
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    target_bytes = int(size_mb * 1024 * 1024)
    
    for i in range(1, n + 1):
        file_path = os.path.join(folder, f"stress_data_{i:03d}.txt")
        print(f"Generating {file_path}...")
        
        with open(file_path, "w") as f:
            current_bytes = 0
            while current_bytes < target_bytes:
                # Create a "line" of random words and numbers
                line = f"{random.choice(WORD_POOL)}={random.randint(1000, 9999)} " \
                       f"log_msg='{''.join(random.choices(string.ascii_letters, k=20))}'\n"
                f.write(line)
                current_bytes += len(line)
                
    print(f"\nSuccessfully created {n} files in '{folder}'")

if __name__ == "__main__":
    create_stress_folder(FOLDER_NAME, NUM_FILES, TARGET_SIZE_MB)
