#!/usr/bin/python3
import sys
from subprocess import PIPE, Popen
#Uses command line to create and run program using imported libraries to capture output and utilize the elements
def cmdline(command):
    w_process = Popen(
        args=command,
        stdout=PIPE,
        shell=True,
        universal_newlines=True
        )
    return w_process.communicate()[0]

#Changes pcap file to .txt and writes the information of TCP streams to it
pcap_file = sys.argv[1]
output_file_name = pcap_file.split('.')[0] + '_streams.txt'
output_file = open(output_file_name, 'w')
counter = 0

#Continuous loop separating different sections of stream and checking for end of index to terminate program
while True:
    cmd = "tshark -r %s -z follow,tcp,ascii,%s" %(pcap_file, counter)
    stream = cmdline(cmd)
    stream = stream.split('=====================================================\n')[1]
    stream += '\n====================\n'
    if "node 0: :0" not in stream:
        output_file.write(stream)
    else:
        break
    counter += 1
#Closing file after finished
output_file.close()