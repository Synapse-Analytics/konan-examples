import os
import argparse
import requests
import pandas as pd

def retraining_func(data_path):
    """Model training function

    :param data_path: csv path of training data with 'y' as the target
    :param webhook: webhook string used to notify backend that training is done
    """

    # TODO: read data
    data = pd.read_csv(data_path)

    # dummy retraining
    import time

    for i in range(5):
        time.sleep(10)
        print("still training")

    # TODO: save weights/model file in path provided in env variable
    retraining_output_path = os.getenv("RETRAINING_ARTIFACTS_PATH")

    # write dummy weights file
    f = open(f'{retraining_output_path}/weights.txt', "w")
    f.write("I am heavier")
    f.close()

    print("retraining successfully completed")

    return

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='konan retraining')


    parser.add_argument('-d', '--data_path', help='path to re-training data')
    parser.add_argument('-w', '--webhook', help='webhook to notify backend on when retraining is done')

    args = parser.parse_args()

    # TODO: call retraining function
    y = retraining_func(args.data_path)

    # TODO: notify backend that retraining is done
    requests.get(args.webhook)
    print("Acknowledgement sent")


