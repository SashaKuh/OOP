from abc import ABC, abstractmethod

class AudioDevice(ABC):
    @abstractmethod
    def play_audio(self):
        pass

class VideoDevice(ABC):
    @abstractmethod
    def play_video(self):
        pass

class Radio(AudioDevice):
    def play_audio(self):
        print("Playing audio on the radio Запустити аудіо на радіо")

class Television(AudioDevice, VideoDevice):
    def play_audio(self):
        print("Playing audio on the television Запустити аудіо на телебаченні")

    def play_video(self):
        print("Playing video on the television Запустити відео на телебаченні")

# Використання
def start_audio(device: AudioDevice):
    device.play_audio()

radio = Radio()
tv = Television()

start_audio(radio)
start_audio(tv)
