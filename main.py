import argparse
import collection
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

    collection.dataCollection(datafile, binaryfile, training_minutes)

    print("DONE ")

    thresholds = threshold.calculate_threshold(datafile, binaryfile)

    threshold_one = baseline(thresholds["AR1"], thresholds["AC1"])
    threshold_two = baseline(thresholds["AR2"], thresholds["AC2"])
    threshold_three = baseline(thresholds["AR3"], thresholds["AC3"])




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


    while True:

        time.sleep(1)
        if board.get_board_data_count() >= 800:

            data = board.get_current_board_data(800).T[:, eeg_channels]
            flattened_data = data.flatten().reshape((1, 2400))
            x = np.reshape(flattened_data, (3, 800))
            X = x.T

            electrode_one = np.mean(x[0])
			electrode_two = np.mean(x[1])
			electrode_three = np.mean(x[2])

			clench1 = electrode_one > threshold_one
			clench2 = electrode_two > threshold_two
			clench3 = electrode_three > threshold_three

			if ((clench1 and clench2) or (clench2 and clench3) or (clench1 and clench3)):
				print("GO!")
			else:
				print("STOP!")

        
    board.stop_stream()
    board.release_session()


def baseline(relax, clench):
	return (relax + clench) / 2


if __name__ == "__main__":
    main()



