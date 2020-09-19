"""
Budget_calculator:
class: category, functions (init,deposit,get_balance,withdraw,transfer,checkfunds,str)
init():
generates a name, and a blank ledger list upon creation of a class iteration

deposit(self, amount, description):
adds an dictionary entry to the ledger list, with values of amount, and (optionally) discription

withdraw (self, amount, description):
same thing as deposit, but converts amount to a negative number. only does the entry if there are more + values than the added negative
returns True if successful or false if failed

get_balance(self):
sums the total account entries

transfer(self, amount, category)
makes a withdrawl from this account, and makes a deposit in the category given. only occurs if more + than the requested amount. returns t/f if successful/not

extranious function:
create_spend_chart(list):
takes a list of categories and creates a spend chart according to rules layed out in the fcc challenge
"""

class Category:
    def __init__(self,name):
        #this section allows us to assign variables on class creation
        self.name = name
        self.ledger = []

    def deposit(self,amount, desc = ""):
        # appends an object to the ledger list in the form of {"amount":amount, "desc": desc}
        self.ledger.append({"amount":float(amount),"description":desc})
        print(self.ledger)

    def get_balance(self):
        #returns the current balance of the account (debits - credits)
        balance = 0
        for entry in self.ledger:
            balance += entry["amount"]
        return balance

    def withdraw(self, amount, desc = ""):
        #same function as deposit, but the amount is negative
        if amount >self.get_balance():
            return False
        else:
            self.ledger.append({"amount":float(f"-{amount}"),"description":desc})
            return True
        
    def transfer(self, amount, category):
        #places a withdrawl on this account, and a deposit on the category in the method bracket
        if amount > self.get_balance():
            return False
        else:
            self.ledger.append({"amount":float(f"-{amount}"),"description":f"Transfer to {category.name}"})
            category.ledger.append({"amount":float(f"{amount}"),"description":f"Transfer from {self.name}"})
            return True
        
    def check_funds(self,amount):
        #returns true or false depending on if the amount is greater or less than the balance of the budget
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        #allows us to choose what is printed when we print the instance of the class
        printable = (format(self.name,"^30").replace(" ","*") + "\n")
        for item in self.ledger:
            printable += (format(item['description'][:23],"<23") + "{:>7.2f}".format(item['amount']) + "\n") #when working with format, either do all your stuff in the {} or in the second argument. Dont mix!
        printable += ("Total: {:.2f}".format(self.get_balance())) 
        return printable


def create_spend_chart(categories):
    #create a very specific bar chart showing percentage of spending that each category in the list is taking up


    balance = []
    names = []
    count = 0
    for cat in categories:
        #generates two lists: one of the name and one of the total withdrawl volume for each of the listed categories
        names.append(cat.name)
        balance.append(0)
        for entry in cat.ledger:
            #generates total withdrawl number by cycling through a categories ledger and adding all the negative numbers to the respective balance number
            if entry["amount"] < 0:
                balance[count] += entry["amount"]
        count += 1
    count = 0

    total = sum(balance) #total spending
    longest = len(max(names,key=len)) #length of the longest name, will be important for chart generation later
    

    for item in balance: 
        #calculates the percentage of total spending that each category is responsible for, rounded to the lowest near 10 
        balance[count] = int(item/total*10)
        count += 1


    chart = "Percentage spent by category" #first line of the chart
    for i in range(100,-1,-10):
        #works through each possible percentage value, adding o's when a categories percentage spending is equal or less than that value
        chart += "\n{:>3}|".format(i)
        for item in balance:
            #checks each category to see if that number is greater or equal to the current percentage value. adds o if yes, spaces if no
            if (item*10) >= (i):
                chart += format("o","^3")
            else:
                chart += format("","^3")
        chart += " "
    
    dashes = "-"*(3*len(balance)+1) #adds a line of dashes to separate chart from colnames
    chart +=f"\n    {dashes}" 

    for i in range(longest):
        #generates a colname for each category using a very similar technique to the one used for o plotting
        chart += "\n    "
        for item in names:
            #checks if the length of the catname is longer or equal to the current collength, prints the current letter if yes or a space if no
            if len(item) >= i + 1:
                chart += format(item[i],"^3")
            else:
                chart += format("","^3")
        chart += " "


    return chart



if __name__ == "__main__":
    food = Category("Food")
    entertainment = Category("Entertainment")
    business = Category("Business")
    food.deposit(900, "deposit")
    entertainment.deposit(900, "deposit")
    business.deposit(900, "deposit")
    food.withdraw(105.55)
    entertainment.withdraw(33.40)
    business.withdraw(10.99)
    handle = open("test.txt", "w")
    handle.write(create_spend_chart([business, food, entertainment]))
    handle.close()

