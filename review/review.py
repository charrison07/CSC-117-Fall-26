print("youll type names to add to a list until you are finished")
print("type 'DONE' when you are finished")

string = input("Enter a name: ")
vip_list = []

while string != "DONE":
    vip_list.append(string)
    string = input("Enter a name: ")

print("The VIP list is:")
for name in vip_list:
    print(name)
