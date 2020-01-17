Stream EMG data from the wireless Delsys Trigno EMG sensors in real time. 

Required software: [The Trigno SDK](https://www.delsys.com/sdk/), streams EMG data using a TCP
protocol. 

See the [Delsys Trigno Documentation](https://www.delsys.com/downloads/USERSGUIDE/trigno/sdk.pdf) for more
information on streaming and packet structure to expand capabilities to your needs. Briefly, the
Trigno SDK exposes ports 50043 and 50041 for 16 channels of 4-bytes-per-sample of EMG streaming and port 50040 for
commands. To stream EMG data in real time, run the Trigno SDK--do not run EMGWorks at the same time,
since this blocks socket connections to the Trigno SDK. 

Starting the EMG data stream requires two start commands:

First send a "start" command over the Command port: `<emgSocket>.sendall(b'start')`

Then send a start trigger to the Trigno Base Station. Once the connection to the command port is
established, each command is terminated with a <CR><LF>
(carriage return, line feed) character. To send a start trigger, use: `<emgSocket>.sendall(b'TRIGGER
START\r\n\r\n')`

Also included is an `emgPlotter.py` file to plot EMG data on 12 Trigno sensors. Dependencies of this
script are `kivy` and `numpy`. 
