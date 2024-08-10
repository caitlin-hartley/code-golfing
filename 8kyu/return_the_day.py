# Complete the function which returns the weekday according to the input number:

# 1 returns "Sunday"
# 2 returns "Monday"
# 3 returns "Tuesday"
# 4 returns "Wednesday"
# 5 returns "Thursday"
# 6 returns "Friday"
# 7 returns "Saturday"
# Otherwise returns "Wrong, please enter a number between 1 and 7"





def whatday(num):
    if num == 1: return 'Sunday'
    elif num == 2: return 'Monday'
    elif num == 3: return 'Tuesday'
    elif num == 4: return 'Wednesday'
    elif num == 5: return 'Thursday'
    elif num == 6: return 'Friday'
    elif num == 7: return 'Saturday'
    else: 
        return "Wrong, please enter a number between 1 and 7"

import codewars_test as test

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(whatday(1), 'Sunday')
        test.assert_equals(whatday(2), 'Monday')
        test.assert_equals(whatday(3), 'Tuesday')
        test.assert_equals(whatday(8), 'Wrong, please enter a number between 1 and 7')
        test.assert_equals(whatday(20), 'Wrong, please enter a number between 1 and 7')