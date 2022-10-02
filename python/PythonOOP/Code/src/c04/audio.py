from pathlib import Path

class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:

        print("i know this file", self.ext)
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath


class MP3File(AudioFile):
    ext = ".mp3"

    def play(self) -> None:
        print(f"Playing {self.filepath} as mp3")


class WaveFile(AudioFile):
    ext = ".wav"

    def play(self) -> None:
        print(f"Playing {self.filepath} as wave")


class OggFile(AudioFile):
    ext = ".ogg"

    def play(self) -> None:
        print(f"Playing {self.filepath} as ogg")


class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath


    def play(self) -> None:
        print(f"Playing {self.filepath} as flac")



p_1 = MP3File(Path("Hello.mp3"))
p_1.play()

