from sets import Set

with open('input/day3.txt', 'r') as f:
  [wire1_input, wire2_input] = f.readlines()
  wire1_input = wire1_input.strip().split(',')
  wire2_input = wire2_input.strip().split(',')

def format_location_to_string(location):
  return str(location[0]) + "," + str(location[1])

def process_instruction(instruction, start_location):
  [x, y, total_traveled] = start_location
  direction = instruction[0]
  distance = int(instruction[1:])
  if direction == 'U':
    y += distance
  elif direction == 'D':
    y -= distance
  elif direction == 'L':
    x -= distance
  elif direction == 'R':
    x += distance
  total_traveled += distance
  return [x, y, total_traveled]

def intersect(segment1, segment2):
  segment1_is_horizontal = segment1[0][1] == segment1[1][1]
  segment2_is_horizontal = segment2[0][1] == segment2[1][1]

  if (segment1_is_horizontal == segment2_is_horizontal):
    return None
  
  if segment1_is_horizontal:
    segment_horizontal = segment1
    segment_vertical = segment2
  else:
    segment_horizontal = segment2
    segment_vertical = segment1

  pre_segment_traveled_1 = segment1[0][2]
  pre_segment_traveled_2 = segment2[0][2]
  total_traveled = pre_segment_traveled_1 + pre_segment_traveled_2

  [left, right] = segment_horizontal if segment_horizontal[0][0] < segment_horizontal[1][0] else [segment_horizontal[1], segment_horizontal[0]]
  [top, bottom] = segment_vertical if segment_vertical[0][1] > segment_vertical[1][1] else [segment_vertical[1], segment_vertical[0]]

  if (left[0] < top[0] and right[0] > top[0]) and (left[1] < top[1] and left[1] > bottom[1]):
    intersection_x, intersection_y = top[0], left[1]
    total_traveled += abs(intersection_x - segment_horizontal[0][0])
    total_traveled += abs(intersection_y - segment_vertical[0][1])
    intersection = [intersection_x, intersection_y, total_traveled]
    return intersection
  else:
    return None

def get_closest_intersection_to_zero(wire1_instructions, wire2_instructions, use_manhattan):
  intersections = []

  wire1_location = [0, 0, 0]
  wire1_segments = []
  for i, instruction in enumerate(wire1_instructions):
    end_location = process_instruction(instruction, wire1_location)
    wire1_segments.append([wire1_location, end_location])
    wire1_location = end_location

  wire2_location = [0, 0, 0]
  wire2_segments = []
  for i, instruction in enumerate(wire2_instructions):
    end_location = process_instruction(instruction, wire2_location)
    wire2_segments.append([wire2_location, end_location])
    wire2_location = end_location
  
  for segment1 in wire1_segments:
    for segment2 in wire2_segments:
      intersection = intersect(segment1, segment2)
      if (intersection != None):
        intersections.append(intersection)

  if (use_manhattan):
    smallest_manhattan_distance = 10000000000000000
    for intersection in intersections:
      manhattan = abs(intersection[0]) + abs(intersection[1])
      if manhattan < smallest_manhattan_distance:
        smallest_manhattan_distance = manhattan

    return smallest_manhattan_distance
  else:
    smallest_traveled_distance = 100000000000000
    for intersection in intersections:
      traveled = intersection[2]
      if traveled < smallest_traveled_distance:
        smallest_traveled_distance = traveled

    return smallest_traveled_distance


assert get_closest_intersection_to_zero("R8,U5,L5,D3".split(","), "U7,R6,D4,L4".split(","), True) == 6
assert get_closest_intersection_to_zero("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","), "U62,R66,U55,R34,D71,R55,D58,R83".split(","), True) == 159
assert get_closest_intersection_to_zero("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","), "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","), True) == 135

print "Part 1: " + str(get_closest_intersection_to_zero(wire1_input, wire2_input, True))

assert get_closest_intersection_to_zero("R8,U5,L5,D3".split(","), "U7,R6,D4,L4".split(","), False) == 30
assert get_closest_intersection_to_zero("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","), "U62,R66,U55,R34,D71,R55,D58,R83".split(","), False) == 610
assert get_closest_intersection_to_zero("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","), "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","), False) == 410

print "Part 2: " + str(get_closest_intersection_to_zero(wire1_input, wire2_input, False))