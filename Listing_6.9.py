.
.
.
numbers = range(1, 101)      # 1 up to 100

# sum: Imperative solution
def imperative_sum(numbers):
    total = 0
    for n in numbers:
      total += n
    return total

print(imperative_sum(numbers))
