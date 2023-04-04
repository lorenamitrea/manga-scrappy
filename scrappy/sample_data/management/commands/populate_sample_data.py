import os
import csv
from django.core.management.base import BaseCommand
from sample_data.models import Artist
from django.db.utils import DataError
from datetime import timedelta, datetime


class Command(BaseCommand):
    help = 'Populates the table Artist with values from artist-data'

    def handle(self, *args, **kwargs):
        with open(os.path.join(os.path.abspath(os.curdir), 'data', 'artist-data.csv'), 'r') as csvfile:
            artist_data = csv.DictReader(csvfile)
            for row in artist_data:
                if ', ' not in row['name'] or not row['gender'] or not row['yearOfBirth']:
                    continue
                last_name, first_name = row['name'].split(', ', 1)
                try:
                    Artist.objects.create(first_name=first_name,
                                          last_name=last_name,
                                          gender=row['gender'],
                                          born_year=int(row['yearOfBirth']),
                                          death_year=int(row['yearOfDeath']) if row['yearOfDeath'] else None)
                except DataError:
                    continue
