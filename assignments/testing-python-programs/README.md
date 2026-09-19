# 📘 Assignment: Testing Python Programs

## 🎯 Objective

Learn how to use `pytest` to verify Python behavior, catch edge cases, and prevent regressions. You will write tests for ordinary functions and FastAPI endpoints using clear, repeatable assertions.

## 📝 Tasks

### 🛠️ Write Your First Unit Tests

#### Description

Download the starter code and create a file named `test_starter_code.py`. Begin by testing the `find_book()` and `format_book()` functions with the sample catalog.

Run your tests with `pytest` and use the failure output to improve any incorrect assumptions in your tests or the starter code.

#### Requirements

Completed test program should:

- Use `pytest` test functions whose names begin with `test_`
- Verify that `find_book()` returns the correct book for an existing ID
- Verify that `find_book()` returns `None` for an unknown ID
- Verify that `format_book()` includes the book title and author in the expected format
- Pass when run with `pytest`


### 🛠️ Test Edge Cases and Validation

#### Description

Expand the test suite to check behavior at the boundaries. Use parametrized tests where several inputs should produce the same kind of result.

#### Requirements

Completed test program should:

- Test an empty book title and an empty author name
- Test that `add_book()` assigns a new unique integer ID
- Test that adding a book does not remove existing books
- Use at least one `@pytest.mark.parametrize` test for multiple inputs
- Keep tests independent so one test does not depend on another test's mutations


### 🛠️ Test FastAPI Endpoints

#### Description

Use FastAPI's `TestClient` to test the `/books` API without starting a separate server. Add tests for successful requests, invalid request data, and a missing book.

Install the dependencies with `pip install fastapi httpx pytest`, then run the complete suite with `pytest`.

#### Requirements

Completed test program should:

- Create a `TestClient` for the starter application's `app`
- Test that `GET /books` returns HTTP 200 and a JSON list
- Test that `POST /books` returns HTTP 201 and includes the submitted title and author
- Test that invalid book data returns a 422 validation response
- Test that `GET /books/9999` returns HTTP 404
- Use assertions for both response status codes and important response data


### 🛠️ Stretch: Protect Against Regressions

#### Description

Review the test suite as a team and identify a behavior that could accidentally break during a future change. Write a focused regression test that documents that behavior.

#### Requirements

Completed test program should:

- Add at least one regression test with a descriptive name
- Explain in a short comment or docstring which behavior the test protects
- Run the full test suite successfully with one `pytest` command
