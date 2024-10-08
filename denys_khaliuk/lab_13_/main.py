class AudioSystem:
    def on(self):
        print("Аудіо система увімкнена.")

    def set_volume(self, level):
        print(f"Гучність аудіо встановлена на рівень {level}.")

    def off(self):
        print("Аудіо система вимкнена.")


# Підсистема: Відеоплеєр
class VideoPlayer:
    def on(self):
        print("Відеоплеєр увімкнений.")

    def play(self, movie):
        print(f"Фільм '{movie}' відтворюється.")

    def off(self):
        print("Відеоплеєр вимкнений.")


# Підсистема: Субтитри
class Subtitles:
    def on(self):
        print("Субтитри увімкнені.")

    def off(self):
        print("Субтитри вимкнені.")


# Клас фасаду
class HomeTheaterFacade:
    def __init__(self, audio, video, subtitles):
        self.audio = audio
        self.video = video
        self.subtitles = subtitles

    def watch_movie(self, movie):
        print("Підготовка до перегляду фільму...")
        self.audio.on()
        self.audio.set_volume(10)
        self.video.on()
        self.video.play(movie)
        self.subtitles.on()

    def end_movie(self):
        print("Завершення перегляду фільму...")
        self.subtitles.off()
        self.video.off()
        self.audio.off()


# Використання фасаду
audio_system = AudioSystem()
video_player = VideoPlayer()
subtitles = Subtitles()

home_theater = HomeTheaterFacade(audio_system, video_player, subtitles)

# Включення фільму
home_theater.watch_movie("Інтерстеллар")

# Завершення фільму
home_theater.end_movie()
