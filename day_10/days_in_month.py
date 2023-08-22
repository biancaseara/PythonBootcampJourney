def is_leap(year):
  '''
  Take a given year then return if is a leap year.
  '''
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month > len(month_days) or month < len(month_days):
    return "You didn't provide a valid number."
  index = month - 1
  if not is_leap(year):
    return month_days[index]
  elif is_leap(year):
    if month_days[index] == month_days[1]:
      month_days[1] += 1
    return month_days[index]

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


