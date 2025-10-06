from typing import Any

from app.cafe import Cafe
from app.errors import NotVaccinatedError, OutdatedVaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict[str, Any]], cafe: Cafe,) -> str:
    mask_to_buy = 0
    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except (NotVaccinatedError, OutdatedVaccineError):
            raise "All friends should be vaccinated"
        except NotWearingMaskError:
            mask_to_buy += 1
        else:
            return f"Friends can go to {cafe.name}"
    
    if mask_to_buy > 0:
        return f"Friends should buy {mask_to_buy} masks"
