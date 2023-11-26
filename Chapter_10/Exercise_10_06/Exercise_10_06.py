"""
6. Patient Charges
Write a class named Patient that has attributes for the following data:
• First name, middle name, and last name
• Address, city, state, and ZIP code
• Phone number
• Name and phone number of emergency contact
The Patient class’s _ _init_ _ method should accept an argument for each attribute. The
Patient class should also have accessor and mutator methods for each attribute.
Next, write a class named Procedure that represents a medical procedure that has been
performed on a patient. The Procedure class should have attributes for the following data:
• Name of the procedure
• Date of the procedure
• Name of the practitioner who performed the procedure
• Charges for the procedure
The Procedure class’s _ _init_ _ method should accept an argument for each attribute.
The Procedure class should also have accessor and mutator methods for each attribute.
Next, write a program that creates an instance of the Patient class, initialized with sample
data. Then, create three instances of the Procedure class, initialized with the following data:
Procedure #1: Procedure #2: Procedure #3:
Procedure name: Physical Exam
Date: Today’s date
Practitioner: Dr. Irvine
Charge: 250.00
Procedure name: X-ray
Date: Today’s date
Practitioner: Dr. Jamison
Charge: 500.00
Procedure name: Blood test
Date: Today’s date
Practitioner: Dr. Smith
Charge: 200.00
The program should display the patient’s information, information about all three of the
procedures, and the total charges of the three procedures.


@author Sharaf Qeshta
"""


class Patient:
    def __init__(self, first_name, middle_name, last_name,
                 address, city, state, zip, phone_number,
                 emergency_contact_name, emergency_contact_phone_number):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip = zip
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone_number = emergency_contact_phone_number

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip(self, zip):
        self.__zip = zip

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_emergency_contact_name(self, name):
        self.__emergency_contact_name = name

    def set_emergency_contact_phone_number(self, phone_number):
        self.__emergency_contact_phone_number = phone_number

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip(self):
        return self.__zip

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone_number(self):
        return self.__emergency_contact_phone_number


class Procedure:
    def __init__(self, name, date, practitioner, charges):
        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges

    def set_name(self, name):
        self.__name = name

    def set_date(self, date):
        self.__date = date

    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    def set_charges(self, charges):
        self.__charges = charges

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_practitioner(self):
        return self.__practitioner

    def get_charges(self):
        return self.__charges


def main():
    patient = Patient("Sharaf", "Awad", "Keshta"
                      , "Houston, TX", "Houston", "Texas",
                      "77034", "878 789 7895", "Ali Ali",
                      "892 952 5652")
    procedure1 = Procedure("Physical Exam", "11/24/2023", "Dr. Irvine", 250.00)
    procedure2 = Procedure("X-ray", "11/24/2023", "Dr. Jamison", 500.00)
    procedure3 = Procedure("Blood test", "11/24/2023", "Dr. Smith", 200.00)

    print(
        f"First Name: {patient.get_first_name()}, Middle Name: {patient.get_middle_name()}, Last Name: {patient.get_last_name()} etc..")
    print(f"total charges: {procedure1.get_charges() + procedure2.get_charges() + procedure3.get_charges()}")


main()
