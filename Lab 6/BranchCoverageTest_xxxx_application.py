"""Decision/branch coverage tests for gym_membership.py.

Run from this directory with:
    coverage run --branch --source=gym_membership -m pytest -q BranchCoverageTest_xxxx_application.py
    coverage report -m
"""
import pytest

from gym_membership import bmi_category, can_enter, membership_cost


@pytest.mark.parametrize(
    "plan,age,student,trainer,expected",
    [
        ("invalid", 30, False, False, None),  # invalid-plan exception branch
        ("monthly", 13, False, False, None),  # minimum-age exception branch
        ("monthly", 14, False, False, 1500),  # age and student false; trainer false
        ("monthly", 25, True, False, 1350),  # student discount
        ("quarterly", 59, True, False, 3600),  # student path immediately below age threshold
        ("monthly", 60, True, False, 1125),  # senior discount takes precedence over student discount
        ("monthly", 30, False, True, 3500),  # trainer add-on; non-yearly plan
        ("yearly", 30, False, True, 13500),  # yearly trainer adjustment true
        ("yearly", 30, True, True, 12300),  # yearly trainer adjustment with student discount
    ],
)
def test_membership_cost_branches(plan, age, student, trainer, expected):
    if plan == "invalid":
        with pytest.raises(ValueError, match="unknown plan"):
            membership_cost(plan, age, student, trainer)
    elif age < 14:
        with pytest.raises(ValueError, match="too young"):
            membership_cost(plan, age, student, trainer)
    else:
        assert membership_cost(plan, age, student, trainer) == expected


@pytest.mark.parametrize(
    "hour,active,women_only,gender,expected",
    [
        (10, False, False, "M", False),  # inactive plan short-circuit
        (4, True, False, "F", False),  # too early
        (5, True, False, "M", True),  # lower boundary included
        (22, True, False, "F", True),  # upper boundary included
        (23, True, False, "M", False),  # too late
        (10, True, True, "F", True),  # women-only slot and matching gender
        (10, True, True, "M", False),  # women-only slot and nonmatching gender
        (10, True, False, "X", True),  # normal slot allows any gender string
    ],
)
def test_can_enter_each_decision(hour, active, women_only, gender, expected):
    assert can_enter(hour, active, women_only, gender) is expected


@pytest.mark.parametrize(
    "weight,height,expected",
    [
        (50, 1.70, "underweight"),  # BMI below 18.5
        (53.465, 1.70, "normal"),  # near 18.5 threshold
        (72.25, 1.70, "overweight"),  # BMI 25.0 boundary is overweight
        (80, 1.70, "overweight"),  # BMI between 25 and 30
        (86.7, 1.70, "obese"),  # BMI at/above 30
    ],
)
def test_bmi_decision_branches(weight, height, expected):
    assert bmi_category(weight, height) == expected


def test_bmi_invalid_height_branch():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, -1)
