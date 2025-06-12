import numpy as np

def main():
    print("\n")
    arr1 = [1,2,3,4,5]
    arr2 = [2,1]

    print(f"Array 1 is {arr1}")
    print(f"Array 2 is {arr2}\n")

    answer: list[int] = convolve_1d_full(arr1, arr2)
    correct_answer: list[int] = np.convolve(arr1, arr2).tolist()

    print(f"Convolve: {answer}")
    print(f"Answer should be {correct_answer}\n")
    print("SUCCESS" if answer == correct_answer else "FAIL")


def convolve_1d_full(signal: list[int], kernel: list[int]) -> list[int]:
    s = len(signal)
    k = len(kernel)
    convolved: list[int] = [0] * len(signal)
    reversed = kernel.copy()
    reversed.reverse()

    for i in range(len(signal) + len(reversed) - 1):

    return convolved

if __name__ == "__main__":
    main()
