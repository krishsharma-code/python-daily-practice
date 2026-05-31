class Camera:
    """Class representing a camera device."""
    def take_photo(self):
        print("📸 Photo captured successfully.")

class MusicPlayer:
    """Class representing a music player device."""
    def play_music(self):
        print("🎵 Playing your favorite tracks.")

class WebBrowser:
    """Class representing a web browser."""
    def browse(self):
        print("🌐 Browsing the internet...")

class SmartPhone(Camera, MusicPlayer, WebBrowser):
    """Demonstrates Multiple Inheritance.
    SmartPhone inherits functionality from Camera, MusicPlayer, and WebBrowser.
    """
    def make_call(self):
        print("📞 Calling home...")

# --- Testing the implementation ---
if __name__ == "__main__":
    my_phone = SmartPhone()
    
    print("--- Smartphone Capabilities ---")
    my_phone.take_photo()
    my_phone.play_music()
    my_phone.browse()
    my_phone.make_call()
    
    print("\n--- Method Resolution Order (MRO) ---")
    # MRO defines the order in which Python looks for a method in a hierarchy.
    for cls in SmartPhone.mro():
        print(cls)
