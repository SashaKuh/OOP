class Instrument:

    def play(self):

        pass

class Guitar(Instrument):

    def play(self):

        return "Грає гітара: бринь-бринь"

class Piano(Instrument):

    def play(self):

        return "Грає піаніно: дінь-дінь"

class Orchestra:

    def __init__(self):

        self.instruments = []


    def add_instrument(self, instrument):

        self.instruments.append(instrument)


    def play_music(self):

        for instrument in self.instruments:

            print(instrument.play())


# Приклад використання

orchestra = Orchestra()

orchestra.add_instrument(Guitar())

orchestra.add_instrument(Piano())

orchestra.play_music()






























