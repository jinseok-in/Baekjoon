import sys

def time_to_seconds(time_str):
  h, m, s = map(int, time_str.split(':'))
  return h * 3600 + m * 60 + s

def seconds_to_clock_int(total_seconds):
  total_seconds %= 86400 
  
  s = total_seconds % 60
  total_minutes = total_seconds // 60
  m = total_minutes % 60
  h = total_minutes // 60
  
  clock_integer = h * 10000 + m * 100 + s
  return clock_integer

def solve():
  line = sys.stdin.readline().split()
  start_str = line[0]
  end_str = line[1]

  start_seconds = time_to_seconds(start_str)
  end_seconds = time_to_seconds(end_str)

  count = 0
  current_seconds = start_seconds

  while True:
    clock_int = seconds_to_clock_int(current_seconds)
    
    if clock_int % 3 == 0:
      count += 1
      
    if current_seconds == end_seconds:
      break
      
    current_seconds = (current_seconds + 1) % 86400 

  return count

results = []
for _ in range(3):
  results.append(solve())

for result in results:
  print(result)