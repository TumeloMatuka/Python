
# Create a shopping cart programme that will continuously ask the user for a food item and the price of that prduct.
# Have an exit clause if the wishes to stop adding to their cart.
# At the end show the items and the total cost to the user.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit : ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price for {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----- YOUR SHOPPING CART -----")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price
 
print("\n")       
print(f"Total cost: R{total}")
    