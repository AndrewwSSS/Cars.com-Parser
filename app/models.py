import csv
from dataclasses import dataclass


@dataclass
class Car:
    make: str
    model: str
    year: int
    price: int | None
    listing_id: str
    contact: str | None = None

    fields_to_write = [
        "make",
        "model",
        "year",
        "price",
        "contact"
    ]

    @staticmethod
    def write_to_csv(cars: ["Car"], filename: str = "cars.csv") -> None:
        if not filename.endswith(".csv"):
            filename += ".csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(Car.fields_to_write)
            for car in cars:
                csv_writer.writerow(
                    [getattr(car, field) for field in Car.fields_to_write]
                )
