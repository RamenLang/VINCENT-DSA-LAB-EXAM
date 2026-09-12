class Student:
    def __init__(self, student_id, name, course, year_level):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.year_level = year_level

    def __str__(self):
        return (f"Student ID: {self.student_id}\n"
                f"Student Name: {self.name}\n"
                f"Course: {self.course}\n"
                f"Year Level: {self.year_level}")

    def short_str(self):
        return f"[{self.student_id} - {self.name}]"



class DynamicArray:
    INITIAL_CAPACITY = 5

    def __init__(self):
        self.capacity = DynamicArray.INITIAL_CAPACITY
        self.count = 0                                   
        self.array = [None] * self.capacity              


    def resize(self):
        """Doubles the capacity of the underlying array and copies old data over."""
        old_array = self.array
        new_capacity = self.capacity * 2
        new_array = [None] * new_capacity

        for i in range(self.count):
            new_array[i] = old_array[i]

        self.array = new_array
        self.capacity = new_capacity
        print(f"[Array resized] New capacity: {self.capacity}")


    def add(self, student):
        if self.count == self.capacity:
            print("Array is full.")
            self.resize()
        self.array[self.count] = student
        self.count += 1

    def get(self, index):
        if 0 <= index < self.count:
            return self.array[index]
        return None

    def set(self, index, student):
        if 0 <= index < self.count:
            self.array[index] = student
            return True
        return False

    def search(self, student_id):
        """Returns the index of the student with the given ID, or -1 if not found."""
        for i in range(self.count):
            if self.array[i].student_id == student_id:
                return i
        return -1

    def remove(self, student_id):
        index = self.search(student_id)
        if index == -1:
            return False

        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]

        self.array[self.count - 1] = None
        self.count -= 1
        return True

    def size(self):
        return self.count

    def is_empty(self):
        return self.count == 0

    def display(self):
        if self.is_empty():
            print("No student records to display.")
            return

        print("-" * 50)
        for i in range(self.count):
            print(f"Record #{i + 1}")
            print(self.array[i])
            print("-" * 50)

    def display_info(self):
        print(f"Number of students : {self.count}")
        print(f"Array capacity     : {self.capacity}")

        if self.is_empty():
            print("Students in array  : (none)")
            return

        names = " ".join(f"[{self.array[i].name}]" for i in range(self.count))
        print(f"Students in array  : {names}")



def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def read_year_level(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and 1 <= int(value) <= 6:
            return int(value)
        print("Please enter a valid year level (a whole number, e.g. 1-6).")


def read_year_level_optional(prompt, current_value):
    """Same validation as read_year_level, but an empty entry keeps current_value."""
    while True:
        value = input(prompt).strip()
        if value == "":
            return current_value
        if value.isdigit() and 1 <= int(value) <= 6:
            return int(value)
        print("Please enter a whole number 1-6, or leave blank to keep the current value.")


def read_menu_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")



def print_menu():
    print("\n================================")
    print("     STUDENT RECORD MANAGER")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")


def add_student(records):
    print("\n-- Add Student --")
    student_id = read_non_empty("Student ID: ")

    if records.search(student_id) != -1:
        print(f"A student with ID {student_id} already exists.")
        return

    name = read_non_empty("Student Name: ")
    course = read_non_empty("Course: ")
    year_level = read_year_level("Year Level: ")

    records.add(Student(student_id, name, course, year_level))
    print("Student added successfully.")


def display_students(records):
    print("\n-- Student List --")
    records.display()


def search_student(records):
    print("\n-- Search Student --")
    student_id = read_non_empty("Enter Student ID to search: ")
    index = records.search(student_id)

    if index == -1:
        print(f"No student found with ID {student_id}.")
    else:
        print("Student found:")
        print(records.get(index))


def update_student(records):
    print("\n-- Update Student --")
    student_id = read_non_empty("Enter Student ID to update: ")
    index = records.search(student_id)

    if index == -1:
        print(f"No student found with ID {student_id}.")
        return

    print("Leave a field blank to keep its current value.")
    current = records.get(index)

    new_name = input(f"New Name [{current.name}]: ").strip()
    new_course = input(f"New Course [{current.course}]: ").strip()
    new_year = read_year_level_optional(
        f"New Year Level [{current.year_level}]: ", current.year_level
    )

    updated = Student(
        current.student_id,
        new_name if new_name else current.name,
        new_course if new_course else current.course,
        new_year,
    )

    records.set(index, updated)
    print("Student updated successfully.")


def remove_student(records):
    print("\n-- Remove Student --")
    student_id = read_non_empty("Enter Student ID to remove: ")

    if records.remove(student_id):
        print("Student removed successfully.")
    else:
        print(f"No student found with ID {student_id}.")


def main():
    records = DynamicArray()

    while True:
        print_menu()
        choice = read_menu_choice("Enter your choice: ", {"1", "2", "3", "4", "5", "6", "7"})

        if choice == "1":
            add_student(records)
        elif choice == "2":
            display_students(records)
        elif choice == "3":
            search_student(records)
        elif choice == "4":
            update_student(records)
        elif choice == "5":
            remove_student(records)
        elif choice == "6":
            records.display_info()
        elif choice == "7":
            print("Exiting Student Record Manager. Goodbye!")
            break


if __name__ == "__main__":
    main()