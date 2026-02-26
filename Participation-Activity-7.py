'''Participation Activity Week 7
Darian Marie Bruce
This program takes user input for pizza toppings
02/25/2026'''

ask_for_toppings: bool = True

print('To exit the program at any time type "q" into the console.')

while ask_for_toppings:
    toppings_input: str = input("Please type the toppings you want on your pizza: ")
    if not isinstance(toppings_input, str):
        print("Please enter a valid topping.")
        continue
    elif toppings_input.strip().lower() == 'q':
        ask_for_toppings = False
    else:
        print(f"You have typed in {toppings_input}. Your pizza will have {toppings_input} on it.")


print('The program has ended.')