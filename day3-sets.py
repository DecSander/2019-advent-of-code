from sets import Set

with open('input/day3.txt', 'r') as f:
  [wire1_input, wire2_input] = f.readlines()
  wire1_input = wire1_input.strip().split(',')
  wire2_input = wire2_input.strip().split(',')

def format_location_to_string(location):
  return str(location[0]) + "," + str(location[1])

def process_instruction(instruction, start_location):
  [x, y] = start_location
  direction = instruction[0]
  distance = int(instruction[1:])
  if direction == 'U':
    locations = map(lambda val: [x, val], range(y, y + distance))
    y += distance
  elif direction == 'D':
    locations = map(lambda val: [x, val], range(y - distance, y))
    y -= distance
  elif direction == 'L':
    locations = map(lambda val: [val, y], range(x - distance, x))
    x -= distance
  elif direction == 'R':
    locations = map(lambda val: [val, y], range(x, x + distance))
    x += distance
  return locations, [x, y]

def get_closest_intersection_to_zero(wire1_instructions, wire2_instructions):
  intersections = []

  wire1_location = [0, 0]
  all_wire_1_locations = []
  for i, instruction in enumerate(wire1_instructions):
    [new_locations, wire1_location] = process_instruction(instruction, wire1_location)
    for location in new_locations:
      all_wire_1_locations.append(format_location_to_string(location))
  all_wire_1_locations.remove(format_location_to_string([0, 0]))

  wire2_location = [0, 0]
  for instruction in wire2_instructions:
    [new_locations, wire2_location] = process_instruction(instruction, wire2_location)
    for location in new_locations:
      if format_location_to_string(location) in all_wire_1_locations:
        intersections.append(location)

  smallest_manhattan_value = 10000000000000000
  for intersection in intersections:
    manhattan = abs(intersection[0]) + abs(intersection[1])
    if manhattan < smallest_manhattan_value:
      smallest_manhattan_value = manhattan

  return smallest_manhattan_value

print get_closest_intersection_to_zero(wire1_input, wire2_input)