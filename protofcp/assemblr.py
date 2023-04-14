from . import consts 

class buildPacket:
    def __init__(self, channel: consts.Channels, raw: bytes):
        self.channel = channel
        self.raw = raw

    def assembly(self) -> bytes:
        packet = bytes()
        for i in consts.FCP:
            packet += int(i).to_bytes(2, byteorder = "big")
        packet += int(self.channel).to_bytes(2, byteorder = "big")
        for r in self.raw:
            packet += int(r).to_bytes(2, byteorder = "big")
        return packet

