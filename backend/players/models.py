from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.conf import settings
from django.utils.timezone import now
import csv
import os


class Player(models.Model):
    number = models.IntegerField()
    firstName = models.CharField(max_length=255, null=False)
    lastName = models.CharField(max_length=255, null=False)
    pos = models.CharField(max_length=2)
    bat = models.CharField(max_length=1)
    thw = models.CharField(max_length=1)
    age = models.IntegerField()
    ht = models.CharField(max_length=255)
    wt = models.CharField(max_length=255)
    birthPlace = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=now, editable=False)

    @property
    def full_name(self):
        return f"{self.firstName} {self.lastName}"


# Create players based on records that we have
@receiver(post_migrate)
def populate_subjects(sender, **kwargs):
    if sender.name == 'players':
        root_path = os.path.join(settings.MEDIA_ROOT, 'records/players')
        csv_files = [f for f in os.listdir(root_path) if f.endswith('.csv')]
        added_players = 0
        existing_players = 0
        print('--- Adding Players ---')
        for csv_file in csv_files:
            csv_file_path = os.path.join(root_path, csv_file)
            filename = os.path.splitext(csv_file)[0]
            print('Reading records from', filename)
            with open(csv_file_path, newline='') as csvfile:

                reader = csv.reader(csvfile)
                next(reader)  # Skip the header row
                for row in reader:
                    PLAYER, CREATED = Player.objects.get_or_create(
                        number=int(row[0]),
                        firstName=row[1],
                        lastName=row[2],
                        pos=row[3],
                        bat=row[4],
                        thw=row[5],
                        age=int(row[6]),
                        ht=row[7],
                        wt=row[8],
                        birthPlace=row[9])
                    if (CREATED):
                        added_players += 1
                    else:
                        existing_players += 1
                print('Skipped', existing_players, 'players')
                print('Added', added_players, 'players')
