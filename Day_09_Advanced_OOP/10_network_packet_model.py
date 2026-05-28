import re

class DataPacket:
    """
    Demonstrating property decorators for strict IP validation.
    Ensures that the source and destination IP addresses follow the standard IPv4 format.
    """
    def __init__(self, source_ip, dest_ip, data):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.data = data

    @property
    def source_ip(self):
        return self._source_ip

    @source_ip.setter
    def source_ip(self, value):
        if not self._validate_ip(value):
            raise ValueError(f"Invalid Source IP format: {value}")
        self._source_ip = value

    @property
    def dest_ip(self):
        return self._dest_ip

    @dest_ip.setter
    def dest_ip(self, value):
        if not self._validate_ip(value):
            raise ValueError(f"Invalid Destination IP format: {value}")
        self._dest_ip = value

    @staticmethod
    def _validate_ip(ip):
        """Helper method to validate IPv4 address format."""
        pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
        if re.match(pattern, ip):
            # Check if each octet is between 0 and 255
            return all(0 <= int(octet) <= 255 for octet in ip.split('.'))
        return False

    def __str__(self):
        return f"Packet: [{self.source_ip} -> {self.dest_ip}] Data: {self.data}"

# Testing the implementation
if __name__ == "__main__":
    try:
        # Valid packet
        p1 = DataPacket("192.168.1.1", "10.0.0.5", "Hello World")
        print(p1)
        
        # Invalid packet (invalid IP format)
        p2 = DataPacket("256.0.0.1", "10.0.0.5", "Error Test")
    except ValueError as e:
        print(f"Validation Error: {e}")
