#!/bin/bash

# WARNING: Run this only in a dedicated test repository!
# This will generate ~2.5 GB of random data, commit it, and push it to the 'master' branch.

# Total batches: 25. Each batch creates 10 files of 10MB (100MB per batch).
# Total size: 25 * 100MB = 2.5 GB

BRANCH="master"

for batch in {1..25}; do
    echo "--- Processing Batch $batch of 25 (~100MB) ---"
    
    for file_num in {1..10}; do
        FILE_NAME="stress_test_data_${batch}_${file_num}.bin"
        
        # Using /dev/urandom ensures the data is uncompressible by Git
        dd if=/dev/urandom of="$FILE_NAME" bs=1M count=10 status=none
        
        git add "$FILE_NAME"
    done
    
    echo "Committing batch $batch..."
    git commit -m "Stress test data: Add batch $batch (100MB)"
    
    echo "Pushing batch $batch to remote..."
    # We push incrementally so the remote server doesn't drop the connection
    git push origin $BRANCH
    
    echo "Batch $batch complete."
done

echo "Finished! Added ~2.5 GB of uncompressible data to the repository."
