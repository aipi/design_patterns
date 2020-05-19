from abc import ABC, abstractmethod


class AbstractChair(ABC):
    @abstractmethod
    def create_product(self) -> str:
        pass


class VictorianChair(AbstractChair):
    def create_product(self) -> str:
        return "The result of the product VictorianChair"


class ModernChair(AbstractChair):
    def create_product(self) -> str:
        return "The result of the product ModernChair"


class AbstractTable(ABC):
    @abstractmethod
    def create_product(self) -> None:
        pass

    @abstractmethod
    def create_collaborating_product(self, product: AbstractChair) -> None:
        pass


class VictorianTable(AbstractTable):
    def create_product(self) -> str:
        return "The result of the product VictorianTable"

    def create_collaborating_product(
        self,
        collaborating: AbstractChair
    ) -> str:
        result = collaborating.create_product()
        return (
            f"The result of the VictorianTable collaborating with the "
            f"({result})"
        )


class ModernTable(AbstractTable):
    def create_product(self) -> str:
        return "The result of the product ModernTable"

    def create_collaborating_product(self, collaborating: AbstractChair):
        result = collaborating.create_product()
        return (
            f"The result of the ModernTable collaborating with the "
            f"({result})"
        )


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> VictorianChair:
        return VictorianChair()

    def create_table(self) -> VictorianTable:
        return VictorianTable()


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> ModernChair:
        return ModernChair()

    def create_table(self) -> ModernTable:
        return ModernTable()


def client_code(factory: FurnitureFactory) -> None:
    product_a = factory.create_chair()
    product_b = factory.create_table()

    print(f"{product_b.create_product()}")
    print(f"{product_b.create_collaborating_product(product_a)}", end="\n")


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(VictorianFurnitureFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ModernFurnitureFactory())
