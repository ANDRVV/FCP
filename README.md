# FCP
**FCP** stands for **Fast Channel Protocol**, a protocol used to route on "**channels**" and send or receive data. 
This protocol does not use a **buffer**, which is specially designed for local network addresses for a camera/audio device connection.
This protocol **has much the same function as radio frequencies**, unlimited clients can send/receive information without physical addresses.

## How to install:

`pip install protofcp`

## Send message in channel 1:
```python
import protofcp

sock = protofcp.FCPSocket(protofcp.Channels.CHANNEL_01)
while True:
    msg = input("> ")
    sock.send(msg.encode())
```

## Receive message in channel 1:
```python
import protofcp

sock = protofcp.FCPSocket(protofcp.Channels.CHANNEL_01)
msg = sock.recv()
print(msg)
```

−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−

Copyright 2023 Andrea Vaccaro

Apache License 2.0