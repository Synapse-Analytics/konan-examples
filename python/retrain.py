import os
import argparse
import requests
import pandas as pd

def retraining_func(data_path, output_base_path):
    """Model training function

    :param data_path: csv path of training data with 'y' as the target
    :param output_path: retraining output base path to write retraining artifacts
    """

    # TODO: read data
    data = pd.read_csv(data_path)

    # dummy retraining
    import time

    for i in range(5):
        time.sleep(10)
        print("still training")

    # TODO: save weights/model file in path provided 

    # write dummy weights file
    f = open(f'{output_base_path}/weights.txt', "w")
    f.write("I am heavier")
    f.close()

    print("retraining successfully completed")

    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='konan retraining')

    parser.add_argument('-d', '--data_path', help='path to re-training data')
    parser.add_argument('-o', '--output_path', help='base path to write retraining artifacts')

    args = parser.parse_args()

    # TODO: call retraining function
    y = retraining_func(args.data_path)
