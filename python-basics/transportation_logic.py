distance_mi = 10
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

# --- Travel Option Logic ---
if distance_mi <= 1:
    if not is_raining:
        print("Walk (It is close and not raining!)")
    else:
        print("Too rainy to walk, find another way.")

elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print("The person can ride a bike!")
    else:
        print("Distance is fine for a bike, but either it's raining or you don't have one.")

elif distance_mi > 6:
    if has_car:
        print("Drive the car!")
    elif has_ride_share_app:
        print("Take a ride-share (Uber/Lyft)!")
    else:
        print("Too far to walk or bike, and no car or app available.")

else:
    print("Invalid distance.")