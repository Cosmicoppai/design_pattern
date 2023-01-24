"""
    You have been asked to create a playlist application that will be used on Android devices.
We will assume that each playlist can be composed of songs or other playlists, or a combination of both.

    Your project manager has told you that the composite pattern is best used in this situation.
The following UML class diagram that communicates the application’s objects and relationships using the composite pattern.

    In this assignment you are required to complete the provided code.
(Note: With the exception of the Playlist class, you do not need to actually implement the methods, just write filler comments (e.g. // play song).
With the Playlist class, write out the method to add songs to the playlist).

"""
from abc import ABC, abstractmethod
from typing import List


class IComponent(ABC):

    @abstractmethod
    def play(self) -> None:
        """Playing song"""

    @abstractmethod
    def set_playback_speed(self, speed: float) -> None:
        """Setting Playback speed"""

    @abstractmethod
    def get_name(self) -> None:
        """printing name"""


class PlayList(IComponent):

    def __init__(self, playlist_name: str, playlist: List[IComponent] = None):
        self.playlist_name: str = playlist_name
        self.playlist = playlist or []

    def play(self) -> None:
        """
        Play all songs from playlist
        """
        for comp in self.playlist:
            comp.play()

    def set_playback_speed(self, speed: float):
        for comp in self.playlist:
            comp.set_playback_speed(speed)

    def get_name(self):
        print(self.playlist_name)

    def add(self, component: IComponent):
        self.playlist.append(component)

    def remove(self, component: IComponent):
        self.playlist.remove(component)


class Song(IComponent):

    def __init__(self, song_name: str, artist: str, speed: float = 1.0):
        self.song_name: str = song_name
        self.artist: str = artist
        self.speed: float = speed

    def play(self):
        print(f"Playing {self.song_name} at {self.speed}")

    def set_playback_speed(self, speed: float):
        self.speed = speed

    def get_name(self):
        print(self.song_name)

    def get_artist(self):
        print(self.artist)


if __name__ == "__main__":
    study_playlist = PlayList(playlist_name="study")
    song1 = Song("Mahou no Jutaan", "Kawasaki Takaya")
    song2 = Song("Akuma no Ko", "Higuchi Ai")
    study_playlist.add(song1)
    study_playlist.add(song2)

    experiment_playlist = PlayList(playlist_name="experiment")

    e_song1 = Song("Don't Worry", "")
    e_song2 = Song("Chaand Taare", "Abhijeet")

    experiment_playlist.add(e_song1)
    experiment_playlist.add(e_song2)

    experiment_playlist.set_playback_speed(1.25)

    study_playlist.add(experiment_playlist)

    study_playlist.play()

