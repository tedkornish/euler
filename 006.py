nums = range(1, 100 + 1)

square_of_sum = sum(nums) ** 2
sum_of_squares = sum(map(lambda x: x ** 2, nums))

print abs(sum_of_squares - square_of_sum)