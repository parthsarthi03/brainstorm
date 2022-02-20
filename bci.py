import argparse
import time
import numpy as np

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations

def main():
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

    averages = []
    # time_per_decision = 1.0
    # sampling_rate = BoardShim.get_sampling_rate(1)
    # print(sampling_rate)

    board.prepare_session()

    board.start_stream(45000, args.streamer_params)
    for _ in range(2):
        time.sleep(4)
        data = board.get_board_data().T[:, eeg_channels]
        # print(data)
        # print(data.shape)
        averages = np.mean(data, axis=0)
    print("Averages:")
    print(averages)
    # get all data
    # data = board.get_current_board_data(256) # do i need to pass in anything?
    board.stop_stream()
    board.release_session()

if __name__ == "__main__":
    main()






