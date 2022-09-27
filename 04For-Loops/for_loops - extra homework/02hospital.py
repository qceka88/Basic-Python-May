days = int(input())
doctors = 7
patients = 0
total_healed = 0
total_unhealed = 0
for i in range(1, days + 1):
    patients = int(input())
    if i % 3 == 0  and total_unhealed > total_healed:
        doctors = doctors + 1
    if doctors >= patients:
        total_healed = total_healed + patients
    else:
        total_healed = total_healed + doctors
        unhealed_patients = patients - doctors
        total_unhealed = total_unhealed + unhealed_patients

print(f"Treated patients: {total_healed}.")
print(f"Untreated patients: {total_unhealed}.")
