
class item:
    def __init__(self,x_position,y_position,use,name,power,armour):
        self.x_position = x_position
        self.y_position = y_position
        self.use = use
        self.name = name
        self.power = power
        self.armour = armour

class bucket(item):
    pass
class soward(item):
    pass
item.x_position = 1
item.y_position = 1
soward.x_position = 3
bucket.x_position = 5
soward.name = "Soward"
bucket.name = "bucket"
y = 2


def ah_ha():
    if y == 1:
        global x
        x = soward
    elif y == 2:
        x = bucket
        bucket.x_position = 5

ah_ha()
print(item.x_position)


print (x)
print(x.x_position)
print(x.name)




