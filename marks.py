import csv

class Pupil:
    def __init__(self, last_name, first_name, grades):
        self.last_name = last_name
        self.first_name = first_name
        self.grades = grades

def load_data(file_path):
    pupil_list = []
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for entry in reader:
            last_name = entry[0]
            first_name = entry[1]
            grades = list(map(int, entry[2:]))  
            pupil_list.append(Pupil(last_name, first_name, grades))
    return pupil_list

def compute_statistics(pupil_list):
    total_grades = [0, 0, 0, 0]  
    highest_total = 0
    top_pupils = []
    failing_count = 0

    for pupil in pupil_list:
        total_grades_for_pupil = sum(pupil.grades)
        
        for index in range(4):
            total_grades[index] += pupil.grades[index]

        if total_grades_for_pupil > highest_total:
            highest_total = total_grades_for_pupil
            top_pupils = [(pupil.last_name, pupil.first_name)]
        elif total_grades_for_pupil == highest_total:
            top_pupils.append((pupil.last_name, pupil.first_name))

        if 2 in pupil.grades:
            failing_count += 1

    average_grades = [total / len(pupil_list) for total in total_grades]

    return average_grades, highest_total, top_pupils, failing_count

def run():
    file_path = 'grades.csv'
    pupil_list = load_data(file_path)
    average_grades, highest_total, top_pupils, failing_count = compute_statistics(pupil_list)

    subjects_list = ['Алгебра', 'Русский язык', 'Физика', 'История']
    print("Средний балл по предметам:")
    for subject, avg in zip(subjects_list, average_grades):
        print(f"{subject}: {avg:.2f}")

    print(f"\nНаивысшая сумма баллов: {highest_total}")

    top_pupils.sort()  
    print("Ученики с наивысшей суммой баллов:")
    for last_name, first_name in top_pupils:
        print(f"{last_name} {first_name}")

    print(f"\nКоличество учеников, получивших хотя бы одну отметку «2»: {failing_count}")

if __name__ == "__main__":
    run()

