def can_reach_the_pump(distance, miles_per_gallon, gallons_left):
    # Calculate the total distance the car can travel
    distance_possible = miles_per_gallon * gallons_left
    
    # Return True if the car can reach the pump, otherwise False
    return distance_possible >= distance
