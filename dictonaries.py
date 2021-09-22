monthConversions = {
  "Jan": "January",
  "Feb": "February",
  "Mar": "March",
  "Apr": "April",
  "May": "May",
  "Jun": "June",
  "Jul": "July",
  "Aug": "August",
  "Sep": "September",
  "Oct": "October",
  "Nov": "November",
  "Dec": "December"
}

print(monthConversions["Jan"])
print(monthConversions.get("Jan"))
print(monthConversions.get("Luv", "Not a valid key default value"))
