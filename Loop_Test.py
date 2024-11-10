
class person():
    def __init__(self,left_hand,right_hand):
        self.left_hand = left_hand
        self.right_hand = right_hand

class item():
    def __init__(self,x_position,y_position):
        self.x_position = x_position
        self.y_position = y_position

class sword(item):
    pass
class shield(item):
    pass
class axe(item):
    pass
class item_4(item):
    pass
class item_5(item):
    pass

person.left_hand = "sword"
person.right_hand = "shield"

list = ["sword","shield"]

for x in range (len(list)):
   if person.right_hand == list[x]:
       print(f"I have a {person.right_hand}")



