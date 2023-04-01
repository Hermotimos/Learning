from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


"""
COMPOSITION vs INHERITANCE
--------------------------
Source: https://www.youtube.com/watch?v=0mcP8ZpUR38

"The gang of four" recommends Composition over Inheritance whenever possible.
    * Inheritance: hierarchy of classes ('is'-relationship)
    * Composition: separate classes that use each other ('has'-relationship)


WATCH: https://www.youtube.com/watch?v=0mcP8ZpUR38

--> use abstract base classes to create interfaces
    and then inherit from them to create concrete classes
    (this reduces coupling, whereas inheritance from concrete superclasses increases it)

"""





"""
[1]

This is the first stage of the code, with a lot of code repetition
and mixed responsibilities.

"""

@dataclass
class HourlyEmployee:
    """Employee that's paid based on number of worked hours."""
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )


@dataclass
class SalariedEmployee:
    """Employee that's paid based on a fixed monthly salary."""
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        return (
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )


@dataclass
class Freelancer:
    """Freelancer that's paid based on number of worked hours."""
    name: str
    id: int
    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return (
            self.pay_rate * self.hours_worked + self.commission * self.contracts_landed
        )


def main1() -> None:
    print()

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}.")

    sarah = SalariedEmployee(name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10)
    print(f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}.")


main1()






"""
[2]

This is the effect achieved with Inheritance.
The problem is that whenever we want to extend the program,
ex. by adding another type of payment modality like yearly bonus,
we get a cascade of new classes and inheritance tree explodes.

Adding bonus modality to a program designed as below with Inheritance, requires:
    HourlyEmployeeWithYearlyBonus(HourlyEmployee)
    SalariedEmployeeWithYearlyBonus(SalariedEmployee)
    FreelancerWithYearlyBonus(Freelancer)

    And even worse, because...
    * HourlyEmployeeWithYearlyBonusWithCommission etc.

So in this example pure inheritance doesn't solve the problem of code repetition.

"""

@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""
    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""
    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""
    monthly_salary: float
    percentage: float = 1

    def compute_pay(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""
    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        return self.pay_rate * self.hours_worked


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on a fixed monthly salary and that gets a commission."""
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class HourlyEmployeeWithCommission(HourlyEmployee):
    """Employee that's paid based on number of worked hours and that gets a commission."""
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that's paid based on number of worked hours and that gets a commission."""
    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        return super().compute_pay() + self.commission * self.contracts_landed


def main2() -> None:
    print()

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}.")

    sarah = SalariedEmployeeWithCommission(name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10)
    print(f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}.")


main2()







"""
[3]

With Composition + Inheritance (inheritance used only for creating interfaces,
i.e. abstract base classes with purely abstract methods),
we get a program that is easily extendable.

"""

class Contract(ABC):
    """Represents a contract and a payment process for a particular employeee."""

    @abstractmethod
    def get_payment(self) -> float:
        """Compute how much to pay an employee under this contract."""


@dataclass
class HourlyContract(Contract):
    """Contract type for an employee being paid on an hourly basis."""
    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""
    monthly_salary: float
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """Contract type for a freelancer (paid on an hourly basis)."""
    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


# ------------------------------------


@dataclass
class Commission(ABC):
    """Represents a commission payment process."""

    @abstractmethod
    def get_payment(self) -> float:
        """Returns the commission to be paid out."""


@dataclass
class ContractCommission(Commission):
    """Represents a commission payment process based on the number of contracts landed."""
    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        """Returns the commission to be paid out."""
        return self.commission * self.contracts_landed


# ------------------------------------


@dataclass
class Employee:
    """Basic representation of an employee at the company."""
    name: str
    id: int
    contract: Contract                              # <--- composition here !
    commission: Optional[Commission] = None         # <--- composition here !

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout


# ------------------------------------


def main3() -> None:
    print()

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours "
        f"and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission)
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts "
        f"and earned ${sarah.compute_pay()}."
    )


main3()
