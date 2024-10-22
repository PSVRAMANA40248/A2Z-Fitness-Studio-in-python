# A2Z Fitness Studio Management System in Python

class Trainee:
    def __init__(self, name, contact, phone, join_month, payment_details):
        self.name = name
        self.contact = contact
        self.phone = phone
        self.join_month = join_month
        self.payment_details = payment_details
        self.workout_details = []
        self.trainer = None

    def assign_trainer(self, trainer):
        if len(trainer.trainees) < 4:
            self.trainer = trainer
            trainer.add_trainee(self)
        else:
            print(f"Trainer {trainer.name} already has 4 trainees.")

    def add_workout(self, workout):
        self.workout_details.append(workout)

    def view_details(self):
        print(f"Trainee: {self.name}\nContact: {self.contact}\nPhone: {self.phone}")
        print(f"Joining Month: {self.join_month}\nPayment Details: {self.payment_details}")
        if self.trainer:
            print(f"Trainer: {self.trainer.name}")
        print(f"Workout Details: {', '.join(self.workout_details)}")


class Trainer:
    def __init__(self, name, expertise, phone):
        self.name = name
        self.expertise = expertise
        self.phone = phone
        self.trainees = []

    def add_trainee(self, trainee):
        self.trainees.append(trainee)

    def view_trainees(self):
        print(f"Trainer: {self.name}, Expertise: {self.expertise}")
        print("Trainees under this trainer:")
        for trainee in self.trainees:
            print(f"- {trainee.name}")

    def available_slots(self):
        return 4 - len(self.trainees)


class Equipment:
    def __init__(self, name, last_maintenance, status):
        self.name = name
        self.last_maintenance = last_maintenance
        self.status = status

    def update_maintenance(self, date, status):
        self.last_maintenance = date
        self.status = status

    def view_details(self):
        print(f"Equipment: {self.name}\nLast Maintenance: {self.last_maintenance}\nStatus: {self.status}")


class FitnessStudio:
    def __init__(self):
        self.trainees = []
        self.trainers = []
        self.equipment_list = []

    def add_trainee(self, name, contact, phone, join_month, payment_details):
        trainee = Trainee(name, contact, phone, join_month, payment_details)
        self.trainees.append(trainee)

    def add_trainer(self, name, expertise, phone):
        trainer = Trainer(name, expertise, phone)
        self.trainers.append(trainer)

    def add_equipment(self, name, last_maintenance, status):
        equipment = Equipment(name, last_maintenance, status)
        self.equipment_list.append(equipment)

    def assign_trainer_to_trainee(self, trainee_name, trainer_name):
        trainee = next((t for t in self.trainees if t.name == trainee_name), None)
        trainer = next((t for t in self.trainers if t.name == trainer_name), None)
        if trainee and trainer:
            trainee.assign_trainer(trainer)
        else:
            print("Invalid trainee or trainer name.")

    def update_workout_attendance(self, trainee_name, workout):
        trainee = next((t for t in self.trainees if t.name == trainee_name), None)
        if trainee:
            trainee.add_workout(workout)
        else:
            print("Invalid trainee name.")

    def view_trainer_list(self):
        for trainer in self.trainers:
            print(f"Trainer: {trainer.name}, Expertise: {trainer.expertise}, Available Slots: {trainer.available_slots()}")

    def view_trainee_details(self, trainee_name):
        trainee = next((t for t in self.trainees if t.name == trainee_name), None)
        if trainee:
            trainee.view_details()
        else:
            print("Trainee not found.")

    def view_equipment_status(self):
        for equipment in self.equipment_list:
            equipment.view_details()


# Main Program
def main():
    studio = FitnessStudio()

    # Add some sample data
    studio.add_trainer("John", "Weightlifting", "1234567890")
    studio.add_trainer("Jane", "Yoga", "0987654321")
    studio.add_trainer("Mike", "Cardio", "1112223333")

    studio.add_trainee("Alice", "123 Street", "5555555555", "January", "Paid")
    studio.add_trainee("Bob", "456 Avenue", "6666666666", "February", "Pending")

    studio.add_equipment("Treadmill", "2024-01-15", "Good")
    studio.add_equipment("Dumbbells", "2024-02-10", "Under Maintenance")

    while True:
        print("\n--- A2Z Fitness Studio Management ---")
        print("1. View Trainers")
        print("2. Assign Trainer to Trainee")
        print("3. View Trainee Details")
        print("4. Update Workout Attendance")
        print("5. View Equipment Status")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            studio.view_trainer_list()
        elif choice == '2':
            trainee_name = input("Enter Trainee Name: ")
            trainer_name = input("Enter Trainer Name: ")
            studio.assign_trainer_to_trainee(trainee_name, trainer_name)
        elif choice == '3':
            trainee_name = input("Enter Trainee Name: ")
            studio.view_trainee_details(trainee_name)
        elif choice == '4':
            trainee_name = input("Enter Trainee Name: ")
            workout = input("Enter Workout Details: ")
            studio.update_workout_attendance(trainee_name, workout)
        elif choice == '5':
            studio.view_equipment_status()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
