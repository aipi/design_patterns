from abc import ABC, abstractmethod


class LogisticApp(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()

        result = f"LogisticApp: {transport.deliver()}"

        return result


class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass


class Truck(Transport):
    def deliver(self) -> str:
        return "Delivered by earth in a box"


class Ship(Transport):
    def deliver(self) -> str:
        return "Delivered by sea in a container"


class RoadLogistic(LogisticApp):
    def create_transport(self) -> Truck:
        return Truck()


class SeaLogistic(LogisticApp):
    def create_transport(self) -> Ship:
        return Ship()


def client_code(logistic: LogisticApp) -> None:
    print(f"{logistic.plan_delivery()}", end="")


if __name__ == "__main__":
    print("App: Launched with the RoadLogistic.")
    client_code(RoadLogistic())
    print("\n")

    print("App: Launched with the SeaLogistic.")
    client_code(SeaLogistic())
