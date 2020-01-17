Currently, this Motive NatNet Client doesn't actually stream pixel data--it just triggers the start
and stop of recording in Motive through message packets. Documentation and download
[here](https://optitrack.com/products/natnet-sdk/). The available commands and ports aren't
documented, but you can infer them from reading the source code in the downloaded NatNet folder. 

For Python, either add the NatNetClient folder to your PYTHONPATH, or manually add it to path using
`sys.path.append(<PATH TO NATNETCLIENT>)` at the top of your script. 
