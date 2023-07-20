def min_refueling_stops(D):
    D.sort()  
    current_position = 0
    num_stops = 0

    for i in range(len(D)):
        if D[i] - current_position > 200:
            
            return float('inf')
        
    
        current_position = D[i]

        if current_position >= D[-1]:
            
            return num_stops

        num_stops += 1

    return float('inf')  


fuel_stations = [0, 80, 140, 210, 300]  
result = min_refueling_stops(fuel_stations)
print(result) 
