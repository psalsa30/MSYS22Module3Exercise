#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from MyInventoryApp.models import Supplier
from datetime import datetime


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyInventorySystem.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)




if __name__ == '__main__':
    main()


Supplier.objects.create(
    name="Meister, Inc.",
    city="Dresden",
    country="Germany",
    created_at=datetime.strptime("01/20/2019 08:20AM", "%m/%d/%Y %I:%M%p")
)


Supplier.objects.create(
    name="Sailfish, Inc.",
    city="Racoon City",
    country="Canada",
    created_at=datetime.strptime("03/14/2019 08:21AM", "%m/%d/%Y %I:%M%p")
)


Supplier.objects.create(
    name="Bucky, Inc.",
    city="California",
    country="USA",
    created_at=datetime.strptime("12/01/2018 08:22AM", "%m/%d/%Y %I:%M%p")
)


#Ray's supplier choice
Supplier.objects.create(
    name="Nestlé Waters, Inc.",
    city="Stamford",
    country="USA",
    created_at=datetime.strptime("04/10/2020 09:30AM", "%m/%d/%Y %I:%M%p")
)



