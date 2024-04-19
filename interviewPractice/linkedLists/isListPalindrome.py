# https://app.codesignal.com/interview-practice/question/HmNvEkfFShPhREMn4/description

# Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

# Given a singly linked list of integers, determine whether or not it's a palindrome.

# Note: in examples below and tests preview linked lists are presented as arrays just for simplicity of visualization: in real data you will be given a head node l of the linked list

# Example

# For l = [0, 1, 0], the output should be
# solution(l) = true;

# For l = [1, 2, 2, 3], the output should be
# solution(l) = false.

class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(l):
  slow = fast = l

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  # reverse second half
  prev, curr = None, slow

  while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

  # compare two halves
  while prev:
    if prev.value != l.value:
      return False

    l = l.next
    prev = prev.next

  return True
        
