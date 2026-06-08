
# 1
def my_function():
    for i in range (1,21):
        if i == 20:
            print("you got it")

my_function()



# 2
from random import randint
dice_imgs = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣"]
dice_nums = randint(0,5)
print(dice_imgs[dice_nums])



# 3
year = int(input("Enter a year of birth: "))
if year <= 1980:
    print("too old")
elif year > 1980 and year < 1994:
    print("you are a millennial ")
elif year >= 1994:
    print("you are a Gen Z")




# 4
age = int(input("how old are you: "))
if age > 18:
    print(f"you can drive at age {age}")
elif age <= 18:
    print("you are child yet, you can not drive. ")



# 5
pages = 0
word_per_page = 0
pages += int(input("number of pages: "))
word_per_page += int(input("number of words per page: "))
total_words = pages * word_per_page
print(total_words)




# 6
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
# b_list = [2, 4, 6, 10, 16, 26]

