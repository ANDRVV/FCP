class stripPacket:
    def __init__(self):
        pass

    def disassembly(self, packet : bytes) -> None:
        fulltag = []
        for t in packet[0:6]:
            if packet.index(t) % 2 != 0:
                fulltag.append(chr(t))
        if "fcp" != "".join(fulltag):
            raise Exception("Packet not valid: FCP Tag not found.")
        self.ch = int.from_bytes(packet[6:8], byteorder = "big")
        fullraw = []
        for i in packet[8:]:
            if packet.index(i) % 2 != 0:
                fullraw.append(i)
        self.rw = fullraw
    
    @property
    def channel(self) -> int:
        """
        Get the channel.
        """
        return self.ch

    @property
    def raw(self) -> list[int]:
        """
        Get the raw.
        """
        return self.rw