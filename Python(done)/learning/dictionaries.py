def ninja_intro(dict):
  for key, val in dict.items():
    print(f'I am {key} and I am {val} belt')
    
ninja_belts = {}

while True:
  ninja_name = input("enter a ninja name: ")
  ninja_belt = input("enter a belt color: ")
  ninja_belts[ninja_name] = ninja_belt
  
  another = input("add another (Y/N)")
  
  if another == "y":
    continue
  else:
    ninja_intro(ninja_belts)
    break
    