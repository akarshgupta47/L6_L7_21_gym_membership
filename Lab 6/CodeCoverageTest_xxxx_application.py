"""Line/code coverage tests for gym_membership.py.

Run from this directory with:
    coverage run --source=gym_membership -m pytest -q CodeCoverageTest_xxxx_application.py
    coverage report -m
"""
import pytest

from gym_membership import bmi_category, can_enter, membership_cost


@pytest.mark.parametrize(
    "plan,age,is_student,with_trainer,expected",
    [
        ("monthly", 30, False, False, 1500),
        ("quarterly", 20, True, False, 3600),
        ("yearly", 60, True, False, 9000),
        ("monthly", 65, False, True, 3125),
        ("yearly", 35, False, True, 13500),
    ],
)
def test_membership_cost_valid_scenarios(plan, age, is_student, with_trainer, expected):
    assert membership_cost(plan, age, is_student, with_trainer) == expected


def test_membership_cost_unknown_plan_raises():
    with pytest.raises(ValueError, match="unknown plan"):
        membership_cost("weekly", 30, False, False)


def test_membership_cost_age_below_minimum_raises():
    with pytest.raises(ValueError, match="too young"):
        membership_cost("monthly", 13, False, False)


@pytest.mark.parametrize(
    "hour,active,women_only,gender,expected",
    [
        (10, True, False, "M", True),
        (10, False, False, "F", False),
        (4, True, False, "F", False),
        (23, True, False, "M", False),
        (10, True, True, "F", True),
        (10, True, True, "M", False),
    ],
)
def test_can_enter_rules(hour, active, women_only, gender, expected):
    assert can_enter(hour, active, women_only, gender) is expected


@pytest.mark.parametrize(
    "weight,height,expected",
    [
        (45, 1.70, "underweight"),
        (68, 1.70, "normal"),
        (80, 1.70, "overweight"),
        (100, 1.70, "obese"),
    ],
)
def test_bmi_categories(weight, height, expected):
    assert bmi_category(weight, height) == expected


def test_bmi_invalid_height_raises():
    with pytest.raises(ValueError, match="invalid height"):
        bmi_category(70, 0)
