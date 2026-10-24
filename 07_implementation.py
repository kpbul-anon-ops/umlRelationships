# Combined example: Enumeration + Interface + Abstract Class
# (Inheritance, Realization and Dependency in one system)
from abc import ABC, abstractmethod
from enum import Enum


class ActivityStatus(Enum):
    PLANNED = 1
    ONGOING = 2
    COMPLETED = 3


class Schedulable:
    def set_schedule(self):
        raise NotImplementedError


class SchoolActivity(ABC):
    def __init__(self, title):
        self.title = title
        self.status = ActivityStatus.PLANNED  # uses the enum as attribute type

    def display_details(self):
        print(self.title, self.status.name)

    @abstractmethod
    def conduct_activity(self):
        pass


class ScienceFair(SchoolActivity, Schedulable):
    def conduct_activity(self):
        print("Conducting science experiments.")

    def set_schedule(self):
        print("Science Fair schedule set.")


if __name__ == "__main__":
    activity = ScienceFair("Science Fair")
    activity.display_details()
    activity.conduct_activity()
    activity.set_schedule()
