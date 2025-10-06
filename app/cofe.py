from datetime import date

from app.errors import NotVaccinatedError, NotWearingMaskError, OutdatedVaccineError


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        current_date = date.today()
        if not "vaccine" in visitor:
            raise NotVaccinatedError
        if visitor["vaccine"] < current_date:
            raise OutdatedVaccineError
        if not visitor["wearing_a_mask"]:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"