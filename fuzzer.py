import time
from input_generator import generate_random_string
import target


def fuzz_target(iterations=1000, delay=0.01):
    """
    Fuzzes the target function with generated inputs.

    :param iterations: Number of input attempts.
    :param delay: Delay between each attempt to simulate real-time testing.
    """
    print("Commencing brute force fuzzing. Prepare for inefficiency!")
    for i in range(iterations):
        # Generate input
        input_data = generate_random_string()
        try:
            # Pass input to the target function
            result = target.vulnerable_function(input_data)
        except Exception as e:
            print(f"Crash detected on iteration {i} with input: {input_data}")
            print(f"Exception: {e}")
            # Optionally, log the input or take further action
            break  # Stop on first detected issue
        time.sleep(delay)
    else:
        print("Fuzzing complete without detecting crashes.")