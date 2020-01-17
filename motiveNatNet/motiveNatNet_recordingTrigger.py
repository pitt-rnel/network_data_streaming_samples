import sys 
import time 

NATNET_PATH = "</PATH TO NATNET FOLDER/>"
MOCAP_IP = "127.0.0.1"
MOCAP_PORT = 1510 
sys.path.append(NATNET_PATH)

from NatNetClient import NatNetClient
mocapClient = NatNetClient()
mocapSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
nameOfFile = "nameOfMocapFile"
mocapClient.sendCommand(2, "SetRecordTakeName " + nameOfFile, mocapSocket, (MOCAP_IP, MOCAP_PORT))
mocapClient.sendCommand(2, "StartRecording", mocapSocket, (MOCAP_IP, MOCAP_PORT))
time.sleep(5) # 5s recording
mocapClient.sendCommand(2, "StopRecording", mocapSocket, (MOCAP_IP, MOCAP_PORT))

