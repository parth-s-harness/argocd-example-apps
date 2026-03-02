# Save this as create_file.py and run: python3 create_file.py
import os

file_name = "large_text_data.txt"
# 9.9 MB in bytes
target_size = int(9.9 * 1024 * 1024) 

# We'll use a readable pattern
pattern = "This is a line of text for testing purposes. Line ID: "
pattern_len = len(pattern) + 10 # Adding buffer for the counter

with open(file_name, "w") as f:
    current_size = 0
    counter = 0
    while current_size < target_size:
        line = f"{pattern}{counter}\n"
        f.write(line)
        current_size += len(line)
        counter += 1

print(f"Created {file_name} with size: {os.path.getsize(file_name) / (1024*1024):.2f} MB")
