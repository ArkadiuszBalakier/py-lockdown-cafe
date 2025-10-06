class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    message = "NotVaccinatedError"
    def __init__(self) -> None:
        super().__init__(self.message)


class OutdatedVaccineError(VaccineError):
    message = "OutdatedVaccineError"
    def __init__(self) -> None:
        super().__init__(self.message)


class NotWearingMaskError(Exception):
    message = "NotWearingMaskError"
    def __init__(self) -> None:
        super().__init__(self.message)