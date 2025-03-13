
print("We have many options to choose from")
Toppings = ["Hot fudge", "chocalte chips", "pretzels" and "carmel"]
prompt = "\nEnter your favorite ice cream toppings."
prompt += "\nEnter 'quit' when you are finished. "

Toppings = ""     

while True:
            Toppings = input(prompt)
            if Toppings == "quit":
                break
            else:
                print (f"Those are great choices I love {Toppings.title()}!")