#defining a function

#1
from cgitb import text
from hashlib import new


# def we_champions(): 
#     print("We are the Champions, My friends")
#     print("We are the Champions, My friends")
#     print("We are the Champions, My friends")

# we_champions()


#2
# def we_champions():
#     text = "We are the Champions, My friends"
#     print(text)
#     print(text)
#     print(text)

# we_champions()


#3
# def we_champions(text):
#     print(text)
#     print(text)
#     print(text)

# we_champions("We are the Champions, My friends")


# defining a function with if, elif & else statement
# def school_age_calc(age):
#     if age == 5:
#         print("Hammad can go to school")
#     elif age > 5:
#         print("Hammad should join higher studies")
#     else:
#         print("Hammad is still a baby")

# school_age_calc(6)        


#defining a function of future
def future_age(age):
    new_age = age + 20
    return new_age
    print(new_age)

predicted_age = future_age(12)
print(predicted_age)

