
class Ice_cream:
    def __init__(self):
        self.toppings = []
        self.deluxe = False
        self.num_scoops = 1
        self.price = 0
        self.flavor = ''
    def get_flavor(self):
        return self.flavor
    def get_num_scoops(self):
        return self.num_scoops
    def get_choice(self):
        return self.choice
    def get_toppings(self):
        return self.toppings
    def set_flavor(self, flavor):
        if flavor.lower() not in ['vanilla','chocolate','strawberry']:
            raise ValueError("Please put in a valid ice cream flavor.")
        self.flavor = flavor.lower()
        if self.flavor == 'vanilla':
            self.price = 1.05
        elif self.flavor == 'chocolate':
            self.price = 1.12
        elif self.flavor == 'strawberry':
            self.price = 1.32
    def set_num_scoops(self, num_scoops):
        if num_scoops <= 0:
            raise ValueError("Please enter a number greater than 0")
        self.num_scoops = num_scoops
        self.price *= num_scoops
    def set_choice(self, deluxe):
        self.deluxe = deluxe
    def set_toppings(self,toppings):
        self.toppings = toppings
    def calc_total(self):
        total = self.price
        if self.deluxe:
            total *= 1.42
        for topping in self.toppings:
            total += topping.get_cost()
        return total
    def ice_cream_info(self):
        info = f"\nFlavor: {self.flavor}"
        info += f"\nScoops: {self.num_scoops}"
        info += f"\nDeluxe: {self.deluxe}"
        info += f"\nToppings: "
        for t in self.toppings:
            info += t.get_type() + " "
        if not self.toppings:
            info += "NONE"
        info += f"\nTotal: ${self.calc_total():.2f}\n"
        return info


class Topping:
    def __init__(self,type):
        self.type = type.lower()
        if self.type.lower() == 'sprinkles':
            self.cost = 0.15
        elif self.type.lower() == 'gummy bears':
            self.cost = 0.45
        elif self.type.lower() == 'oreos':
            self.cost = 0.38
    def get_type(self):
        return self.type
    def get_cost(self):
        return self.cost
    


    

        

class Receipt:
    def __init__(self):
        self.ice_creams = []
        self.name = ""
    def add(self,ice_cream):
        self.ice_creams.append(ice_cream)
    def calc_total(self):
        total = 0
        for i in self.ice_creams:
            total += i.calc_total()
        return total
    def set_name(self, name):
        self.name = name
    def print_receipt(self):
        str_total = ""
        str_total += "\nAdkins' Scoop City Receipt"
        str_total +=f"\nCustomer Name: {self.name}"
        for i in self.ice_creams:
            str_total += (i.ice_cream_info())
        str_total += (f"Final Total: ${self.calc_total():.2f}")
        return str_total
    def main():
        rec = Receipt()
        print("Welcome to Adkins' Scoop City!")
        print("What is your name?")
        user_name = input().strip()
        rec.set_name(user_name)
        like_to_order = 'y'
        while like_to_order == 'y':
            ice_cream = Ice_cream()
            print("What flavor of ice cream would you like to order?")
            print("Your options are: Vanilla, Strawberry, Chocolate.")
            while True:
                try:
                    user_flavor = input().strip().lower()
                    ice_cream.set_flavor(user_flavor)
                    break
                except ValueError:
                    print("Please put in a valid ice cream flavor.")
            print("Would you like the deluxe brand? (Yes/No)")
            deluxe_choice = input().strip().lower()
            while deluxe_choice != 'yes' and deluxe_choice != 'no':
                print("Please input Yes or No!")
                deluxe_choice = input().strip().lower()
            ice_cream.set_choice(deluxe_choice == "yes")
            print("How many scoops would you like to order?")
            while True:
                try: 
                    user_scoops = int(input())
                    ice_cream.set_num_scoops(user_scoops)
                    break
                except ValueError:
                    print("Please enter a number greater than 0")
            print("Which toppings would you like? Enter done if you do not want any.")
            print("Your options are: sprinkles, gummy bears, oreos.")
            toppings_temps = []
            while True:
                topping_type = input().strip().lower()
                if topping_type == "done":
                    break
                elif topping_type in ["sprinkles","gummy bears","oreos"]:
                    topping = Topping(topping_type)
                    toppings_temps.append(topping)
                    print(f"Topping {topping.get_type()} added for ${topping.get_cost():.2f}")
                    print("Enter done if you are done selecting toppings, or enter another topping.")
                else:
                    print("Please put in a valid topping type.")
            ice_cream.set_toppings(toppings_temps)
            rec.add(ice_cream)
            print('Your order so far:')
            print(rec.print_receipt())
            print("Would you like to order another ice cream? (Yes/No)")
            new_order = input().strip().lower()
            while new_order != 'yes' and new_order != 'no':
                print("Please input Yes or No!")
                new_order = input().strip().lower()
            if new_order == 'yes':
                continue
            elif new_order == 'no':
                like_to_order = 'n'
            print(rec.print_receipt())
    
if __name__ == "__main__":
    Receipt.main()



            



    
        
        
            

        





    
    
    