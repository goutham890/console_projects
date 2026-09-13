from copy import deepcopy

movies = {
    "Avatar": [50, 1500],
    "Batman": [50, 180],
    "Interstellar": [100, 250],
    "Inception": [100, 220],
    "Titanic": [50, 200]
}

Dup = deepcopy(movies)
booking = {}

while(True):

    print("1 - Admin")
    print("2 - User")
    print("3 - Exit")
    print("-----------------------")

    n = int(input("Choose An Option :"))

    if n == 1:

        # ADMIN PANEL

        username = "admin@1234"
        pas = "erwin@12"

        x = input("enter the username :")

        if username == x:

            y = input("Enter the password :")

            if pas == y:

                print("Login successfull")

                while(True):

                    print("-------ADMIN-------")
                    print("1 - Add Movie")
                    print("2 - Remove Movie")
                    print("3 - Update Ticket Price")
                    print("4 - View Movie")
                    print("5 - theater Statistic")
                    print("6 - Reset Thearet")
                    print("7 - Back")
                    print("---------------------")

                    choose = int(input("Choose An Option :"))

                    if choose == 1:

                        n1 = input("Enter The Movie :")
                        n2 = int(input("Enter The Ticket Price :"))

                        if n1 in movies:
                            print("Movie Already Exists")
                        else:
                            movies.__setitem__(n1,[50,n2])
                            Dup.__setitem__(n1,[50,n2])
                            print("Movie Added Successfully")


                    if choose == 2:

                        rem = input("Enter The Movie :")

                        if rem in movies:
                            rm = movies.pop(rem)
                            Dup.pop(rem)

                            if rem in booking:
                                booking.pop(rem)

                            print("Movie", rem, "Removed")
                        else:
                            print("Movie Not Found")


                    if choose == 3:

                        n3 = input("Enter The Movie Name :")

                        if n3 in movies:

                            n4 = int(input("Enter The New Ticket Price :"))

                            movies[n3].__setitem__(1,n4)
                            Dup[n3].__setitem__(1,n4)

                            print("Ticket Price Updated")

                        else:
                            print("Movie Not Exist")


                    if choose == 4:

                        if len(movies) == 0:
                            print("No Movies Available")

                        else:

                            print("\n╔════════════════════════════════════════════════╗")
                            print("║              🎬 MOVIE LIST                    ║")
                            print("╠════════════════════════════════════════════════╣")

                            num = 1

                            for movie in movies:

                                print(f"║ {num}. {movie:<18} Seats: {movies[movie][0]:<4} Price: ₹{movies[movie][1]:<5} ║")

                                num += 1

                            print("╚════════════════════════════════════════════════╝")


                    if choose == 5:

                        if len(movies) == 0:
                            print("No Movies Available")

                        else:

                            total = 0
                            high = 0
                            low = 100

                            for i in movies:

                                total = total + movies[i][0]

                                if movies[i][0] >= high:
                                    high = movies[i][0]
                                    nan = i

                                if movies[i][0] <= low:
                                    low = movies[i][0]
                                    loww = i

                            avg = total / len(movies)

                            print("Total Seats :",total)
                            print("Most available :",nan," - ",high," Seats")
                            print("Least available :",loww," - ",low," Seats")
                            print("Average Seats :",avg)


                    if choose == 6:

                        movies.clear()
                        movies = deepcopy(Dup)

                        booking.clear()

                        print("Reset Succesfull")


                    if choose == 7:
                        break

            else:
                print("Wrong password")

        else:
            print("wrong username")


    if n == 2:

        # USER PANEL

        while(True):

            print("------USER------")
            print("1. View Movies")
            print("2. Book Tickets")
            print("3. Cancel Booking")
            print("4. My Bookings")
            print("5. Back")
            print("-----------------")

            s = int(input("Choose An Option :"))


            if s == 1:

                if len(movies) == 0:
                    print("No Movies")

                else:

                    s1 = 1

                    print("-----------------MOVIES-----------------")
                    print("No     Movies            Seats     Price")

                    for i in movies:

                        print(f"{s1:<5}{i:<18}{movies[i][0]:<10}₹{movies[i][1]:<10}")

                        s1 = s1 + 1

                    print("----------------------------------------")


            if s == 2:

                s2 = input("Enter The Name Of Movie :")

                if s2 in movies:

                    s3 = int(input("Enter The Number Of Tickets :"))

                    if s3 > 0:

                        if movies[s2][0] >= s3:

                            movies[s2][0] = movies[s2][0] - s3

                            s4 = s3 * movies[s2][1]

                            if s2 in booking:

                                booking[s2][0] = booking[s2][0] + s3
                                booking[s2][1] = booking[s2][1] + s4

                            else:

                                booking.__setitem__(s2,[s3,s4])

                            print("=======Booking Succesfull=======")
                            print("MOVIE :",s2)
                            print("No Of Ticket :",s3)
                            print("Price Per Ticket :",movies[s2][1])
                            print("Total Price :",s4)

                        else:
                            print("Not Enough Seats")

                    else:
                        print("Invalid Number Of Tickets")

                else:
                    print("Movie Not Fount")


            if s == 3:

                s5 = input("Enter The Name Of Movie :")

                if s5 in booking:

                    s6 = int(input("Enter The No. Of Ticket :"))

                    if s6 > 0:

                        if booking[s5][0] >= s6:

                            movies[s5][0] = movies[s5][0] + s6

                            booking[s5][0] = booking[s5][0] - s6
                            booking[s5][1] = booking[s5][1] - (s6 * movies[s5][1])

                            print("Tickets Cancelled Successfully")
                            print("Available Seats:",movies[s5][0])

                            if booking[s5][0] == 0:
                                booking.pop(s5)

                        else:
                            print("You Don't Have That Many Tickets")

                    else:
                        print("Invalid Number Of Tickets")

                else:
                    print("No Booking Found")


            if s == 4:

                print("================================")
                print("          MY BOOKINGS")
                print("================================")

                if len(booking) == 0:

                    print("No Bookings Found")

                else:

                    print("Movie          Tickets       Total Price")
                    print("----------------------------------------")

                    for movie in booking:

                        print(f"{movie:<15}{booking[movie][0]:<14}₹{booking[movie][1]}")

                    print("================================")


            if s == 5:
                break

    if n == 3:
        break