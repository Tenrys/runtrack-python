def round_grades(grades):
  for k, n in enumerate(grades):
    remainder = n % 5 
    if remainder >= 3:
      grades[k] = n + 5 - remainder
  return grades
  
print("Liste de notes arrondies:")
for grade in round_grades([16, 27, 38, 49, 50, 61, 72, 83, 94, 105]):
  print(grade)
  