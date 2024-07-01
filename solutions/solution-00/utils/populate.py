""" Populate the database with some data at the start of the application"""

from src.persistence.repository import Repository
from src.models.country import Country

def populate_db(repo: Repository) -> None:
    """Populates the db with a dummy country"""
    from src.models.country import Country

    countries = [
        Country(name="Uruguay", code="UY"),
    ]

    for country in countries:
        repo.save(country)

    print("Memory DB populated with initial data.")

if __name__ == "__main__":
    from src.persistence.repository import MemoryRepository

    repo = MemoryRepository()  # Example of using MemoryRepository, adjust as needed
    populate_db(repo)
