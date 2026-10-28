# Lab 6 — Code and Branch Coverage Analysis

**Student Name:** Akarsh Kumar Gupta  
**SRN:** `PES1UG24AM021`  
**Repository:** https://github.com/SETAPESU26/L6_L7_21_gym_membership  
**Application Under Test:** `gym_membership.py`

## Objective

Measure code (statement/line) coverage and branch coverage for the gym membership application. Tests target membership pricing, entry rules, BMI classification, invalid inputs, threshold conditions, and conditional combinations.

## Test files

- `CodeCoverageTest_xxxx_application.py` — code coverage tests.
- `BranchCoverageTest_xxxx_application.py` — branch-focused tests that exercise both outcomes of decision conditions and relevant boundary cases.

The `xxxx` placeholder follows the naming pattern in the lab instructions. Rename both files to include the required identifier if your instructor expects your SRN or student identifier in place of `xxxx`.

## Results from local execution

### Code coverage

Command:

```bash
coverage run --source=gym_membership -m pytest -q CodeCoverageTest_xxxx_application.py
coverage report -m
```

Observed result: **18 tests passed; 100% statement coverage (35 statements, 0 missed).**

### Branch coverage

Command:

```bash
coverage run --branch --source=gym_membership -m pytest -q BranchCoverageTest_xxxx_application.py
coverage report -m
```

Observed result: **23 tests passed; 100% combined coverage, with 35 statements, 26 branches, 0 missed statements, and 0 partially covered branches.**

## Analysis

The code coverage tests execute all measured statements in `gym_membership.py`, including validation errors for unsupported plans, under-age membership, and invalid BMI height. They test all BMI result categories and gym-entry restrictions.

The branch coverage tests explicitly exercise the true and false outcomes of plan validation, minimum age, senior/student discount selection, trainer add-on and yearly-plan adjustment, inactive membership, opening-hour boundaries, women-only entry, and BMI category thresholds. The report shows zero partial branches in the local run.

## Evidence

Include these terminal-output files/screenshots in the repository:

- `code_coverage_terminal.txt` — raw output from the passing code-coverage run.
- `branch_coverage_terminal.txt` — raw output from the passing branch-coverage run.
- `code_coverage_screenshot.png` — screenshot of terminal showing at least 90% code coverage.
- `branch_coverage_screenshot.png` — screenshot of terminal showing at least 90% branch coverage.

The `.txt` files are captured terminal outputs, not substitutes for the requested screenshots. Run the commands in a terminal and capture screenshots on your machine before final submission.

## Conclusion

The local test runs exceed the lab requirement of at least 90% code coverage and 90% branch coverage. Coverage measures which statements and branches were exercised; it does not by itself prove the absence of defects.
