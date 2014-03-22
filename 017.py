# length counts - 0 for a 0 in that column, and a 0 as a placeholder in tens because of irregularities in teens
ones = map(lambda x: len(x), ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
teens = map(lambda x: len(x), ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])
tens = map(lambda x: len(x), ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'])

# x is a number between 1 and 1000
def word_len(x):
  if x == 100: return len('one hundred'.replace(" ", ""))
  elif x == 1000: return len('one thousand'.replace(" ", ""))

  digits = map(lambda x: int(x), list(str(x)))
  one = digits[-1]
  ten = digits[-2] if len(digits) > 1 else False
  hundred = digits[-3] if len(digits) > 2 else False

  count = 0
  if hundred: count += ones[hundred] + len('hundred')
  if hundred and (one != 0 or ten != 0): count += len('and')
  if ten:
    if ten != 1:
      count += tens[ten]
      count += ones[one]
    else:
      count += teens[one]
  if one and ten == 0:
    count += ones[one]
  return count

print sum(map(word_len, range(1, 1000 + 1)))