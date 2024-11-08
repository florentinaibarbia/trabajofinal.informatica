import csv
import statistics
from models.product import Report

def save_client_statistics(info):
    with open('db/statistics.csv', 'a') as client_statistics_file:
        header = ['date', 'city', 'current_weather', 'weather_data']

        writer = csv.DictWriter(client_statistics_file, fieldnames=header)

        if client_statistics_file.tell() == 0:
            writer.writeheader()

        writer.writerow(info)


def load_client_statistics():
    client_statistics = []
    with open('db/statistics.csv', 'r') as statistics_file:
        rows = csv.DictReader(statistics_file)

        for row in rows:
            client_statistics.append(
                Report(
                    row['date'],
                    row['city'],
                    row['current_weather'],
                    row['weather_data']
                )
            )
        return client_statistics

def statistics_average():
    client_statistics = load_client_statistics()
    average_weather = statistics.mean([report.current_weather for report in client_statistics])
    average_data = statistics.mean([report.weather_data for report in client_statistics])
    return average_weather, average_data