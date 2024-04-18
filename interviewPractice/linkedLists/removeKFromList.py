# https://app.codesignal.com/interview-practice/question/gX7NXPBrYThXZuanm/description

# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

# Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

# Example

# For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
# solution(l, k) = [1, 2, 4, 5];
# For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
# solution(l, k) = [1, 2, 3, 4, 5, 6, 7].

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

# Cleaner solution
def solution(l, k):
  copy = l
  
  while copy:
    if copy.next and copy.next.value == k:
      copy.next = copy.next.next
    else: copy = copy.next
          
  if l and l.value == k: return l.next
  
  return l

# First solution
def solution(l, k):
  head = tmp = ListNode(0)
  
  while l and l.next:
    if l.value != k:
      tmp.next = l
      tmp = tmp.next
    
    if not l.next.next and l.next.value == k:
      tmp.next = None
        
    l = l.next
          
  return head.next