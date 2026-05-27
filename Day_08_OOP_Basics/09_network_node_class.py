class NetworkNode:
    """
    Represents a server node in a network.
    """
    def __init__(self, ip_address, port, status="Offline"):
        self.ip_address = ip_address
        self.port = port
        self.status = status

    def connect(self):
        self.status = "Online"
        print(f"Node {self.ip_address}:{self.port} is now {self.status}.")

    def disconnect(self):
        self.status = "Offline"
        print(f"Node {self.ip_address}:{self.port} has been disconnected.")

    def get_info(self):
        return f"Node Info -> IP: {self.ip_address}, Port: {self.port}, Status: {self.status}"

# Networking Simulation
node1 = NetworkNode("192.168.1.1", 8080)
print(node1.get_info())

node1.connect()
print(node1.get_info())

node1.disconnect()
