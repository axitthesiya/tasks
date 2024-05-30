
# Class for MedicalStaff with attributes name, staff_id, and patients list
class MedicalStaff:
    def __init__(self, name, staff_id):
        self.name = name  # Name of the medical staff member
        self.staff_id = staff_id  # ID of the medical staff member
        self.patients = []  # List of patients assigned to the medical staff member

# Method to assign a patient to the medical staff member
    def assign_patient(self, patient):
        self.patients.append(patient)  # Add patient to the list of patients

# Method to display the schedule of the medical staff member
    def display_schedule(self):
        print(f"Schedule for {self.name}:")
        for patient in self.patients:
            print(f"Patient: {patient.name}, Procedure: {patient.procedure}")

# Class for Patient with attributes name, patient_id, and procedure
class Patient:
    def __init__(self, name, patient_id, procedure):
        self.name = name  # Name of the patient
        self.patient_id = patient_id  # ID of the patient
        self.procedure = procedure  # Procedure assigned to the patiet

# Class for Doctor, a type of MedicalStaff, with a method to perform a medical procedure
class Doctor(MedicalStaff):
    # Method to perform a medical procedure on a patient
    def perform_procedure(self, patient):
        patient1.procedure = "Medical Procedure"  # Update the patient's procedure
        self.assign_patient(patient)  # Assign the patient to the doctor

# Class for Nurse, a type of MedicalStaff, with a method to perform a Nursing Care or Checkup
class Nurse(MedicalStaff):
    # Method to perform a Nursing Care or Checkup on a patient
    def perform_procedure(self, patient):
        patient.procedure = "Nursing Care or Checkup"  # Update the patient's
        self.assign_patient(patient) 

# Class for Sergeon, a type of Medicalstaff, with a method to perform a operation
class Surgeon(MedicalStaff):
    # Method to perform a operation on a patient
    def perform_procedure(self, patient):
        patient.procedure = "Operation"
        self.assign_patient(patient)

        
# Instantiate medical staff members obj
doctor = Doctor("Dr. Smith", "D001")
nurse = Nurse("Nurse aliya", "N001")
surgeon = Surgeon("Dr. Patel", "S001")

# Instantiate patients obj
patient1 = Patient("Jake", "P001", "investigates ")
patient2 = Patient("Oggay", "P002", "enquires about")
patient3 = Patient("Pandey", "P003", "Patient reports")

# Assign patients to medical staff members
doctor.perform_procedure(patient1)
nurse.perform_procedure(patient2)
surgeon.perform_procedure(patient3)

# Display all registered medical staff members and their assigned patients
print("Registered Medical Staff:")
print()

print(doctor.name + ":")
doctor.display_schedule()
print()  

print(nurse.name + ":")
nurse.display_schedule()
print()

print(surgeon.name + ":")
surgeon.display_schedule()
print()