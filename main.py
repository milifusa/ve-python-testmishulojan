"""
You are the designated 'technology specialist' of a local Sporting Organization
(S.O.). Numerous teams of athletes participate in races organized by the
association. Each time, you receive a string containing the race results for
all participating teams. Here's an example string representing the individual
results of a team of 5 runners:

'01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17'

In this format, each part of the string represents the time taken by a runner
in the format 'h|m|s', where 'h' represents hours, 'm' represents minutes,
and 's' represents seconds. Each result is separated by a comma or a comma
followed by a space.

To evaluate and compare the performance of the teams, you need to calculate
three statistics: range, average, and median.

Range: The range is the difference between the lowest and highest values in a
set of numbers. For example, given the set {4, 6, 9, 3, 7},
the lowest value is 3 and the highest value is 9.
Therefore, the range is calculated as 9 - 3 = 6.

Average: The average, also known as the mean, is obtained by adding up all the
numbers in a set and dividing the sum by the total count of numbers.

Median: The median is the middle number that separates the higher half from the
lower half of a data sample. If the sample size is odd, the median is the
middle value. If the sample size is even, the median is the mean of the two
middle values.

Your task is to calculate these three values and return a string in the
following format:

'Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss'

where 'hh', 'mm', and 'ss' represent two-digit integers
(represented as strings).

Please note:

If a result in seconds has decimals (e.g., ab.xy...), it should be truncated to
'ab'. If the given string is empty, your function should return an empty string
as well.
"""


def stat(s):
    if not s:
        return ''
    
    # Helper function to convert time string 'h|m|s' to total seconds
    def to_seconds(time):
        h, m, s = map(int, time.split('|'))
        return h * 3600 + m * 60 + s
    
    # Helper function to convert total seconds to 'hh|mm|ss' format
    def to_hms(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}|{m:02}|{s:02}"
    
    # Parse the times and convert them to seconds
    times = list(map(to_seconds, s.split(', ')))
    
    # Sort the times in ascending order
    times.sort()
    
    # Calculate range, average, and median
    range_time = times[-1] - times[0]
    average_time = sum(times) // len(times)
    median_time = (times[len(times) // 2] if len(times) % 2 != 0 
                   else (times[len(times) // 2 - 1] + times[len(times) // 2]) // 2)
    
    return f"Range: {to_hms(range_time)} Average: {to_hms(average_time)} Median: {to_hms(median_time)}"


# Test cases
test_1 = stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17")

assert test_1 == "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34", \
    "❌ Test 1 failed!"
print("✅ Test 1 passed!")

test_2 = stat(
    "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")

assert test_2 == "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00", \
    "❌ Test 2 failed!"
print("✅ Test 2 passed!")

test_3 = stat("")

assert test_3 == "", "❌ Test 3 failed!"
print("✅ Test 3 passed!")
