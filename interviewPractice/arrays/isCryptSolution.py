# https://app.codesignal.com/interview-practice/question/yM4uWYeQTHzYewW9H/description

# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence between letters and digits, such that the given arithmetic equation consisting of letters holds true when the letters are converted to digits.

# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping of letters and digits, solution. The array crypt will contain three non-empty strings that follow the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes, the answer is true. If it does not become a valid arithmetic solution, the answer is false.

# Note that number 0 doesn't contain leading zeroes (while for example 00 or 0123 do).

# Example

# For crypt = ["SEND", "MORE", "MONEY"] and

# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]
# the output should be
# solution(crypt, solution) = true.

# When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652 which is correct and a valid arithmetic equation.

def solution(crypt, solution):
  cypher = {}
  
  # populate cypher hashmap
  for i in range(len(solution)):
    cypher[solution[i][0]] = solution[i][1]

  # get decoded word based on cypher
  n1 = decode_word(crypt[0], cypher)
  n2 = decode_word(crypt[1], cypher)
  n3 = decode_word(crypt[2], cypher)
  
  return is_valid_equation(n1, n2, n3)
    
def decode_word(word_in_crypt, cypher):
  num = ''
  
  for char in word_in_crypt:
    if char in cypher:
      num += cypher[char]
      
  return num
    
def is_valid_equation(num1, num2, num3):
  if has_leading_zeroes(num1) or has_leading_zeroes(num2) or has_leading_zeroes(num3):
    return False
      
  return int(num1) + int(num2) == int(num3)
    
def has_leading_zeroes(num):
  if num == '0': return False
  if num[0] == '0': return True
  
  return False
    

