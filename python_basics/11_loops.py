# while and for loops

# while loops



# x = 0
# while (x<5):
#     print(x)
#     x = x+1


# for loops
# for x in range(5,11):
#     print(x)

# example(array)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for d in days:
    # if (d == "Saturday"): break  #loop stops
    if (d == "Saturday"): continue  #skips d
    print(d)
