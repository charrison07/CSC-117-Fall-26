#ask what the temp is today
#store response as temp

#if temp is 40 and below wear a jacket

temp = int(input("What is the temperature today? "))

if temp <= 0:
    print("Stay inside - Its freezing!")

elif temp <= 20:
    print("Bundle up - Its REALLY cold!")

elif temp <= 40:
    print("Wear a jacket")

elif temp <= 100:
    print("Wear some clothes for hotter weather today")

else:
    print("HOW ARE YOU NOT DEAD?!")



