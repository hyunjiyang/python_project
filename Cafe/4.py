
def main():
    listOfmenu = obtainListOfmenu()
    displayResults(listOfmenu)
    order(listOfmenu)

def obtainListOfmenu():
    listOfmenu = []
    carryOn = 'Y'               
    while carryOn == 'Y':
        try:
            name = input("Enter menu's name: ")
            quantity = int(input("Enter the initial quantity of menu: "))
            category = input("Enter category (DRINK or FOOD): ")
        except:
            print("ERROR")
            continue
        else:
            if category.upper() == "FOOD":
                option = input("Enter warming option (WARM or COLD): ")
                if option.upper() == 'WARM':
                    option = True
                else:
                    option = False
                st = Food(name,quantity,option)
            elif category.upper() == "DRINK":
                st = Cafe(name,quantity)
            else :
                print("ERROR\n")
                continue

        listOfmenu.append(st)
        carryOn = input("Do you want to continue (Y/N)? ")
        carryOn = carryOn.upper()
    return listOfmenu

def displayResults(listOfmenu):
    print("*-"*15) 
    print("Welcome to the Galaxy cafe".center(30))
    print("*-"*15)
    print("< Menu >")

    listOfmenu.sort(key=lambda x: x.getName())
    for menu in listOfmenu:
        print(listOfmenu.index(menu)+1,")",menu)

class Cafe:
    def __init__(self, name="", quantity=0):
        self._name = name
        self._quantity = quantity

    def getName(self):
        return self._name

    def __str__(self):
        return self._name +"(quantity="+ str(self._quantity)+ ")"

class Food(Cafe):
    def __init__(self, name="", quantity=0, option=True):
        super().__init__(name,quantity)
        self._warming = option
    

    def __str__(self):    
        if self._warming:
            status = "warm desert"
        else:
            status = "cold desert"
        return self._name + "(quantity="+ str(self._quantity)+ ")"

def order(listofmenu):
    while len(listofmenu) != 0:
        try:
            numMenu = int(input("Make a selection from the menu: "))
            print("You choosed",listofmenu[numMenu-1],"\n")
        except :
            print("Wrong number! Choose number\n")
        else:
            numQuan = int(input("Give quantity of coffee: "))
            print("Here you are")
            del listofmenu[numMenu-1]
        finally:    
            displayResults(listofmenu)
    print("\n***Cafe closed***")


main()