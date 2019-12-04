input_value = '387638-919123'
input_range = map(int, input_value.split('-'))

def is_valid(i, pair_can_be_in_group):
  v = str(i)
  highest = int(v[0])
  has_double = False

  for i, char in enumerate(v):
    if int(char) < highest:
      return False
    highest = int(char)
    if char == v[i-1] and char != v[i-2] and (pair_can_be_in_group or (i+1 == len(v) or char != v[i+1])):
      has_double = True
  result = has_double
  return result

valids_part_1 = 0
for i in range(input_range[0], input_range[1]):
  if is_valid(i, True):
    valids_part_1 += 1

print "Part 1: " + str(valids_part_1)

valids_part_2 = 0
for i in range(input_range[0], input_range[1]):
  if is_valid(i, False):
    valids_part_2 += 1

print "Part 2: " + str(valids_part_2)