fantasy_roster = ["Brock Purdy", "Bijan Robinson", "Tetairoa Mcmillan"]
print(fantasy_roster[1])
print(len(fantasy_roster))
fantasy_roster.append("Malik Nabers")
print(fantasy_roster[3])
print(fantasy_roster[-1])
fantasy_roster.insert(0, "Trey Mcbride")

print("MY FANTASY ROSTER")
for thing in fantasy_roster:
    print(f"-- {thing}")
    