import datetime as dt
print("welcome")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the program.")

timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestamp)


vip_file = open("09/files/vip.txt", "r")
vip_list = vip_file.readlines()
print(vip_list)

vip_status = False
for guest_name in vip_list:
    if guest_name.strip() == name:
        vip_status = True
        print("VIP")

file = open("09/files/all-guests.txt", "a")
file.write(f"{name}, VIP: {vip_status}, Arrival Time: {timestamp}\n")
file.close()
