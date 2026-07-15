def average_score(*marks):
    total = sum(marks)
    average = total / len(marks)
    return average

print(average_score(85, 90, 78, 92, 88))
print(average_score(75, 80, 70))