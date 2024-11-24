from random import choice
menu=["Alfham","mandhi","noodles"]
while True:
    choice_1=print("1.show food list")
    choice_2=print("2.Add food ")
    choice_3=print("3.Remove food")
    choice_4=print("4.Exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print(menu)
    elif choice==2:
        add_food=input("enter a food item to add:")
        menu.append(add_food)
        print(menu)
    elif choice==3:
        remove_food=input("enter a food item to remove from the list:")
        menu.remove(remove_food)
        print(menu)
    else:
        print("Thankyou...!!!")
