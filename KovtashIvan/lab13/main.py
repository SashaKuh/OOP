class MusicPlayerState:
    """Базовий клас для станів плеєра"""
    def play(self, player):
        pass
    
    def pause(self, player):
        pass
    
    def stop(self, player):
        pass

class PlayingState(MusicPlayerState):
    """Стан відтворення"""
    def play(self, player):
        print("Вже відтворюється")
    
    def pause(self, player):
        print("Поставлено на паузу")
        player.state = PausedState()
    
    def stop(self, player):
        print("Зупинено")
        player.state = StoppedState()

class PausedState(MusicPlayerState):
    """Стан паузи"""
    def play(self, player):
        print("Відновлено відтворення")
        player.state = PlayingState()
    
    def pause(self, player):
        print("Вже на паузі")
    
    def stop(self, player):
        print("Зупинено")
        player.state = StoppedState()

class StoppedState(MusicPlayerState):
    """Стан зупинки"""
    def play(self, player):
        print("Починаємо відтворення")
        player.state = PlayingState()
    
    def pause(self, player):
        print("Неможливо поставити на паузу зупинений трек")
    
    def stop(self, player):
        print("Вже зупинено")

class MusicPlayer:
    """Музичний плеєр"""
    def __init__(self):
        self.state = StoppedState()
    
    def play(self):
        self.state.play(self)
    
    def pause(self):
        self.state.pause(self)
    
    def stop(self):
        self.state.stop(self)

# Демонстрація роботи
if __name__ == "__main__":
    player = MusicPlayer()
    
    print("Спроба поставити на паузу зупинений трек:")
    player.pause()
    
    print("\nПочинаємо відтворення:")
    player.play()
    
    print("\nСтавимо на паузу:")
    player.pause()
    
    print("\nВідновлюємо відтворення:")
    player.play()
    
    print("\nЗупиняємо:")
    player.stop()
