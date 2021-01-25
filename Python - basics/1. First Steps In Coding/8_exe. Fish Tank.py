length = float(input())
width = float(input())
height = float(input())
perc_full = float(input())
aquarium_volume = length*width*height
total_liters = aquarium_volume*0.001
perc = perc_full*0.01
needed_liters = total_liters*(1-perc)
print(needed_liters)