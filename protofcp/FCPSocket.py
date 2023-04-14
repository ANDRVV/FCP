from . import assemblr, disassemblr
from .consts import *
from scapy.all import conf
from cryptography.utils import CryptographyDeprecationWarning
import warnings
warnings.filterwarnings(action = "ignore", category = CryptographyDeprecationWarning)

class FCPSocket:
    def __init__(self, channel: Channels):
        self.ch = channel
        self.sock = conf.L2socket()

    def send(self, raw: bytes):
        packet = assemblr.buildPacket(self.ch, raw).assembly()
        self.sock.send(packet)

    def recv(self):
        while True:
            data = self.sock.recv()
            if data is not None:
                data = bytes(data)
                try:   
                    fulltag = []
                    for t in data[0:6]:
                        if data.index(t) % 2 != 0:
                            fulltag.append(chr(t))
                    if "fcp" != "".join(fulltag):
                        continue
                except:
                    continue 
                dis = disassemblr.stripPacket()
                dis.disassembly(data)
                if dis.channel == self.ch:
                    return bytes(dis.raw)
            


        