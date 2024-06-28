# Feature: Fearful Number Associations

#   As a person with a unique mental illness
#   I want to determine if I'm afraid of a number on a specific day
#   So that I can manage my fears effectively

#   Scenario: Check if a number triggers fear on a specific day
#     Given today is a specific day of the week
#     And I have a particular number
#     When I check if I'm afraid of the number
#     Then the result should indicate whether I'm afraid or not



Create a function that take 2 urg
Create a dictionary to associate days of the week with numbers
    // Check if the given day is in the associations dictionary

def is_afraid(day_of_week, number):
    # Define the number associations for each day of the week
    associations = {
        "Monday": [12],
        "Tuesday": [x for x in range(96, 100)],
        "Wednesday": [34],
        "Thursday": [0],
        "Friday": [x for x in range(0, 100, 2)],
        "Saturday": [56],
        "Sunday": [666, -666]
    }

    # Check if the given number is associated with the given day
    if day_of_week in associations:
        return number in associations[day_of_week]
    else:
        return False



# The time complexity of the is_afraid function is primarily determined by the dictionary look-up and the membership test (number in associations[day_of_week]). In terms of time complexity:

# The dictionary look-up has an average and worst-case time complexity of O(1) due to hash-based look-up in Python dictionaries.
# The membership test (number in associations[day_of_week]) has an average case of O(k), where k is the number of elements in the list associated with the day of the week. The worst case would be O(n), where n is the total number of associations.
# In terms of space complexity, the function uses a dictionary to store the associations, which takes up space proportional to the number of days of the week. However, since the number of days is fixed and small (7 days), the space complexity remains O(1).

# Overall, the provided code is already quite efficient for this specific problem and likely has the best possible time and space complexity given the problem's constraints.