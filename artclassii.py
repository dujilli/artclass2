x = 0
y = 0

hole_x = []
hole_y = []

def hole_counter():
        while True:
            try:
                    holes_x = int(input("Enter x coords:"))
                    holes_y = int(input("\nEnter y coords:"))

                    # holes_x, holes_y = hole_search()
                    x = holes_x
                    y = holes_y

                    hole_x.append(x)
                    hole_y.append(y)

                    hole_x.sort()
                    hole_y.sort()

                    x_count = len(hole_x)
                    y_count = len(hole_y)

                    low_x = hole_x[0]
                    low_y = hole_y[0]

                    high_x = hole_x[x_count-1]
                    high_y = hole_y[y_count-1]

                    dist_x = high_x - low_x
                    dist_y = high_y - low_y

                    print(hole_x,hole_y)


                    print(f"\nDistance x: {dist_x}cm, Distance y: {dist_y}cm")
                    print(f"Area: {dist_x * dist_y}cm^2\n")

            except ValueError:
                print("Please enter in a integer!")

hole_counter()
