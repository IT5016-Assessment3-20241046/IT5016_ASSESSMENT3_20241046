class membership:
    def __init__(self):

        ## K.I.S.S
        # I am using KISS to make my code as simple and easier to understand .
        self.members = []
        self.total_member = 0
        self.diploma_count = 0
        self.bachelor_count = 0
        self.withdraw_count = 0

    def register_member(self):

        #Seperation of Corncerns
        #inputs are stored in variable student_id, last_name, programme and strip() is used to remove spaces in the input aswell as lower() is used 
        student_id = input("Enter Student ID: ").strip()
        last_name = input("Enter Last Name: ").strip()
        programme = input("Enter Programme (Diploma/Bachelor): ").strip().lower()

        if not student_id.startswith("W"):
            print(" Only Whitecliffe students can join")
            return

        self.total_member += 1
        membership_id = f"WCSC{self.total_member}"
        #opened/ closed
        #Here i can input new programmes easily in this part without even rewriting the main logic.

        member = {
            "membership_id": membership_id,
            "student_id": student_id,
            "last_name": last_name,
            "programme": programme
        }

        self.members.append(member)

        if programme == "diploma":
            self.diploma_count += 1
        elif programme == "bachelor":
            self.bachelor_count += 1

        print(f"{last_name} has been registered successfully with membership ID: {membership_id}")

        #DRY
        # I have not repeat my code 

    def withdraw_member(self):
        membership_id = input("Enter Membership ID: ").strip()
        last_name = input("Enter Last Name: ").strip()

        for member in self.members:
            if member["membership_id"] == membership_id and member["last_name"] == last_name:
                self.members.remove(member)

                #composition > Inheritance
                # Here , instead of subclassing , i have just a simple attribute

                if member["programme"] == "diploma":
                    self.diploma_count -= 1
                elif member["programme"] == "bachelor":
                    self.bachelor_count -= 1
                self.withdraw_count += 1
                print(f" Member {last_name} ({membership_id}) has been withdrawn.")
                return

        print("Error: Member not found.")

    def display_members(self):
        #Clean Code > Clever Code
        # Here i have keep my code straightforward and clean  do not tried to twist it more complex.

        if not self.members:
            print(" No members currently registered.")
        else:
            print("\n--- Registered Members ---")
            for member in self.members:
                print(f"ID: {member['membership_id']} | Student ID: {member['student_id']} | "
                    f"Name: {member['last_name']} | Programme: {member['programme'].capitalize()}")

        print("\n--- Club Statistics ---")
        print(f"Total Members: {self.total_member}")
        print(f"Diploma Students: {self.diploma_count}")
        print(f"Bachelor Students: {self.bachelor_count}")
        print(f"Withdrawn Members: {self.withdraw_count}")

    def show_member_details(self):

        # Yagni 
        # In this i avoids unnecessary compleexity , no extra features is added.

        membership_id = input("Enter Membership ID: ").strip()
        for member in self.members:
            if member["membership_id"] == membership_id:
                print("\n--- Member Details ---")
                print(f"Membership ID: {member['membership_id']}")
                print(f"Student ID: {member['student_id']}")
                print(f"Last Name: {member['last_name']}")
                print(f"Programme: {member['programme'].capitalize()}")
                return
        print("No member found with that Membership ID.")

    def main_menu(self):
        #Refactor
        # In this menu ,I have used if-elif to improve and clean up the existing code without changing . 
        while True:
            print("\n  Whitecliffe Students Club ")
            print("1. Register a new member")
            print("2. Withdraw a member")
            print("3. Display all members and statistics")
            print("4. Show specific member details")
            print("5. Quit")

            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                self.register_member()
            elif choice == "2":
                self.withdraw_member()
            elif choice == "3":
                self.display_members()
            elif choice == "4":
                self.show_member_details()
            elif choice == "5":
                print("👋 Exiting the system. Goodbye!")
                break
            else:
                print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    #creating object
    member_system = membership()
    member_system.main_menu()
