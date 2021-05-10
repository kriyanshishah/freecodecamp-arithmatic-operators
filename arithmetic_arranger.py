import re

def arithmetic_arranger(problems, solve = False):
  first=""
  second=""
  lines=""
  sums=""
  strings=""
  
  if(len(problems)>5):
    return 'Error: Too many problems.'

  for problem in problems:
    if(re.search("[^\s 0-9.+-]", problem)):
      if(re.search("[*]", problem) or re.search("[/]", problem)):
        return "Error: Operator must be '+' or '-'."
      return 'Error: Numbers must only contain digits.'
    firstno = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondno = problem.split(" ")[2]
    if(len(firstno) > 4 or len(secondno) > 4):
      return 'Error: Numbers cannot be more than four digits.'
    sum=""
    if(operator == "+"):

      sum = str(int(firstno) + int(secondno))
    elif(operator == "-"):
      sum = str(int(firstno) - int(secondno))

    lengthdash = max(len(firstno), len(secondno)) + 2
    top = str(firstno).rjust(lengthdash)
    bottom = operator + str(secondno).rjust(lengthdash-1)
    line=""
    res = str(sum).rjust(lengthdash)
    for s in range(lengthdash):
      line += "-"
    if(problem != problems[-1]):
      first += top + "    "
      second += bottom + '    '
      lines += line + "    "
      sums += res + "    "
    else:
      first += top
      second += bottom
      lines += line
      sums += res
  if solve:
    strings = first + "\n" + second + "\n" + lines + "\n" + sums 
  else:
    strings = first + "\n" + second + "\n" + lines
  return strings
