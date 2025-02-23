#!/usr/bin/env python3

import os
import shutil
import sys

def check_disk_usage(disk, min_gb, min_percent):
	"""Return True if there is enough free disk space, false otherwise"""
	du = shutil.disk_usage(disk)
	# Calculate the percentage of free space 
	percent_free = 100 * du.free /du.total
	gigabytes_free = du.free / 2**30
	if percent_free < min_percent or gigabytes_free < min_gb:
		return False
	return True, percent_free

# Check for at least 2 GB and 10% free
if not check_disk_usage("/", min_gb=2, min_percent=10):
	print("ERROR: No enough disk space...")
	sys.exit(1)
free_space = check_disk_usage("/", 0,0)
print(f"free space {free_space[1]:.2f}")

print("Everything OK")
sys.exit(0)

def main():
    # TODO: ADD main($args) passing to function from terminal

if __name__ == "__main__":
    main()
