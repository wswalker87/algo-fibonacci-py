import functools
def fibonacci(n):
  # create an array of 0 and 1 since those are the first nums.
  # first solution starts down one line 
  fullArray = [0, 1]
  # loop over the array and do the math
  counter = n
  index = 1
  
  while counter > 1:
    temp_num = fullArray[index - 1] + fullArray[index]
    fullArray.append(temp_num)
    counter -= 1
    index += 1

  return fullArray[n]