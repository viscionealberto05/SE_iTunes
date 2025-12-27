from dataclasses import dataclass
@dataclass
class Album:
    id : int
    title : str
    artist_id : int

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return f"Album {self.id},{self.title},{self.artist_id}"


