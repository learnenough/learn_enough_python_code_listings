import calendar

def dayname(time):
  """Return the name of the day of the week for the given time."""
  return calendar.day_name[time.weekday()]
