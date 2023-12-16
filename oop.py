class parkingGarage:
    tickets = ["ticket", "ticket", "ticket", "ticket", "ticket", "ticket", "ticket", "ticket", "ticket"]
    parkingSpace = ["space", "space", "space", "space", "space", "space", "space", "space", "space"]
    ticketPrice = 10
    currentTicket = {"paid" : False}

    def __init__(self):
        self.hours = "none"
    
    def greeting(self):
        choice = input("Hi Welcome to express Parking press 1 take a ticket or press 2 to cancel \n")
        self.currentTicket["paid"] = False
        self.hours = 0
        while choice == "1" or choice == "2":
            if choice == "1":
                return True
            elif choice == "2":
                return False
            else:
                print("input invalid try again")
        
    def takeTicket(self):
        self.tickets.pop()
        self.parkingSpace.pop()

    def payForParking(self):
        
        while int(self.hours) != int:
            try:
                self.hours= int(input("Please type amount of hours you have parked then insert debit card \n"))
                break;
            except ValueError:
                print("input invalid try again")
        price = self.hours * self.ticketPrice
        print(f"Your total cost is ${price:.2f}")
        self.currentTicket["paid"] = True
        print("ticket paid")
    
    def leaveGarage(self):
        print("Your total cost will be the amount of hours you parked times ticket price of $10")
        self.payForParking()
        print("You have 15 min to leave - Thank you have a nice day!")
        self.tickets.append("ticket")
        self.parkingSpace.append("space")

while True:
    leaving = "0"
    newParking = parkingGarage()
    choice = newParking.greeting()
    if choice == True:
        newParking.takeTicket()
        while leaving != "1":
            leaving = input("please type 1 when you are ready to leave \n")
            if leaving == "1":
                newParking.leaveGarage()
            else: 
                print("input invalid try again")
    else:
        break;




    




        