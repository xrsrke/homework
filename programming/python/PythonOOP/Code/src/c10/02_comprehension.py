input_strings = ["1", "5", "28", "123123", "4819"]

output_integers = []
for num in input_strings:
    output_integers.append(int(num))

print(output_integers)

## list comprehensions
output_integers_2 = [(int(num) + 1) for num in input_strings]
print(output_integers_2)

output_integers_3 = [(int(num) + 1) for num in input_strings if len(num) < 3]
print(output_integers_3)