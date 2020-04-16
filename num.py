number = "4003600000000014"
i = 0
second_digits_sum = 0
first_digit_sum = 0

while i < len(number):
  if i % 2 == 0:
    if len(str(int(number[i]) * 2)) == 2:
      splited_num = list(str(int(number[i]) * 2))
      second_digits_sum += (int(splited_num[0]) + int(splited_num[1]))
    else:
      second_digits_sum += (int(number[i]) * 2)
  else:
    first_digit_sum += int(number[i])
  i+=1

nums_sum = str(second_digits_sum + first_digit_sum)
if (nums_sum[-1] == "0"):
  print("correct card number")
else:
  print("card number is incorrect")
