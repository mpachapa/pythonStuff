def arithmetic_arranger(problems):
  import re
  # Checks to see if more than 5 problems are passed
  if len(problems) > 5:
    return "Error: Too many problems."
  for i in problems: # Looping through the problems
    if re.search('[a-zA-Z]',i): # Checks only if digits were passed
      return "Error: Numbers must only contain digits."
    for j in problems: # Checks number of digits
      tmp = j.split()
      if len(tmp[0]) > 4 or len(tmp[2]) > 4:
        return "Error: Numbers cannot be more than four digits."
    if "+" in i and "-" in i:  # Checks which opperators are passed
      break
    else:
      return "Error: Operator must be '+' or '-'."

  
    return arranged_problems
