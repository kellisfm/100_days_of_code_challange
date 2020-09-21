import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        #on initialization, will take any number of keywords and append them into a list based on thier value
        self.contents = []
        
        for arg in kwargs.items():
            #cycles through each of the provided keywords
            i = 1
            while i <= arg[1]:
                #appends the keyword to the list i times, where i is the value of the keyword
                self.contents.append(arg[0])
                i+=1
        
        self.oghat = copy.copy(self.contents) #this copy will be useful for reseting the list
        

    def draw(self,numball):
        #extract a number of items from the list randomly, without replacement
        if numball >= len(self.contents):
            #returns the full contents of the bag if the user wants an amount greater than or equal to remaining
            return self.contents

        draw = random.sample(self.contents,numball) #does a draw without replacement

        for d in draw:
            #they want it to remove the items from our list for some reason? This does that
            self.contents.remove(d)
        
        return draw
        
    def reset(self):
        #resets the bag to it's origional state
        self.contents = copy.copy(self.oghat)


def cif(v2,v1):
    #does a check if one list is the subset of another, duplicates included. takes two ORDERED lists
    it = iter(v1)
    return all(c in it for c in v2)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    success = 0
    expected_list = []

    for arg in expected_balls.items():
        #converts from dic to list
            i = 1
            while i <= arg[1]:
                expected_list.append(arg[0])
                i+=1
                 
    expected_list = sorted(expected_list)

    while count < num_experiments:
        #does a draw num_experiments times, and checks if the expected items were included in the draw. increases success tally if yes, remains the same if no
        draw = hat.draw(num_balls_drawn)
        draw = sorted(draw)
        if cif(expected_list,draw):
            success += 1
        hat.reset()
        count += 1

    prob = success/count
    return prob

if __name__ == "__main__":
    hat = Hat(blue=3,red=2,green=6)
    print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=100))
    