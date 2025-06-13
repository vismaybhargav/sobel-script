import numpy as np

def main():
    print("\n")
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2]

    print(f"Array 1 is {arr1}")
    print(f"Array 2 is {arr2}\n")

    answer: list[int] = convolve_1d(arr1, arr2)
    correct_answer: list[int] = np.convolve(arr1, arr2).tolist()

    print(f"Convolve: {answer}")
    print(f"Answer should be {correct_answer}\n")
    print("SUCCESS" if answer == correct_answer else "FAIL")


def convolve_1d(signal: list[int], kernel: list[int]) -> list[int]:
    slen = len(signal)
    klen = len(kernel)

    convolved: list[int] = []

    for i in range(slen + klen - 1):
        curr = 0
        for k in range(klen):
            # This should be where the current summed value should be in the final list
            curr_idx = i - k
            if curr_idx >= 0 and curr_idx < slen:
                curr += signal[curr_idx] * kernel[k]
        convolved.append(curr)
    return convolved

def convolve_2d(signal: list[list[int]], kernel: list[list[int]]) -> list[list[int]]:
    return [[]]


if __name__ == "__main__":
    main()
