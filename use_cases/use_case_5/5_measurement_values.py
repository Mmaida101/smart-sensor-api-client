# -*- coding: utf-8 -*-
"""Example 5

This code prints out some measurement values for a particular asset

Example:
    $ python 5_measurement_values.py

"""

from smart_sensor_client.smart_sensor_client import SmartSensorClient
from datetime import datetime
import matplotlib.pyplot as plt

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

    # Ask users for their input:
    print('Please enter your query parameters:')
    asset_id = input('Asset ID: ')

    possible_measurement_types = client.get_measurement_types(asset_id=asset_id)
    print(possible_measurement_types)
    measurement_type = input('Measurement type (find measurementTypeID in list above): ')
    start_date = input('Start date (YYYY-MM-DD): ')
    end_date = input('End date (YYYY-MM-DD): ')

    # Get the measurement data during this time
    values = client.get_measurement_value(asset_id=asset_id,
                                          measurement_type=measurement_type,
                                          start_time=start_date,
                                          end_time=end_date)

    values_to_plot = [[datetime.strptime(v['measurementCreated'], '%Y-%m-%dT%H:%M:%S'), float(v['measurementValue'])]
                      for v in values[0]['measurements']
                      ]
    values_to_plot.sort(key=lambda v: v[0])

    measurement_timestamp = [v[0] for v in values_to_plot]
    measurement_values = [v[1] for v in values_to_plot]
    plt.plot(measurement_timestamp, measurement_values)
    plt.show()

    return True


# Main body
if __name__ == '__main__':

    result = run_task()

    if result is True:
        print('Task SUCCESS')
    else:
        print('Task FAILED')
