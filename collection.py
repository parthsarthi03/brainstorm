import argparse
import time
import threshold
import numpy as np
from csv import writer

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations
from datetime import datetime, timedelta



def main():

    datafile = "data.csv"
    binaryfile = "binary.csv"
    training_minutes = 2
    dataCollection(datafile, binaryfile, training_minutes)


def dataCollection(datafile, binaryfile, training_minutes):
    BoardShim.enable_dev_board_logger()

    parser = argparse.ArgumentParser()

    # arguments that the Ganglion board needs
    parser.add_argument('--board-id', type=int, help='board id, check docs to get a list of supported boards', required=False, default=1)
    parser.add_argument('--timeout', type=int, help='timeout for device discovery or connection', required=False, default=0)
    parser.add_argument('--serial-port', type=str, help='serial port', required=False, default='/dev/cu.usbmodem11')
    parser.add_argument('--mac-address', type=str, help='other info', required=False, default='')

    # have streamer params -- empty
    parser.add_argument('--streamer-params', type=str, help='streamer params', required=False, default='')

    args = parser.parse_args()

    params = BrainFlowInputParams()
    # write the parameters to params
    #params.board_id = args.board_id
    params.timeout = args.timeout 
    params.serial_port = args.serial_port
    params.mac_address = args.mac_address

    board = BoardShim(args.board_id, params)
    eeg_channels = [2, 3, 4]
    action_counter = 0

    board.prepare_session()

    board.start_stream(100000, args.streamer_params)

    now = datetime.now()

    while datetime.now() <= now + timedelta(minutes=training_minutes):

        binary_val = 0
        if action_counter < 4:
            print("Rest")
        else:
            print("Clench")
            binary_val = 1
        action_counter = (action_counter + 1) % 8

        time.sleep(1)
        if board.get_board_data_count() >= 800:
            data = board.get_current_board_data(800).T[:, eeg_channels]
            flattened_data = data.flatten().reshape((1, 2400))

            with open("data.csv", "w") as f:
                np.savetxt(f, flattened_data, delimiter=',', fmt='%f')
            with open("binary.csv", "w") as f:
                np.savetxt(f, [binary_val], delimiter=',', fmt='%f') 

        
    board.stop_stream()
    board.release_session()


if __name__ == "__main__":
    main()






