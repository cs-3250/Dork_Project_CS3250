print('\n\n\n')


basket = ['Apple', 'Bun' , 'Cola']
crate = ['Egg', 'Fig', 'Grape']
print('Basket List:' , basket)
print('Basket Elements:' , len(basket))

basket.append('Damson')
print('Item Appended',basket)

print('Last Item Removed:', basket.pop())
print('Basket List:', len(basket))

basket.extend(crate)

print("Extended:" , basket)

del basket[1]

print('Item Removed:' , basket)

del basket[1:3]
print('Slice Removed:' , basket)


    