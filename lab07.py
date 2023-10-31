class Toppings:
    def __init__(self, user_toppings = []):
        self.user_toppings = user_toppings
    def cost(self, user_toppings):
        cost = 0
        for topping in self.user_toppings:
            if self.topping == 'sprinkles':
                cost += 0.15
            elif self.topping == 'gummy bears':
                cost += 0.45
            elif self.topping == 'oreos':
                cost +=0.38
            else:
                cost += 0
        return cost
    

class Ice_cream:
    def __init__(self, flavor, choice, num_scoops,toppings = Toppings()):
        self.flavor = flavor
        self.choice = choice
        self.num_scoops = num_scoops
        self.toppings = toppings
    def cost(self):
        cost = 0
        if self.choice == 'yes':
            if self.flavor == 'Vanilla':
                cost += 1.491 * self.num_scoops
            elif self.flavor == 'Chocolate':
                cost += 1.5904 * self.num_scoops
            else:
                cost += 1.8744 * self.num_scoops
        else:
            if self.flavor == 'Vanilla':
                cost += 1.05 * self.num_scoops
            elif self.flavor == 'Chocolate':
                cost += 1.12 * self.num_scoops
            else:
                cost += 1.32 * self.num_scoops
        return cost
    def ice_cream_info(self):
        print(f"Flavor: {self.flavor}")
        print(f"Scoops: {self.num_scoops}")
        if self.choice == 'yes':
            print(f"Deluxe: True")
        else:
            print(f"Deluxe: False")
        if self.toppings.cost() == 0: 
            print(f"Toppings: NONE")
        else:
            print(f"Toppings: ", end = '')
            for i in range(len(self.toppings.user_toppings())):
                print(f"{user_toppings[i]} ", end = '')

    

        

class Receipt:
    def __init__(self, user_ice_cream = Ice_cream()):
        self.name = name
        self.user_ice_cream = user_ice_cream
    def print_receipt(self,):
        print("Adkin's Scoop City Receipt")
        print(f"Customer Name: {self.name}")
        print(self.user_ice_cream.ice_cream_info())
        print(f"Total: ")
        
        
            

        




print("Welcome to Adkins' Scoop City!")
print("What is your name?")
user_name = input()
like_to_order = 'y'
while like_to_order == 'y':
    print("What flavor of ice cream would you like to order?")
    print("Your options are: Vanilla, Strawberry, Chocolate.")
    user_flavor = input().lower()
    while user_flavor != 'vanilla' and user_flavor != 'strawberry' and user_flavor != 'chocolate':
        print("Please put in a valid ice cream flavor.")
        user_flavor = input().lower()
    print("Would you like the deluxe brand? (Yes/No)")
    deluxe_choice = input().lower()
    while deluxe_choice != 'yes' and deluxe_choice != 'no':
        print("Please input Yes or No!")
        deluxe_choice = input().lower()
    print("How many scoops would you like to order?")
    user_scoops = int(input())
    while user_scoops <= 0:
        print("Please enter a number greater than 0")
        user_scoops = int(input())
    users_ice_cream = Ice_cream(user_name, user_flavor, deluxe_choice, user_scoops, )
    print("Which toppings would you like? Enter done if you do not want any.")
    print("Your options are: sprinkles, gummy bears, oreos.")
    user_toppings_list = []
    user_choice_toppings = input().lower()
    while user_choice_toppings != 'sprinkles' and user_choice_toppings != 'gummy bears' and user_choice_toppings != 'oreos' and user_choice_toppings != 'done':
        print("Please put in a valid topping type.")
        user_choice_toppings = input().lower().split()
    user_toppings_list.append(user_choice_toppings)
    print(f"Topping {user_choice_toppings} added for {}")
    done = 'n'
    while done == 'n':
        print("Enter done if you are done selecting toppings, or enter another topping.")
        user_input = input().lower()
        if user_input == 'done':
            break
        while user_input != 'sprinkles' and user_input != 'gummy bears' and user_input != 'oreos' and user_input != 'done':
            print("Please put in a valid topping type.")
            user_input = input().lower()
        if user_input == 'done':
            done = 'y'
        else:
            if user_input == 'sprinkles':
                print(f"Topping {user_input} added for $0.15")
            user_choice_toppings.append(user_input)
    users_toppings = Toppings(user_name, user_choice_toppings)
    print('Your order so far:')
    
        

    print("Would you like to order another ice cream? (Yes/No)")
    print("Please input Yes or No!")