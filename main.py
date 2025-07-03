# Online Python - IDE, Editor, Compiler, Interpreter
import random
from datetime import datetime, timedelta

# Original cage labels
cages = ["1A", "1B", "1C", "2A", "2B", "2C", "3A", "3B", "3C", "4A", "4B", "4C"]

def generate_random_distribution(date):
    random.shuffle(cages)
    print(f"\nCage Distribution for {date.strftime('%d/%m/%y')}:")
    for i in range(0, len(cages), 3):
        print(f"{cages[i]} | {cages[i+1]} | {cages[i+2]}")

# Start date
start_date = datetime.strptime("02/07/25", "%d/%m/%y")

# Generate cage distribution every 14 days (2 weeks)
for i in range(14):  # For example, 6 future distributions (3 months)
    next_date = start_date + timedelta(days=14 * i)
    generate_random_distribution(next_date) 
print(f"\n Simple Sample Randomizer :for Public use @ Fred2025") 
