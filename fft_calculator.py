import numpy as np
import sys

def calculate_fft(input_array):
    return np.fft.fft(input_array)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fft_calculator.py <space-separated list of numbers>")
        sys.exit(1)

    try:
        input_array = list(map(float, sys.argv[1:]))
    except ValueError:
        print("Please provide a valid list of numbers.")
        sys.exit(1)

    fft_result = calculate_fft(input_array)
    print("FFT Result:", fft_result)

if __name__ == "__main__":
    main()