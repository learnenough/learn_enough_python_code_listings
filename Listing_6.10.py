.
.
.
numbers = range(1, 11)  # 1 up to 10

# sum: Imperative solution
def imperative_sum(numbers):
    total = 0
    for n in numbers:
      total += n
    return total

print(imperative_sum(numbers))
print(sum(numbers))
