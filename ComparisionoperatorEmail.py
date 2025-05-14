weight =input('Weight: ')
weight =int(weight)
unit =input ('(L)bs or (K)g : ').strip().lower()
weight_kg_conv = float(0.453592)
weight_lbs_conv= float(2.20462)
if unit =='l':
    print (f'You are {weight * weight_kg_conv:.2f} kgs')
else:
    print(f'You are {weight *weight_lbs_conv:.2f} lbs')

