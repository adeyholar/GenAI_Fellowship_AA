import os
print("Current Directory in VS Code:", os.getcwd())
from log_utils import read_log, write_summary, append_log

log_file = r"C:\Users\adeol\ai\GenAI_Fellowship_AA\BaseCamp_1\Lesson_8_Base_Camp_Session1\network.log"
summary_file = r"C:\Users\adeol\ai\GenAI_Fellowship_AA\BaseCamp_1\Lesson_8_Base_Camp_Session1\summary.txt"
new_entry = "2025-06-13 Router3 ERROR: Timeout"

print("Append Result:", append_log(log_file, new_entry))
log_lines = read_log(log_file)
print("\nLog Contents:")
for line in log_lines:
    print(line)
print("\nWrite Result:", write_summary(summary_file, log_lines))