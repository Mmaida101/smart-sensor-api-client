# -*- coding: utf-8 -*-
"""Example 1

This code demonstrates how to get a list of all the assets for each plant in the organization

Example:
    $ python use_case_1_list_of_assets.py

"""

from smart_sensor_client.smart_sensor_client import SmartSensorClient
from pprint import pprint

DEFAULT_SETTINGS_FILE = 'settings.yaml'


def run_task(settings_file=DEFAULT_SETTINGS_FILE) -> bool:

    # Create the client instance
    client = SmartSensorClient(settings_file=settings_file)

    # Authenticate
    if not client.authenticate():
        print('Authentication FAILED')
        return False

    # Print organization
    print('Organization {}, {}'.format(client.organization_id, client.organization_name))
    print()

    # Get list of plants
    plants = client.get_plant_list()

    # Iterate the plant list and print all assets therein
    for plant in plants:
        print('Plant {}, {}:'.format(plant['plantID'], plant['plantName']))
        print('Assets:')

        # Get list of assets
        assets = client.get_asset_list(organization_id=client.organization_id, plant_id=plant['plantID'])
        if len(assets) == 0:
            print('No assets in this plant')
        else:
            for asset in assets:
                pprint(asset)

        print()

    return True


# Main body
if __name__ == '__main__':

    result = run_task()

    if result is True:
        print('Task SUCCESS')
    else:
        print('Task FAILED')
