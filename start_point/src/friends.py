import re


def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

# def likes_to_eat(person, food):
#     snacks = person["favourites"]["snacks"]
#     for snack in snacks:
#         if snack == food:
#          return True
        
        
def likes_to_eat(person, food):
    foundFood = False
    snacks = person["favourites"]["snacks"]
    
    for snack in snacks:
        if snack == food:
            foundFood = True
    return foundFood 
        
def add_friend(person, new_friend):
    person["friends"].append(new_friend)

def add_friend(person, old_friend):
    person["friends"].append(old_friend)    

           
        
