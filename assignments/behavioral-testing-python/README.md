# 📘 Assignment: Behavioral Testing with Pytest

## 🎯 Objective

Write behavioral tests for a small task-list program using `pytest`. You will describe what users should observe, test normal and edge-case behavior, and use failing tests to find and fix a defect.

## 📝 Tasks

### 🛠️ Describe Task Behavior

#### Description

Read `starter-code.py` and identify the behavior a user should observe when adding tasks and completing tasks. Create `test_tasks.py` with tests that describe those expectations.

#### Requirements

Completed program should:

- install or use `pytest` and run tests from the assignment folder
- test that a new task contains its title, priority, and an incomplete status
- test that completing a task changes its status to complete
- test that completing an unknown task reports that no task was changed
- use clear test names that describe behavior rather than implementation details

### 🛠️ Test Filters and Edge Cases

#### Description

Add tests for `list_tasks`. A user should be able to request all tasks, only completed tasks, or only incomplete tasks. Include an edge case that checks the result when no tasks match the requested status.

#### Requirements

Completed program should:

- verify that listing without a status returns every task
- verify that `completed=True` returns only completed tasks
- verify that `completed=False` returns only incomplete tasks
- verify that a filter with no matches returns an empty list
- keep each test independent by creating its own task data

### 🛠️ Use Failures to Improve the Code

#### Description

Run the full test suite and read the failure output. Locate the defect in `starter-code.py`, explain which expected behavior it violates, and correct the implementation without changing the public function names or parameters.

#### Requirements

Completed program should:

- pass all of the behavioral tests after the fix
- preserve the behavior covered by the earlier tests
- avoid changing tests merely to hide a failure
- include a short comment or commit message explaining the defect that was fixed

### 🛠️ Add a Boundary Test

#### Description

Add one additional test for a boundary or invalid input, such as an empty task title or an invalid task ID. Decide what predictable behavior the function should provide, then implement that behavior and test it.

#### Requirements

Completed program should:

- include at least one test for an input outside the normal path
- state the expected result clearly in the test
- make the implementation and test agree on a predictable outcome
- finish with a complete passing test run
