import os
import django

# Set the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lessonabsentees.settings")
django.setup()

# Import your Django models
from base.models import Learner

def delete_all_records():
    # Count the number of records before deletion
    count = Learner.objects.count()
    print(f"Number of records before deletion: {count}")
    
    # Delete all records from the Learner table
    Learner.objects.all().delete()
    
    # Verify the deletion
    new_count = Learner.objects.count()
    print(f"Number of records after deletion: {new_count}")

if __name__ == "__main__":
    delete_all_records()
