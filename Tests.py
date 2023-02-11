def cubes(number):

   return number*number*number

def getCubes(range_of_nums):

   for i in range(range_of_nums):

       yield cubes(i)

cube_object = getCubes(5)

print(list(cube_object))