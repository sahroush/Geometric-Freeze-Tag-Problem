import subprocess
import numpy as np
from concurrent.futures import ThreadPoolExecutor

mx = 0

# Function to compile the C++ program
def compile_cpp_program():
    compile_command = ["g++", "-O2", "-std=c++17", "-o", "animation_feeder", "animation_feeder.cpp"]
    subprocess.run(compile_command, check=True)

# Function to run a single instance of the program and return the result
def run_instance():
    global mx
    result = subprocess.run(["./animation_feeder", str(number)], capture_output=True, text=True)
    mx = max(mx, float(result.stdout.strip()))
    print(mx)
    return float(result.stdout.strip())  # Convert result to integer

# Function to process each interval and get the maximum result
def process_interval(start, end):
    with ThreadPoolExecutor(max_workers=12) as executor:
        # Create a list of numbers for the interval
        numbers = range(start, end + 1)
        
        # Run instances in parallel
        results = list(executor.map(run_instance, numbers))
        
        # Get the maximum result from the results
        max_result = max(results)
        print(f"Maximum result for interval [{start}-{end}]: {max_result}")

# Main function to set up and run the program
def main():
    compile_cpp_program()
    
    # Define intervals
    intervals = [
        (1, 16384)
    ]
    
    # Process each interval
    for start, end in intervals:
        process_interval(start, end)

if __name__ == "__main__":
    main()
