# API Test Automation Exercise

## Overview

### Brief description of the solution:
This project uses Python + pytest to test the JSONPlaceholder API. Tests are organized by endpoint/resource and use fixture-driven request/expected data for deterministic assertions. A shared helper module centralizes fixture loading and response validation logic.

### Assumptions made:
1. JSONPlaceholder responses are static and always return the same result given the same request data
2. No special authentication is required to make these API requests
3. User will run these tests via the command line

### Scope of testing completed:
1. Happy path scenarios for all endpoints (i.e. one basic GET, POST, PUT, PATCH, DELETE) for each of posts/, todos/, etc.
2. 2 negative and edge-case tests per endpoint (e.g. missing payload, null values, long strings, special characters, non-existent routes, non-existence of ids).
3. Assertions check for status code, response headers, and response body content.

## Execution Instructions

Ensure you have the latest version of python installed - this project was created with Python 3.14.6.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Execute the test suite:

```bash
python -m pytest --html-report.html
```

### 2 ways to view test results:
1. Console output
   <img width="1124" height="238" alt="image" src="https://github.com/user-attachments/assets/1a904f91-864b-4eb0-bba7-1cbff08a2b73" />

3. Visual HTML report - Upon running above command, a `report.html` file will be generated at the root level. Open this file in any browser to view a comprehensive report.

> **Note:** You may have to open your computer's file explorer and manually look for the file for it to load properly. If you drag `report.html` directly into a browser, it may open as a blank screen.


   <img width="1912" height="908" alt="image" src="https://github.com/user-attachments/assets/d5001109-b632-4dd2-a041-3b3ad309fa98" />

## Coverage Summary

### Routes/resources tested:
All endpoints (`/posts`, `/comments`, `/albums`, `/photos`, `/todos`, `/users`)
- Happy paths, negative scenarios, edge cases for each
- GET, POST, PUT, PATCH, DELETE for each

### Types of validations implemented:
1. Return status code check
2. Verify header's content-type
3. Validated exact match for JSON response body

### Areas intentionally omitted due to time constraints:
1. Wider test coverage (e.g. more negative and edge cases)
2. Performance and load testing
3. CI/CD pipeline integration
