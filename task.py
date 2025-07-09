print('----------------------tuples_examples----------------------')




#1. Tuple for Min/Max
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([3, 8, 1, 6])
print(result) 


#Use: Functions often return tuples to bundle multiple values.

# 2. Tuple Unpacking
def get_coordinates():
    return (25.5, 78.4)

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")


#Use: Assign multiple values quickly.

#3. Tuple for User Data
def create_user(name, age):
    return (name, age)

user = create_user("Nina", 30)
print(user)


#Use: Lightweight record-keeping.

# 4. Dictionary with Tuple Keys
def add_entry(record_dict, key_tuple, value):
    record_dict[key_tuple] = value
    return record_dict

data = add_entry({}, ('Math', '2025'), 'Passed')
print(data)


#Use: Tuples are hashable and can be used as keys.

# 5. Fixed Location Data
def get_location():
    return (19.0760, 72.8777)  # Mumbai

print("Location:", get_location())


#Use: Represent fixed-position data.

#  6. Named Tuples
from collections import namedtuple

Person = namedtuple('Person', 'name age')
p = Person('Arjun', 26)
print(p.name, p.age)


#Use: Readable attribute access while retaining immutability.

# 7. Swapping Values
def swap(x, y):
    x, y = y, x
    return (x, y)

print(swap(5, 10)) 


#Use: Elegant value swapping.

# 8. Game Player Position
def player_position():
    return ('A1', 'B3', 'C2')

print("Moves:", player_position())


#Use: Prevents accidental changes to game states.

# 9. Enumerating with Tuple
def list_with_index(items):
    return [(i, item) for i, item in enumerate(items)]

print(list_with_index(["apple", "banana", "cherry"]))


#Use: Combine index and value cleanly.

# 10. Zipping Lists
def match_pairs(names, scores):
    return list(zip(names, scores))

print(match_pairs(['A', 'B'], [90, 85]))


#Use: Create pairings from two lists.

# 11. Returning Status + Data
def fetch_data():
    return (True, [1, 2, 3])

status, data = fetch_data()
print("Success:", status, "Data:", data)


#Use: Bundle success indicator with payload.

# 12. Time Representation
def get_time():
    return (12, 30, 45)  # hh:mm:ss

print("Time:", get_time())


#Use: Clear representation of structured values.

# 13. Range Tuples
def in_range(value, range_tuple):
    return range_tuple[0] <= value <= range_tuple[1]

print(in_range(5, (1, 10)))  # True


#Use: Represent value ranges cleanly.

# 14. Parameter Packing
def print_args(*args):
    print("Arguments:", args)

print_args(1, 2, 3, "Hello")


#Use: Accept variable arguments as a tuple.

# 15. Data for Plotting
def chart_points():
    return [(1, 2), (2, 4), (3, 6)]

print("Points:", chart_points())


#Use: Coordinates in (x, y) format.




print('----------------------sets_examples----------------------')





#1. Unique Elements
def unique_items(lst):
    return set(lst)

print(unique_items([1, 2, 2, 3, 4, 4]))


#Use: Remove duplicates from a list.

# 2. Set Union
def combined_skills(dev1, dev2):
    return dev1 | dev2

print(combined_skills({"Python", "JS"}, {"C++", "Python"}))


#Use: Combine unique skills from two developers.

# 3. Set Intersection
def common_courses(student1, student2):
    return student1 & student2

print(common_courses({"Math", "Bio"}, {"Bio", "Chem"}))


#Use: Find shared items in datasets.

# 4. Set Difference
def missing_tasks(assigned, completed):
    return assigned - completed

print(missing_tasks({"task1", "task2", "task3"}, {"task2"}))


#Use: Identify what's left to do.

# 5. Symmetric Difference
def unique_visitors(day1, day2):
    return day1 ^ day2

print(unique_visitors({"Alice", "Bob"}, {"Bob", "Carol"}))


#Use: Get elements exclusive to one group.

# 6. Add Items
def add_hobby(hobbies, new_hobby):
    hobbies.add(new_hobby)
    return hobbies

print(add_hobby({"Reading", "Gaming"}, "Painting"))


#Use: Add an element if not present.

# 7. Remove Item (with discard)
def remove_hobby(hobbies, hobby):
    hobbies.discard(hobby)
    return hobbies

print(remove_hobby({"Reading", "Gaming"}, "Gaming"))


#Use: Remove item safely (no error if absent).

# 8. Check Membership
def has_access(user_roles, required):
    return required in user_roles

print(has_access({"admin", "editor"}, "admin"))


#Use: Test for permission or membership.

# 9. Loop Through Set
def print_tags(tags):
    for tag in tags:
        print(tag)

print_tags({"Python", "Dev", "AI"})


#Use: Process unordered unique items.

# 10. Subset Check
def is_subset(sub, full):
    return sub.issubset(full)

print(is_subset({"Python"}, {"Python", "JS"}))


#Use: Validate data containment.

# 11. Superset Check
def has_all_skills(employee_skills, required_skills):
    return employee_skills.issuperset(required_skills)

print(has_all_skills({"Python", "SQL", "Excel"}, {"Python", "SQL"}))


#Use: Verify if all required items are present.

# 12. Clear a Set
def reset_selection(selection):
    selection.clear()
    return selection

print(reset_selection({"A", "B", "C"}))


#Use: Erase all elements.

# 13. Immutable Set (frozenset)
def frozen_choices():
    return frozenset(["Option1", "Option2"])

choices = frozen_choices()
print("Option1" in choices)


#Use: Read-only sets.

# 14. Remove Duplicates from Input
def distinct_words(text):
    return set(text.split())

print(distinct_words("hello world hello universe"))


#Use: Clean up repeated words.

# 15. Compare Preferences
def different_choices(user1, user2):
    return user1.symmetric_difference(user2)

print(different_choices({"Tea", "Coffee"}, {"Juice", "Coffee"}))


#Use: Find mismatched selections.




print('----------------------frozensets_examples----------------------')





#1. Immutable Permissions
def get_permissions():
    return frozenset(["read", "write", "execute"])

print(get_permissions())


#Use: Secure permission sets that can't be modified.

# 2. Valid Nucleotides
def is_valid_sequence(seq):
    valid = frozenset("ATGC")
    return all(char in valid for char in seq)

print(is_valid_sequence("ATGTGCA"))


#Use: Ensure only predefined characters are allowed.

# 3. Role Access Keys
def get_role_keys(role):
    access_map = {
        "admin": frozenset(["edit", "delete", "add"]),
        "user": frozenset(["view"])
    }
    return access_map.get(role, frozenset())

print(get_role_keys("admin"))


#Use: Store immutable access sets for roles.

# 4. Prevent Duplication
def freeze_and_compare(data):
    return frozenset(data)

fs1 = freeze_and_compare(["a", "b", "c"])
fs2 = freeze_and_compare(["c", "a", "b"])
print(fs1 == fs2)


#Use: Order-independent content comparison.

# 5. Hashable Container for Dictionary Keys
def tag_stats():
    return {
        frozenset(["python", "dev"]): 42,
        frozenset(["music", "jazz"]): 15
    }

print(tag_stats())


#Use: Use frozenset as a reliable and hashable key.

# 6. Comparing Frozen Groups
def same_skills(set1, set2):
    return frozenset(set1) == frozenset(set2)

print(same_skills(["SQL", "Excel"], ["Excel", "SQL"]))


#Use: Ensure group equality regardless of order.

# 7. Immutable Survey Answers
def record_answers(answers):
    return frozenset(answers)

ans = record_answers(["Yes", "No", "Maybe"])
print(ans)


#Use: Protect user answers from accidental changes.

# 8. Read-Only Vocabulary
def get_stopwords():
    return frozenset(["the", "is", "in", "and", "on"])

print("is" in get_stopwords())


#Use: Store filter terms safely in NLP tasks.

# 9. Teacher-Class Mapping
def assign_class():
    return {
        "Mr. Kumar": frozenset(["Math", "Physics"]),
        "Ms. Leela": frozenset(["English", "History"])
    }

print(assign_class())


#Use: Maintain immutable subject allocations.

# 10. Track Puzzle States
def current_state(pieces):
    return frozenset(pieces)

print(current_state(["corner", "edge", "center"]))


#Use: Freeze a game's current status.

# 11. Game Achievement Set
def achieved(milestones):
    return frozenset(milestones)

print(achieved(["level1", "boss_defeated"]))


#Use: Record completed tasks securely.

# 12. Immutable Config Options
def get_config_flags():
    return frozenset(["debug", "log", "safe_mode"])

print("debug" in get_config_flags())


#Use: Prevent accidental overrides in configurations.

#13. Math Constants
def immutable_constants():
    return frozenset([3.14, 2.718, 1.618])

print(immutable_constants())


#Use: Lock down core mathematical values.

# 14. Immutable Identity Set
def citizen_profile(name, id_num):
    return frozenset([name, id_num])

print(citizen_profile("Aditi", "IND12345"))


#Use: Store identity data safely and unalterably.

# 15. Non-editable Tags on Content
def create_post(title, tags):
    return {"title": title, "tags": frozenset(tags)}

post = create_post("Python Tips", ["coding", "tutorial", "python"])
print(post)


#Use: Lock down tag metadata on user-generated content.





print('----------------------complex_numbers_examples----------------------')





# 1. Create a Complex Number
def make_complex(real, imag):
    return complex(real, imag)

print(make_complex(3, 4))  # 3 + 4j


#Use: Define a number with real and imaginary parts.

#2. Add Complex Numbers
def add_complex(c1, c2):
    return c1 + c2

print(add_complex(3+4j, 1-2j))


#Use: Sum currents or signals in electronics.

# 3. Multiply Complex Numbers
def multiply_complex(c1, c2):
    return c1 * c2

print(multiply_complex(2+3j, 4+5j))


#Use: Perform transformations in electrical engineering.

# 4. Get Magnitude (Absolute Value)
def magnitude(z):
    return abs(z)

print(magnitude(3+4j))  # 5.0


#Use: Calculate vector length or signal amplitude.

# 5. Get Phase Angle
import cmath

def get_phase(z):
    return cmath.phase(z)

print(get_phase(1+1j))  # ≈ 0.785 rad


#Use: Analyze the phase of a wave or signal.

# 6. Convert to Polar Coordinates
def to_polar(z):
    return cmath.polar(z)

print(to_polar(1+1j))


#Use: Express complex number in polar form (r, θ).

# 7. Convert from Polar to Complex
def from_polar(r, theta):
    return cmath.rect(r, theta)

print(from_polar(2, cmath.pi/4))


#Use: Construct signal from magnitude and phase.

# 8. Real and Imaginary Parts
def get_parts(z):
    return (z.real, z.imag)

print(get_parts(5+6j))


#Use: Extract components for separate analysis.

# 9. Complex Conjugate
def conjugate(z):
    return z.conjugate()

print(conjugate(4+3j))  # 4 - 3j


#Use: Normalize signals and remove imaginary parts.

# 10. Check if Purely Imaginary
def is_imaginary(z):
    return z.real == 0

print(is_imaginary(0+4j))


#Use: Filter purely imaginary signals in analysis.

# 11. Signal Reflection (Negative)
def reflect_signal(z):
    return -z

print(reflect_signal(3+2j))


#Use: Mirror signal across origin in complex plane.

# 12. Divide Complex Numbers
def divide_complex(c1, c2):
    return c1 / c2

print(divide_complex(4+2j, 1+1j))


#Use: Perform impedance division in circuits.

# 13. Power of a Complex Number
def power_complex(z, n):
    return z ** n

print(power_complex(1+1j, 3))


#Use: Model oscillating systems or growth over time.

# 14. Filter Out Low-Magnitude Signals
def filter_weak_signals(data, threshold):
    return [z for z in data if abs(z) >= threshold]

signals = [1+1j, 0.1+0.2j, 5+0j]
print(filter_weak_signals(signals, 1))


#Use: Eliminate noise in signal processing.

# 15. Fourier Component Example
def simulate_fourier():
    return sum([cmath.rect(1, 2 * cmath.pi * f * 0.1) for f in range(3)])

print(simulate_fourier())


#Use: Sum wave harmonics in signal decomposition.


