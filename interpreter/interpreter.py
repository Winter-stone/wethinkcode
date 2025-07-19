equation = input('Enter Equation: ').strip().split(" ")
print(f'{float(eval("".join(equation))):.1f}')