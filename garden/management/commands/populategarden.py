
from django.core.management.base import BaseCommand
from ._private import *


class Command(BaseCommand):
    help = 'Populates subjects and lecturers'

    def handle(self, *args, **options):
        add_sup_group()
        self.stdout.write(self.style.SUCCESS("Succesfully added supervidor group"))
        add_supervisor()
        self.stdout.write(self.style.SUCCESS("Succesfully added supervidor"))
        add_locations()
        self.stdout.write(self.style.SUCCESS("Succesfully added locations"))
        add_areas()
        self.stdout.write(self.style.SUCCESS("Succesfully added areas"))
        add_jobs()
        self.stdout.write(self.style.SUCCESS("Succesfully added jobs"))
        add_specializations()
        self.stdout.write(self.style.SUCCESS("Succesfully added specializations"))
        add_tasks()
        self.stdout.write(self.style.SUCCESS("Succesfully added tasks"))
        add_employees()
        self.stdout.write(self.style.SUCCESS("Succesfully added employees"))
        add_emp_task()
        self.stdout.write(self.style.SUCCESS("Succesfully added emp task"))
