from database import CursorFromPool


class User:

    def __init__(self, customer, room, check_in, check_out):
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def __repr__(self):
        return "Customer :{}, Room: {}".format(self.customer, self.room)

    # adding details of a new guest

    def insert_to_db(self):
        with CursorFromPool() as cursor:
            cursor.execute('insert into reservation values(%s, %s, %s, %s)',
                           (self.customer, self.room, self.check_in, self.check_out))

    @classmethod
    def load_from_db(cls, customer):
        with CursorFromPool() as cursor:
            cursor.execute('select * from reservation where name = %s', (customer,))
            customer_data = cursor.fetchone()

        if customer_data:
            return cls(customer_data[0], customer_data[1], customer_data[2], customer_data[3])

# checking the availabilty of the rooms (i think i have an error here)


def availability(room):

    with CursorFromPool() as cursor:

        if room == "Presidential" or room == "Suite":
            cursor.execute('select count(*) from reservation where room = %s', (room,))
            for row in cursor:
                if row[0] >= 2:
                    print("NO more rooms available")
                else:
                    print("Welcome!")

        elif room == "Double":
            cursor.execute('select count(*) from reservation where room = %s', (room,))
            for row in cursor:
                if row[0] >= 5:
                    print("NO more rooms available")
                else:
                    print("Welcome!")

        elif room == "Standard":
            cursor.execute('select count(*) from reservation where room = %s', (room,))
            for row in cursor:
                if row[0] >= 5:
                    print("NO more rooms available")
                else:
                    print("Welcome!")

# to calculate the net payable amount


def check(customer):
    with CursorFromPool() as cursor:
        cursor.execute('select * from net where name = %s', (customer,))

# to remove the guest entry after checkout


def update(customer):
    with CursorFromPool() as cursor:
        cursor.execute('delete from reservation where name = %s cascade', (customer,))
