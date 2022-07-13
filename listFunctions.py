lucky_numbers=[42,4,5,9,8,10,12]
friends=["El","Will","Dustin","Dustin","Mike","Lucas","Max"]

friends.insert(3,"Steve")
friends.append("joyes")
friends.remove("Lucas")
friends.pop()

print(friends.index("El"))
print(friends.index("Steve"))
print(friends.count("Dustin"))
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)
friends.extend(lucky_numbers)
print(friends)
friends.clear()