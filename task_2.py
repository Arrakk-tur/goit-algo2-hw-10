class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

    def __repr__(self):
        return f"{self.first_name} {self.last_name} ({self.age} років)"


def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    selected_teachers = []

    while uncovered_subjects:
        best_teacher = None
        best_cover = set()

        for teacher in teachers:
            cover = teacher.can_teach_subjects & uncovered_subjects
            if not cover:
                continue

            if (best_teacher is None or
                len(cover) > len(best_cover) or
                (len(cover) == len(best_cover) and teacher.age < best_teacher.age)):
                best_teacher = teacher
                best_cover = cover

        if not best_teacher:
            return None

        # Призначення предметів викладачу
        best_teacher.assigned_subjects = best_cover
        selected_teachers.append(best_teacher)

        # Оновлення списку непокритих предметів
        uncovered_subjects -= best_cover

        # Видалення викладача зі списку доступних
        teachers.remove(best_teacher)

    return selected_teachers


if __name__ == '__main__':
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}

    teachers = [
        Teacher("Олександр", "Іваненко", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Сергій", "Коваленко", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Дмитро", "Бондаренко", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")