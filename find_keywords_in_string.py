# check for a list of items inside a list of items

ingredients = ['pepperoni','cheese','sausage']
orders = [(1, 'cheese, anchovi, lettuce'), (2, 'cheese'), (3, 'pepperoni, sausage'), (4, 'lettuce'), (5, 'ketchup, sausage')]

accepted_orders = []
rejected_orders = []

for index, items in orders:
    if max([i in items for i in ingredients]):
        accepted_orders.append((index, items))
    else:
        rejected_orders.append((index, items))

print()
print('Desired Ingredients:')
print(ingredients)

print()
print('Accepted Orders:')
for a in accepted_orders:
    print(a)

print()
print('Rejected Orders:')
for r in rejected_orders:
    print(r)
