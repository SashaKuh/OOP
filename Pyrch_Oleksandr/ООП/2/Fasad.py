
class FlightBooking:
    def book_flight(self) -> str:
        return "Flight booked"

class HotelBooking:
    def book_hotel(self) -> str:
        return "Hotel booked"

class TaxiBooking:
    def book_taxi(self) -> str:
        return "Taxi booked"

class TravelFacade:
    def __init__(self):
        self.flight = FlightBooking()
        self.hotel = HotelBooking()
        self.taxi = TaxiBooking()

    def book_trip(self):
        result = []
        result.append(self.flight.book_flight())
        result.append(self.hotel.book_hotel())
        result.append(self.taxi.book_taxi())
        return "\n".join(result)

if __name__ == "__main__":
    travel = TravelFacade()
    print(travel.book_trip())
