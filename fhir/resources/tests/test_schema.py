from .. import fhirtypes  # noqa: F401
from ..patient import Patient


def test_schema_of_type_matches():
    assert Patient.schema() == fhirtypes.PatientType.schema()


def test_schema_of_type_matches():
    assert Patient.schema()["properties"].keys() == []
