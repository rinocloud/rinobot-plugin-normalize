import sys
import os
import argparse
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('--column', type=int, required=True)
    parser.add_argument('--algo', type=str, choices=['sum', 'max'], required=True)

    args = parser.parse_args()
    filepath = args.filepath

    filename_without_ext = os.path.splitext(filepath)[0]
    data = np.loadtxt(filepath)

    col = data[:, args.column - 1]

    if args.algo == "sum":
        data[:, args.column - 1] = col/col.sum()
    if args.algo == "max":
        data[:, args.column - 1] = col/col.max()

    np.savetxt(filename_without_ext + '-normalized.txt', data)
