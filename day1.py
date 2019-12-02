with open('day1-input.txt', 'r') as f:
  lines = map(int, f.readlines())

def get_fuel_needed(mass):
  return (mass / 3) - 2

# part 1
fuel_part_1 = reduce(lambda acc, mass: acc + get_fuel_needed(mass), lines, 0)
print("Part 1: " + str(fuel_part_1))

# part 2
def get_fuel_needed_with_fuel_mass(mass):
  total_fuel = get_fuel_needed(mass)
  fuel_added_last = total_fuel
  while get_fuel_needed(fuel_added_last) > 0:
    fuel_added_last = get_fuel_needed(fuel_added_last)
    total_fuel += fuel_added_last
  return total_fuel

fuel_part_2 = reduce(lambda acc, mass: acc + get_fuel_needed_with_fuel_mass(mass), lines, 0)

print("Part 2: " + str(fuel_part_2))