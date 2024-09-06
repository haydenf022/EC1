print("Available movies today:")
print("A)12 Strong:	        1)2:30	2)4:40	3)7:50	4)10:50")
print("B)Coco:			1)12:40	2)3:45")
print("C)The Post:		1)12:45	2)3:35	3)7:05	4)9:55")
choice = str(input("Movie choice:   "))
if choice == "A" or choice == "B" or choice == "C":
    showtime = int(input("Showtime:    "))
    if (showtime >= 1 and showtime <= 4 and choice == "A" or choice == "C") or (
        choice == "B" and showtime == 1 or showtime == 2
    ):
        adult_tickets = int(input("Adult tickets:   "))
        kid_tickets = int(input("Kid tickets:   "))
        if kid_tickets + adult_tickets <= 30:
            if (choice == "B" or choice == "C") and showtime == 1:
                print(
                    f"Total cost: ${round((kid_tickets * 8) + (adult_tickets * 11.17), 2):.2f}"
                )
            else:
                print(
                    f"Total cost: ${round((kid_tickets * 9.68) + (adult_tickets * 12.45), 2):.2f}"
                )
        else:
            print("Invalid option; please restart app...")
    else:
        print("Invalid option; please restart app...")
else:
    print("Invalid option; please restart app...")
