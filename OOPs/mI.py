"""Create class the class name is monday
monday have 4 methode


i have  a class Monday
    avl seat in monday - 60
    seat booked --- 30
    seat cancel - 12
    current sets on monday== ?

i have  a class Tuesday
    avl seat in Tuesday - 60
    seat booked --- 23
    seat cancel - 18
    current sets on Tuesaday== ?



i have  a class Wednesday
    avl seat in Tuesday - 60
    seat booked --- 45
    seat cancel - 0
    current sets on wednesday== ?


class Chcek do a multiple inhheritance and which day how many seat avl."""

class Monday:
    def avl_seat(self, mon_avl):
        self.mon_avl = mon_avl
        return mon_avl

    def seat_booked(self, mon_booked):
        self.mon_booked = mon_booked
        return mon_booked

    def seat_cancel(self, mon_cancel):
        self.mon_cancel = mon_cancel
        return mon_cancel

    def current_seat(self):
        mon_current = self.mon_avl - self.mon_booked + self.mon_cancel
        print("Monday current seats:", mon_current)


class Tuesday:
    def avl_seat(self, tues_avl):
        self.tues_avl = tues_avl
        return tues_avl

    def seat_booked(self, tues_booked):
        self.tues_booked = tues_booked
        return tues_booked

    def seat_cancel(self, tues_cancel):
        self.tues_cancel = tues_cancel
        return tues_cancel

    def current_seat(self):
        tues_current = self.tues_avl - self.tues_booked + self.tues_cancel
        print("Tuesday current seats:", tues_current)


class Wednesday(Monday, Tuesday):
    def avl_seat(self, wed_avl):
        self.wed_avl = wed_avl
        return wed_avl

    def seat_booked(self, wed_booked):
        self.wed_booked = wed_booked
        return wed_booked

    def seat_cancel(self, wed_cancel):
        self.wed_cancel = wed_cancel
        return wed_cancel

    def current_seat(self):
        wed_current = self.wed_avl - self.wed_booked + self.wed_cancel
        print("Wednesday current seats:",wed_current)

    def Avl_seat_daywise(self):

        super().avl_seat(60)
        super().seat_booked(30)
        super().seat_cancel(12)
        super().current_seat()

        super().avl_seat(60)
        super().seat_booked(23)
        super().seat_cancel(18)
        super().current_seat()

        self.avl_seat(60)
        self.seat_booked(45)
        self.seat_cancel(0)
        self.current_seat()

obj = Wednesday()
obj.Avl_seat_daywise()