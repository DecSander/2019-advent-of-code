with open('input/day2.txt', 'r') as f:
  lines = map(int, f.read().split(','))

def handle_simple_two_param_operation(func, position, numbers):
  input1 = numbers[numbers[position + 1]]
  input2 = numbers[numbers[position + 2]]
  return func(input1, input2)

def handle_operation(opcode, position, numbers):
  if (opcode == 1):
    func = lambda x, y: x + y
  elif (opcode == 2):
    func = lambda x, y: x * y
  value = handle_simple_two_param_operation(func, position, numbers)
  output_location = numbers[position + 3]
  numbers[output_location] = value

def modify_numbers(numbers):
  position = 0
  cursor_size = 4
  while position < len(numbers):
    opcode = numbers[position]
    if (opcode == 99):
      return numbers
    elif (opcode == 1 or opcode == 2):
      handle_operation(opcode, position, numbers)
    position += cursor_size
  return numbers

# part 1
day1_numbers = lines[:]
day1_numbers[1] = 12
day1_numbers[2] = 2
modify_numbers(day1_numbers)
print "Part 1: " + str(day1_numbers[0])

# part 2
value_to_be_reached = 19690720
limit = 100
def get_values():
  for noun in range(0, limit):
    for verb in range(0, limit):
      nums = lines[:]
      nums[1] = noun
      nums[2] = verb
      modify_numbers(nums)
      if nums[0] == value_to_be_reached:
        return noun, verb

noun, verb = get_values()
print "Part 2: " + str(100 * noun + verb)