import argparse
import serial
import datetime
import os

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument(
    "-d", "--device", help="device to read from", default="COM12")
parser.add_argument("-s", "--speed", help="speed in bps",
                    default=9600, type=int)
args = parser.parse_args()

outputFilePath = os.path.join(os.path.dirname(__file__),
                              datetime.datetime.now().strftime("%Y-%m-%dT%H.%M.%S") + ".txt")

data = []

with serial.Serial(args.device, args.speed) as ser, open(outputFilePath, mode='wb') as outputFile:
    print("Logging started. Ctrl-C to stop.")
    try:
        while True:
            d = ser.readline().strip().decode('ascii')
            # print(data)  # uncomment this line to debug the coming data

            val = d.split(',')
            data.append([float(val[i]) for i in range(len(val))])

    except KeyboardInterrupt:
        print("Logging stopped, saving to file")

    for i in range(len(data[0])):
        for line in data:
            outputFile.write(str(line[i]).encode('ascii'))
            outputFile.write(b',')
        outputFile.write(b'\n')

    print("Data saved to", outputFilePath)
    outputFile.flush()
    outputFile.close()
