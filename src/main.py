import numpy as np
import cv2

def main():
    sobel_gx = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]

    sobel_gy = [
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ]

    image = cv2.imread("imgs/man.png", cv2.IMREAD_GRAYSCALE).astype(int)
    image_list = image.tolist()

    gy = convolve_2d(image_list, sobel_gy)
    gx = convolve_2d(image_list, sobel_gx)

    # gradient magnitude
    mag = np.sqrt(np.square(gx) + np.square(gy))
    mag = np.clip(mag, 0, 255).astype(np.uint8)
    
    cv2.imshow("Sobel", mag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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
    """
    Assumes that the kernel is a square matrix of 3x3
    And that the signal CAN be a rectangular matrix
    """
    s_width = len(signal[0])
    s_height = len(signal)
    k_width = len(kernel[0])
    k_height = len(kernel)

    padded = [[0] * (s_width + 2) for _ in range(s_height + 2)]

    for y in range(s_height):
        for x in range(s_width):
            padded[y + 1][x + 1] = signal[y][x]

    output = [[0] * (s_width) for _ in range(s_height)] 

    for i in range(s_height):
        for j in range(s_width):
            sum = 0
            for k in range(k_height):
                for l in range(k_width):
                    sum += kernel[k][l] * padded[i + k][j + l]
            output[i][j] = sum

    return output

def inverse_square_matrix(matrix: list[list[int]]) -> list[list[int]]:
    inverse = [[0] * len(matrix[0])] * len(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            inverse[j][i] = matrix[i][j]
    
    return inverse

def convolve_1d_test():
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
    
if __name__ == "__main__":
    main()
