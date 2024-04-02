def activity_selection(activities):
  
  activities.sort(key=lambda x: x[1])

  selected_activities = []

  selected_activities.append(activities[0])

  for i in range(1, len(activities)):

    if activities[i][0] >= selected_activities[-1][1]:
      selected_activities.append(activities[i])

  return selected_activities

activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = activity_selection(activities)
print(selected_activities)
