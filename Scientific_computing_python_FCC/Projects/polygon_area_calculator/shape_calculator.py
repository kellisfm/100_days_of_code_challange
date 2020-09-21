class Rectangle:
    def __init__(self, width = 0, height = 0):
        #on startup sets the width and height of the rectangle to user defined values, or 0 if not entered
        self.width = width
        self.height = height

    def set_width(self, number):
        #changes width to user value
        self.width = number

    def set_height(self, number):
        #changes height to user value
        self.height = number
    
    def get_area(self):
        #returns area
        return (self.height * self.width)
    
    def get_perimeter(self):
        #returns perimeter
        return (2*self.width + 2* self.height)
    
    def get_diagonal(self):
        #returns length of the long diagonal
        return ((self.width**2 + self.height ** 2) **0.5)
    
    def get_picture(self):
        #prints a picture made of * to a max of 50x50
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ""
            i = 1
            while i <= self.height:
                picture += (("*"*self.width) + "\n")
                i += 1
            return picture

    def get_amount_inside(self,shape):
        #calculates and returns how many of a different shape instance can fit in this one
        shape_area = shape.width*shape.height
        return self.get_area() // shape_area

    def __str__(self):
        #defines what should print when this class is called as a str
        return f"Rectangle(width={int(self.width)}, height={int(self.height)})"

    
class Square(Rectangle):
    def __init__(self,side =0):
        #sets side to a user value, and duplicates for w/h
        self.width = side
        self.height = self.width
    
    def set_side(self, num):
        self.width = num
        self.height = self.width

    def __str__(self):
        return (f"Square(side={self.width})")

    def set_width(self,num):
        self.width = num
        self.height = self.width

    def set_height(self,num):
        self.width = num
        self.height = self.width

if __name__ == "__main__":
    s = Rectangle(3,6)
    print(str(s))
