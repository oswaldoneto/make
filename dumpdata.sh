#!/bin/sh

echo "Dumping data from Make database..."
python manage.py dumpdata --indent=4 campaign.Campaign > campaign/fixtures/campaign.json
python manage.py dumpdata --indent=4 campaign.Challenge > campaign/fixtures/challenge.json
