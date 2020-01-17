# Python package for unpacking binary data
import struct 
import time # To run the streaming loop for 5s 

EMG_IP = "127.0.0.1"
EMG_COMMAND_PORT = 50040
EMG_STREAM_PORT = 50043

# Open a socket to both the command and streaming ports
emgCommandSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
emgCommandSocket.connect((EMG_IP, EMG_COMMAND_PORT))

emgStreamSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
emgStreamSocket.connect((EMG_IP, EMG_STREAM_PORT))

# Tell the Trigno server to start broadcasting data packets 
emgCommandSocket.sendall(b'START')
emgCommandSocket.sendall(b'TRIGGER START\r\n\r\n')
startTime = time.time()
while time.time() - startTime <= 5:
    emgData = emgStreamSocket.recv(64)
    emgArray = struct.unpack("<16f", emgData) # 16 channels of 4 byte EMG data
emgCommandSocket.sendall(b'TRIGGER STOP\r\n\r\n')
