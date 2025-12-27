from dataclasses import dataclass
@dataclass
class Track:
    id : int
    name : str
    album_id : int
    media_type_id : int
    genre_id : int
    composer : str
    milliseconds : int
    bytes : int
    unit_price : int

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
    def __str__(self):
        return f"Traccia {self.id},{self.name},{self.album_id}"