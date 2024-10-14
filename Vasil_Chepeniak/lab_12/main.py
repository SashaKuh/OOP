class TV: 
    def on(self): 
        print("TV is on") 
     
    def off(self): 
        print("TV is off") 
 
class DVDPlayer: 
    def on(self): 
        print("DVD Player is on") 
     
    def play(self, movie): 
        print(f"Playing movie: {movie}") 
     
    def off(self): 
        print("DVD Player is off") 
 
class SoundSystem: 
    def on(self): 
        print("Sound System is on") 
     
    def set_volume(self, level): 
        print(f"Setting volume to {level}") 
     
    def off(self): 
        print("Sound System is off") 
 
class Lights: 
    def dim(self): 
        print("Lights are dimmed") 
     
    def on(self): 
        print("Lights are on") 
 
# Facade 
class HomeTheaterFacade: 
    def __init__(self, tv, dvd_player, sound_system, lights): 
        self.tv = tv 
        self.dvd_player = dvd_player 
        self.sound_system = sound_system 
        self.lights = lights 
     
    def watch_movie(self, movie): 
        print("Get ready to watch a movie...") 
        self.lights.dim() 
        self.tv.on() 
        self.sound_system.on() 
        self.sound_system.set_volume(5) 
        self.dvd_player.on() 
        self.dvd_player.play(movie) 
     
    def end_movie(self): 
        print("Shutting down the home theater...") 
        self.dvd_player.off() 
        self.sound_system.off() 
        self.tv.off() 
        self.lights.on() 
 
if __name__ == "__main__": 
    tv = TV() 
    dvd_player = DVDPlayer() 
    sound_system = SoundSystem() 
    lights = Lights() 
     
    home_theater = HomeTheaterFacade(tv, dvd_player, sound_system, lights) 
     
    home_theater.watch_movie("The Matrix") 
    home_theater.end_movie()
