
MAX_SCORE = 100
MIN_SCORE = 0
DATA_FILE = "students.txt"
FIELD_DELIMITER = "|" 
SCORE_DELIMITER = ","

# standard grading scale using list
GRADE_CUTOFFS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
]
FAILING_GRADE = "F"
#does repeated functions 
def is_valid_score(score):
    return MIN_SCORE <= score <= MAX_SCORE

def is_valid_text(text):
    return text.strip() != "" and FIELD_DELIMITER not in text

def calculate_average(scores):
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    for cutoff, letter in GRADE_CUTOFFS:
        if average >= cutoff:
            return letter
    return FAILING_GRADE
#file saving
def save_student(name, student_id, scores):
    score_text = SCORE_DELIMITER.join(str(s) for s in scores)
    line = name + FIELD_DELIMITER + student_id + FIELD_DELIMITER + score_text + "\n"
    f = open(DATA_FILE, "a", encoding="utf-8")
    f.write(line)
    f.close()
#file handling 
def load_students():
    students = []
    try:
        f = open(DATA_FILE, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(FIELD_DELIMITER)
            if len(parts) != 3:
                continue
            name, student_id, score_text = parts
            
            try:
                scores = []
                for s in score_text.split(SCORE_DELIMITER):
                    if s != "":
                        scores.append(float(s))
            except ValueError:
                continue
                
            students.append({"name": name, "id": student_id, "scores": scores})
        f.close()
    except FileNotFoundError:
        pass
        
    return students
# student ID of course 
def id_exists(student_id):
    all_studs = load_students()
    for s in all_studs:
        if s["id"] == student_id:
            return True
    return False
#calculates average 
def format_student(student):
    average = calculate_average(student["scores"])
    letter = get_letter_grade(average)
    name = student["name"].title()
    
    scores_text = ", ".join(f"{s:g}" for s in student["scores"])
    
    res = name.ljust(20) + " ID: " + student["id"].upper().ljust(10) + " Scores: [" + scores_text + "]" + "  Avg: " + f"{average:.1f}".rjust(5) + "  Grade: " + letter
    return res
#code for option 2
def display_all_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
        
    print("\n" + "=" * 80)
    print("STUDENT RECORDS")
    print("=" * 80)
    
    for student in students:
        print(format_student(student))
        
    print("=" * 80)
    
    all_scores = []
    for student in students:
        for s in student["scores"]:
            all_scores.append(s)
            
    if all_scores:
        class_average = calculate_average(all_scores)
        print("Class average: " + f"{class_average:.1f}")
        
        max_s = max(all_scores)
        min_s = min(all_scores)
        print("Highest score: " + f"{max_s:g}" + " (" + find_owner(students, max_s) + ")")
        print("Lowest score:  " + f"{min_s:g}" + " (" + find_owner(students, min_s) + ")")

def find_owner(students, target_score):
    for student in students:
        if target_s_in_list(target_score, student["scores"]): 
            return student["name"].title()
    return "unknown"

def target_s_in_list(target, lst):
    for x in lst:
        if x == target:
            return True
    return False

def read_scores():
    scores = []
    print("Enter assignment scores (" + str(MIN_SCORE) + "-" + str(MAX_SCORE) + "). Type 'done' when finished.")
    
    while True:
        entry = input("  Score " + str(len(scores) + 1) + ": ").strip().lower()
        if entry == 'done':
            break
            
        try:
            score = float(entry)
        except ValueError:
            print("  Please enter a number or 'done'.")
            continue
            
        if not is_valid_score(score):
            print("  Score must be between " + str(MIN_SCORE) + " and " + str(MAX_SCORE) + ".")
            continue
        scores.append(score)
        
    return scores

def add_student_flow():
    name = input("Student name: ").strip()
    if not is_valid_text(name):
        print("name is INVALID" + FIELD_DELIMITER + "'.")
        return
        
    student_id = input("Student ID: ").strip()
    if not is_valid_text(student_id):
        print("invalid ID" + FIELD_DELIMITER + "'.")
        return
        
    if id_exists(student_id):
        print("that ID already exists.")
        return
        
    scores = read_scores()
    if len(scores) == 0: 
        print("a record is required.")
        return
        
    save_student(name, student_id, scores)
    
    average = calculate_average(scores)
    print("Saved " + name.title() + " - average " + f"{average:.1f}" + " (" + get_letter_grade(average) + ")")

def main():
    while True:
        print("\n=== Grading System ===")
        print("1. Add student")
        print("2. View all students")
        print("3. Quit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_student_flow()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            print("bye!")
            break
        else:
            print("Please enter 1-3.")

if __name__ == "__main__":
    main()