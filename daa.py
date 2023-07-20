def min_min_refuelling_stops(D):
	D.sort()
	current_position =0
	num-stops = 0	For i ni range(len(D)):
		if D(i) – current_position >200:
			Return float(‘inf ‘)
		current_position = D[i]
		
		if currrentn_position >=D[-1]:
			return num_stops		num_stops += 1	return float(‘ inf ‘)
