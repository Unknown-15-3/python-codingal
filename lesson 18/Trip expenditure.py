def hotelcost(days):
    return 140 * days

def planeridecost(city):
    if "charlotte" == city:
        return 23145
    elif "tampa" == city:
        return 200000
    elif "pittsburgh" == city:
        return 300500
    elif "los angeles" == city:
        return 500130
    
def rentalcarcost(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    
def tripcost(city,days, spendingmoney):
    return rentalcarcost(days) + hotelcost(days) + planeridecost(city) + spendingmoney
     
print("cost of car rental:", rentalcarcost(7))
print("cost of hotel cost:", hotelcost(4000))
print("cost of plane ride cost:",planeridecost("los angeles"))
print("cost of the trip:", tripcost("los angeles", 57, 500000))
