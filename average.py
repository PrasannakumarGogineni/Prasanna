def average_numbers(*args):
  num = sum(args)
  dec = len(args)
  return num / dec
print(average_numbers(1,2,3,4,5,6,7,8,9,10))