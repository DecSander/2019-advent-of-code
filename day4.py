input_value = '387638-919123'
input_range = map(int, input_value.split('-'))

def is_valid(i):
  if i < input_range[0] or i > input_range[1]:
    return False
  else:
    v = str(i)
    highest = int(v[0])
    last = None
    has_double = False

    for char in v:
      print char
      if int(char) < highest:
        return False
      highest = int(char)
      if last == char:
        has_double = True
    return has_double

valids = 0
for i in range(000000, 1000000):
  if is_valid(i):
    valids += 1

print valids
