class NetworkError(Exception):
    """Base class for exceptions in this module."""
    pass

class ConnectionTimeoutError(NetworkError):
    """Raised when the network connection times out."""
    def __init__(self, message, timeout_limit):
        super().__init__(message)
        self.timeout_limit = timeout_limit

class DataTransferError(NetworkError):
    """Raised when data transfer fails."""
    def __init__(self, message, bytes_sent):
        super().__init__(message)
        self.bytes_sent = bytes_sent

def simulate_data_transfer(data):
    """Simulates a network operation that might fail."""
    import random
    
    if random.choice([True, False]):
        raise ConnectionTimeoutError("Network is too slow!", 30)
    else:
        raise DataTransferError("Packet lost during transmission.", 1024)

# --- Testing the implementation ---
if __name__ == "__main__":
    try:
        simulate_data_transfer("Sensitive Data")
    except ConnectionTimeoutError as e:
        print(f"Connection Error: {e}")
        print(f"Limit exceeded: {e.timeout_limit} seconds")
    except DataTransferError as e:
        print(f"Data Error: {e}")
        print(f"Bytes processed before failure: {e.bytes_sent}")
    except NetworkError as e:
        print(f"General Network Issue: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
