

words = ["foo", "bar", "baz"]
def map1(word):
  return [word, 1]

arr = ["foo", [1,1]]
def reduce1(arr):
  return [ arr[0], sum(arr[1])]