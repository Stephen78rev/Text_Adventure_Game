# adverture text game
#from Combat import combat

i_dir = 0

class person:
    def __init__(self,pocket,left_hand,right_hand,life,strength,body,shoulder,stamina,armour,speed):
        self.pocket = pocket 
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.life = life
        self.strength = strength
        self.body = body
        self.shoulder = shoulder
        self.stamina = stamina
        self.armour = armour
        self.speed = speed

class monster:
    def __init__(self,life,strength,armour,type,x_position,y_position,ignore):
        self.life = life
        self.strength = strength
        self.armour = armour
        self.type = type
        self.x_position = x_position
        self.y_position = y_position
        self.ignore = ignore

class map:
    def __init__(self,x_position,y_position):
        self.x_position = x_position
        self.y_position = y_position


############################################################
#                      movement
############################################################

class my_position:
    def my_position(self,new_position,stored_position):
        self.new_position = new_position
        self.stored_position = stored_position

def pos_1():
    my_position.new_position = input("what direction would you like to travel? N,S,E,W   ")
    pos_1_1()

def pos_1_1():    
    print("")
    if my_position.new_position == "exit":
        game_over()
    if my_position.new_position == "n" and map.y_position != 3:
        map.y_position = map.y_position + 1
        main_game()
    elif my_position.new_position == "n":
        print("you cant go that way") 
        main_game() 
    if my_position.new_position == "s" and map.y_position != 1:
        map.y_position = map.y_position - 1
        main_game()
    elif my_position.new_position == "s":
        print("you cant go that way")
        main_game() 
    if my_position.new_position == "e" and map.x_position != 3:
        map.x_position = map.x_position + 1
        main_game()
    elif my_position.new_position == "e":
        print("you cant go that way") 
        main_game() 
    if my_position.new_position == "w" and map.x_position != 1:
        map.x_position = map.x_position - 1
        main_game()
    elif my_position.new_position == "w":
        print("you cant go that way") 
        main_game() 
    else:
        print("invalid input")
        main_game()

def pos_2():                                       ############################  if facing a monster
    my_position.stored_position = my_position.new_position
    my_position.new_position = input("what direction would you like to travel? N,S,E,W  ")
    while my_position.new_position == my_position.stored_position:
        print("")
        print("a monster blockes your path")
        my_position.new_position = input("what direction would you like to travel? N,S,E,W  ")
    else:
        pos_1_1()

def invallid_direction(i_dir):
    i_dir = i_dir
    if i_dir == 1: i_dir = 0, pos_1()
    if i_dir == 2: i_dir = 0, fight_or_flight()

#################################################
#                   Items
#################################################

class item:
    def __init__(self,type,x_position,y_position,ignore,strength,armour):
        self.type = type
        self.x_position = x_position
        self.y_position = y_position
        self.ignore = ignore
        self.strength = strength
        self.armour = armour

class bucket(item):
    pass
class sword(item):
    pass
class shield(item):
    pass
class item_4(item):
    pass
class item_5(item):
    pass   

#items = [bucket,sword,shield,item_4,item_5]
#items_x = [bucket.x_position,sword.x_position,shield.x_position,item_4.x_position,item_5.x_position]
#items_y = [bucket.y_position,sword.y_position,shield.y_position,item_4.y_position,item_5.y_position]

def is_item():                                  ############################     is there an item in the current location
    if map.x_position == bucket.x_position and map.y_position == bucket.y_position:
        item.type = "bucket"
        item.ignore = 1
        print(f"I have seen a {item.type}")
        item_action()
    elif map.x_position == sword.x_position and map.y_position == sword.y_position:
        item.type = "sword"
        item.ignore = 1
        print(f"I have seen a {item.type}")
        item_action()
    elif map.x_position == shield.x_position and map.y_position == shield.y_position:
        item.type = "shield"
        item.ignore = 1
        print(f"I have seen a {item.type}")
        item_action()
    elif map.x_position == item_4.x_position and map.y_position == item_4.y_position:
        item.type = "item_4"
        item.ignore = 1
        print(f"I have seen a {item.type}")
        item_action()
    elif map.x_position == item_5.x_position and map.y_position == item_5.y_position:
        item.type = "item_5"
        item.ignore = 1
        print(f"I have seen a {item.type}")
        item_action()
    else:
        print("I see nothing")
        main_game()

def item_action():                                ###########################    to pick up or ..........?
    pick_up_item = input(f"infront of you is a {item.type} would you like to pick up this item? Y/N  ")
    print(person.right_hand,person.left_hand)
    if person.right_hand == "":
        right_hand_status = pick_up_item
        if right_hand_status == "y":
            print(f"you have picked up the {item.type}")
            person.right_hand = item.type
            if item.type == "bucket":
                bucket.x_position = ""
                bucket.y_position = ""
                item.ignore = 1
                main_game()
            elif item.type == "sword":
                sword.x_position = ""
                sword.y_position = ""
                item.ignore = 1
                main_game()
            elif item.type == "shield":
                shield.x_position = ""
                shield.y_position = ""
                item.ignore = 1
                main_game() 
            elif item.type == "item_4":
                item_4.x_position = ""
                item_4.y_position = ""
                item.ignore = 1
                main_game()
            elif item.type == "item_5":
                item_5.x_position = ""
                item_5.y_position = ""
                item.ignore = 1
                main_game() 
            else:
                print("something is wromg item_action")
                game_over()         #pickup_item_right()    

        elif right_hand_status == "n":
            main_game()
        else:
            print("invalid input")
            item.ignore = 0
            main_game()
    
    elif person.left_hand == "" and person.right_hand != "":
            left_hand_status= pick_up_item
            if left_hand_status == "y":
                print(f"you have picked up the {item.type} in your left hand")
                person.left_hand = item.type
                if item.type == "bucket":
                    bucket.x_position = ""
                    bucket.y_position = ""
                    item.ignore = 1
                    main_game()
                elif item.type == "sword":
                    sword.x_position = ""
                    sword.y_position = ""
                    item.ignore = 1 
                    main_game()
                elif item.type == "shield":
                    shield.x_position = ""
                    shield.y_position = "" 
                    item.ignore = 1
                    main_game()
                elif item.type == "item_4":
                    item_4.x_position = ""
                    item_4.y_position = ""
                    item.ignore = 1
                    main_game()
                elif item.type == "item_5":
                    item_5.x_position = ""
                    item_5.y_position = ""
                    item.ignore = 1
                    main_game() 
                else:
                    print("end of right hand status")
                    drop_item()

            elif left_hand_status == "n":   
                main_game()
            else:
                print("invalid input")
            item.ignore = 0
            main_game()
    else:
        print("final status else")
        if pick_up_item == "n":
            main_game()
        else:
            drop_item()


def drop_item():                                    ##################     drop item if hands are full   
    print(f"you cant pick up this item. You are carrying a {person.left_hand} in your left hand and a {person.right_hand} in your right")
    print("")
    left_hand_status = input(f"would you like to drop the {person.left_hand}?  Y/N  ")
    if left_hand_status == "y":
        print(f"you have dropped the {person.left_hand}")
        if person.left_hand == "bucket":
            person.left_hand = ""
            bucket.x_position = map.x_position
            bucket.y_position = map.y_position
            item_action()
        if person.left_hand == "sword":
            person.left_hand = ""
            sword.x_position = map.x_position
            sword.y_position = map.y_position
            item_action()
        if person.left_hand == "shield":
            person.left_hand = ""
            shield.x_position = map.x_position
            shield.y_position = map.y_position
            item_action()
        if person.left_hand == "item_4":
            person.left_hand = ""
            item_4.x_position = map.x_position
            item_4.y_position = map.y_position
            item_action()
        if person.left_hand == "item_5":
            person.left_hand = ""
            item_5.x_position = map.x_position
            item_5.y_position = map.y_position
            item_action()

    elif left_hand_status == "n":
        right_hand_status = input(f"would you like to drop the {person.right_hand}?  Y/N  ")
        if right_hand_status == "y":
            print(f"you have dropped the {person.right_hand}")
            if person.right_hand == "bucket":
                person.right_hand = ""
                bucket.x_position = map.x_position
                bucket.y_position = map.y_position
                item_action()
            if person.right_hand == "sword":
                person.right_hand = ""
                sword.x_position = map.x_position
                sword.y_position = map.y_position
                item_action()
            if person.right_hand == "shield":
                person.right_hand = ""
                shield.x_position = map.x_position
                shield.y_position = map.y_position
                item_action()
            if person.right_hand == "item_4":
                person.right_hand = ""
                item_4.x_position = map.x_position
                item_4.y_position = map.y_position
                item_action()
            if person.right_hand == "item_5":
                person.right_hand = ""
                item_5.x_position = map.x_position
                item_5.y_position = map.y_position
                item_action()
        elif right_hand_status == "n":
            main_game()
    else:
        print("invalid input_3")
        item_action()
    




################################################
#                   Weapons
################################################


################################################
#                    Armour
################################################


#################################################
#                   Combat!
#################################################

class boar(monster):
    pass
class troll(monster):
    pass
class mon_3(monster):
    pass
class mon_4(monster):
    pass
class mon_5(monster):
    pass


def is_monster():                       ############################     is there an monster in the current location
    if map.x_position == boar.x_position and map.y_position == boar.y_position:
        monster.type = boar.type
        monster.x_position = boar.x_position
        monster.y_position = boar.y_position
        monster.life = boar.life
        monster.strength = boar.strength
        monster.armour = boar.armour
        monster.ignore = 1
        print(f"I have seen a {monster.type}")
        fight_or_flight()
    elif map.x_position == troll.x_position and map.y_position == troll.y_position:
        monster.type = troll.type
        monster.x_position = troll.x_position
        monster.y_position = troll.y_position
        monster.life = troll.life
        monster.strength = troll.strength
        monster.armour = troll.armour
        monster.ignore = 1
        print(f"I have seen a {monster.type}")
        fight_or_flight()
    elif map.x_position == mon_3.x_position and map.y_position == mon_3.y_position:
        monster.type = mon_3.type
        monster.x_position = mon_3.x_position
        monster.y_position = mon_3.y_position
        monster.life = mon_3.life
        monster.strength = mon_3.strength
        monster.armour = mon_3.armour
        monster.ignore = 1
        print(f"I have seen a {monster.type}")
        fight_or_flight()
    elif map.x_position == mon_4.x_position and map.y_position == mon_4.y_position:
        monster.type = mon_4.type
        monster.x_position = mon_4.x_position
        monster.y_position = mon_4.y_position
        monster.life = mon_4.life
        monster.strength = mon_4.strength
        monster.armour = mon_4.armour
        monster.ignore = 1
        print(f"I have seen a {monster.type}")
        fight_or_flight()
    elif map.x_position == mon_5.x_position and map.y_position == mon_5.y_position:
        monster.type = mon_5.type
        monster.x_position = mon_5.x_position
        monster.y_position = mon_5.y_position
        monster.life = mon_5.life
        monster.strength = mon_5.strength
        monster.armour = mon_5.armour
        monster.ignore = 1
        print(f"I have seen a {monster.type}")
        fight_or_flight()
    else:
        print("I see nothing")
        main_game()
    


def fight():                                  #######################  FIGHT! FIGHT! FIGHT!
    while monster.life > 1:
        print("fight")
        person.life = person.life - monster.strength
        monster.life = monster.life - person.strength
        if monster.life < 1:
            mon_defeat()
        else:
            print(f"monster life = {monster.life} and persons life = {person.life}")
            if person.life < 1:
                print(" you are dead")
                game_over()  
            carry_on = input("do you want to carry on the fight ? Y/N  ")
            if carry_on == "n":
                pos_2()
    else:
        mon_defeat()

def mon_defeat():
        print(f"you have defeated the {monster.type}!")
        if monster.type == "boar":
            boar.x_position = 0
            boar.y_position = 0
        elif monster.type == "troll":
            troll.x_position = 0
            troll.y_position = 0
        elif monster.type == "mon_3":
            mon_3.x_position = 0
            mon_3.y_position = 0
        elif monster.type == "mon_4":
            mon_4.x_position = 0
            mon_4.y_position = 0
        elif monster.type == "mon_5":
            mon_5.x_position = 0
            mon_5.y_position = 0 
        pos_2()



    

def fight_or_flight():                              ##################    fight or walk slowley and quietly backwards
    fight_flight = input("would you like to take on the beast?  y/n  ")
    print("")
    if fight_flight == "n":
        monster.ignore = 0
        pos_2()
    elif fight_flight =="y":
        fight()
    else:
        print("invalid input 2")
        invallid_direction(2)

############################################################
#                         Terain (maybe)
############################################################



############################################################
#                  starting deffinitions
############################################################

bucket.type = "Bucket"
bucket.x_position = 2
bucket.y_position = 3
sword.type = "sword"
sword.x_position = 6
sword.y_position = 6
shield.type = "shield"
shield.x_position = 6
shield.y_position = 6
item_4.type = "item_4"
item_4.x_position = 6
item_4.y_position = 6
item_5.type = "item_5"
item_5.x_position = 6
item_5.y_position = 6
map.x_position = 2
map.y_position = 2
item.x_position = 0
item.y_position = 0
item.type = 0
item.ignore = 0
person.pocket = ""
person.right_hand = sword.type
person.left_hand = shield.type
person.strength = 2
person.life = 10
person.armour = 0
person.body = 0
person.shoulder = ""   #for slinging a shield
monster.life = 0
monster.strength = 0
monster.armour = 0
monster.ignore = 0
monster.x_position = 0
monster.y_position = 0
my_position.new_position = ""
my_position.stored_position =""
boar.type = "boar"
boar.x_position = 2
boar.y_position = 3
boar.life = 6
boar.strength = 1
boar.armour = 0


############################################################
#                     Main Game / Map
############################################################

def game_over():
    print("Game Over!")
    quit()


def main_game():
    
    if map.x_position == 1 and map.y_position == 1:
        print("1,1")  
        pos_1()

    if map.x_position == 2 and map.y_position == 1: 
            print("2,1")                                                        
            pos_1()

    if map.x_position == 2 and map.y_position == 1:
        print("2,1")
        pos_1()
 
    if map.x_position == 3 and map.y_position == 1:
        print("3,1")
        pos_1()

    if map.x_position == 1 and map.y_position == 2:
        print("1,2")
        print("you are in a forest in front of you is a wild boar")
        monster.life = 6
        monster.strength = 2
        fight_flight = ""
        fight_or_flight()
        #pos_1()
        
    if map.x_position == 2 and map.y_position == 2:
        print("middle")
        pos_1()

    if map.x_position == 3 and map.y_position == 2:
        print("3,2")
        pos_1()

    if map.x_position == 1 and map.y_position == 3:
        print("1,3")  
        pos_1()
        
    if map.x_position == 2 and map.y_position == 3:           ###################################################### new item code
        print("2,3")
        if item.ignore == 0:
            is_item()                                       
        else: 
            item.ignore = 0
            if monster.ignore == 0:
                is_monster()
            else:
                monster.ignore = 0
                pos_1()

    if map.x_position == 3 and map.y_position == 3:
        print("3,3")
        print("you are in a forest in front of you is a troll")
        monster.life = 10
        monster.strength = 6
        fight_flight = ""
        fight_or_flight()
        pos_1()

    else:
        print("Bye Now!") 
        print(map.x_position,map.y_position)

if my_position.new_position != "exit":
    main_game()
else:
    print(my_position.new_position)    
    print(map.y_position,map.x_position)
    game_over()