def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


save = {}
motive = []
def weekly_goals(day,*goal):
    print(f'your set goals for the day:')
    for g in goal:
        print(f'-{g}')
    print(f' \n Have a happy {day} sir.')
    save[day] = goal
    motivation = input('what motivates you today?')
    results = f'{motivation} and Allah will guide us through.'
    motive.append(motivation.lower())
    print(f'{goal} and {motivation} have been saved.')
    return results       

