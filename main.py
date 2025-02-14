import fuzzer

if __name__ == "__main__":
    # Adjust iterations and delay as needed
    fuzzer.fuzz_target(iterations=10000, delay=0.005)