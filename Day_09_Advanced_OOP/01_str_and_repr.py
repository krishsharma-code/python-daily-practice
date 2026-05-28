class VideoGame:
    """
    Demonstrating __str__ and __repr__ magic methods.
    __str__: For users, provides a readable description.
    __repr__: For developers, provides an unambiguous representation (ideal for debugging).
    """
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

    def __str__(self):
        # Friendly representation for the end-user
        return f"'{self.title}' is a {self.genre} game rated {self.rating}/10."

    def __repr__(self):
        # Technical representation for debugging/logging
        return f"VideoGame(title='{self.title}', genre='{self.genre}', rating={self.rating})"

# Testing the implementation
if __name__ == "__main__":
    game = VideoGame("Cyberpunk 2077", "RPG", 9)
    
    # Using str() or print() calls __str__
    print(f"User View: {game}")
    
    # Using repr() or inspecting the object in a console calls __repr__
    print(f"Developer View: {repr(game)}")
