import datetime
import time

def medication_reminder(medication_name, dosage, interval):
    while True:
        # Get the current time
        current_time = datetime.datetime.now().time()
        
        # Display the reminder message
        print(f"It's time to take your {medication_name}. Dosage: {dosage}")
        
        # Wait for the specified interval
        time.sleep(interval)

# Example usage
medication_name = "Aspirin"
dosage = "1 tablet"
interval = 3600  # 1 hour in seconds

medication_reminder(medication_name, dosage, interval)