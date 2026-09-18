# Compute the minimum number of gas tank refills to get from one city to another.
def car_fueling(distance: int, miles_per_tank: int, stops_count: int, stops: list):
    if(len(stops) != stops_count):
        return -1

    next_stop = 0
    current_tank = miles_per_tank
    current_distance = 0
    stops.append(distance)

    fills = 0

    while current_distance < distance:
        if current_tank < (stops[next_stop] - current_distance):
            fills += 1
            current_tank = miles_per_tank
            if current_tank < (stops[next_stop] - current_distance):
                return -1
            
        current_tank -= stops[next_stop] - current_distance
        current_distance = stops[next_stop]
        next_stop += 1
            

    return fills

def main():
    distance = int(input())
    miles_per_tank = int(input())

    stops_count = int(input())
    stops = input().split(' ')
    stops = [int(x) for x in stops]

    print(car_fueling(distance, miles_per_tank, stops_count, stops))


            
        


main()