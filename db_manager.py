import csv
import statistics
from models.product import Report

def save_weather_statistics(info):
    with open('db/statistics.csv', 'a') as weather_statistics_file:
        header = ['date', 'city', 'current_weather', 'weather_data']

        writer = csv.DictWriter(weather_statistics_file, fieldnames=header)

        if client_statistics_file.tell() == 0:
            writer.writeheader()

        writer.writerow(info)


def load_weather_statistics():
    weather_statistics = []
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
    weather_statistics = load_weather_statistics()
    average_weather = statistics.mean([report.current_weather for report in weather_statistics])
    average_data = statistics.mean([report.weather_data for report in weather_statistics])
    return average_weather, average_data
