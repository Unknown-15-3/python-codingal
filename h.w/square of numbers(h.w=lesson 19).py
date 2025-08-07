start=int(int(input("enter the startting number: ")))
end = int(int(input("enter the ending number: ")))

squares = []
evensquare = []
oddsquare = []


for i in range( start, end + 1):
    square = i ** 2
    squares.append(square)

    if i % 2 == 0:
        evensquare.append(square)
    else:
        oddsquare.append(square)

print("squares:", squares, "even squares:", evensquare, "odd squares:", oddsquare)
      