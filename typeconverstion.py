name = input("What is your name ? ")
print(f"Hae {name} nice to meet you")
weight_conv_kg = 0.45
weight = input(f'How much  do you weight in pounds {name}? ')
weight = float(weight)
weight_kgs = weight * weight_conv_kg
print(f'This means your are {weight_kgs:.2f} kilograms')
