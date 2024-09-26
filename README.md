# Python UI Automation Framework

This repository contains a UI automation framework built with Python. It provides tests using both Selenium and Playwright to compare automation tools for UI testing. The framework follows best practices such as the **Page Object Model (POM)** and the **Screenplay Pattern**.

## Table of Contents
- [Python UI Automation Framework](#python-ui-automation-framework)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Setup Instructions](#setup-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
    - [3. Install Dependencies](#3-install-dependencies)
    - [4. Install Playwright Browsers](#4-install-playwright-browsers)
  - [Running Tests](#running-tests)
    - [1. Run All Playwright Tests](#1-run-all-playwright-tests)
    - [2. Run All Selenium Tests](#2-run-all-selenium-tests)
    - [3. Running Specific Tests](#3-running-specific-tests)
    - [Generating Reports](#generating-reports)
  - [Directory Structure](#directory-structure)

## Features

- **Cross-browser testing** using Selenium and Playwright.
- **Page Object Model (POM)** and **Screenplay Pattern** design patterns for test structure.
- **Allure** reporting integration for detailed test reports.
- Tests for login functionality on [The Movie Database (TMDb)](https://www.themoviedb.org/).

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/python-ui-automation.git
cd python-ui-automation
```

### 2. Create a Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # For Mac/Linux
# For Windows, use: .venv\Scripts\activate
```

### 3. Install Dependencies
Install all necessary packages using pip:
```bash
pip install -r requirements.txt
```

### 4. Install Playwright Browsers
To use Playwright, install the required browsers:
```bash
playwright install
```

## Running Tests
### 1. Run All Playwright Tests
To run all Playwright tests:
```bash
pytest --alluredir=allure-results playwright_module/tests/
```
### 2. Run All Selenium Tests
To run all Selenium tests:
```bash
pytest --alluredir=allure-results selenium_module/tests/
```
### 3. Running Specific Tests
You can run specific test files. For example, to run a Playwright POM test:
```bash
pytest --alluredir=allure-results playwright_module/tests/test_login_pom_playwright.py
```
Or to run a Selenium Screenplay test:
```bash
pytest --alluredir=allure-results selenium_module/tests/test_login_screenplay_selenium.py
```
### Generating Reports
After running the tests, you can generate and view the Allure report using:
```bash
allure serve allure-results
```
This will open the Allure report in your default web browser.

## Directory Structure
```plaintext
.
├── playwright_module/
│   ├── pages/                    # Page Object Model for Playwright
│   ├── screenplay/               # Screenplay pattern for Playwright
│   ├── tests/                    # Playwright test cases
│   └── utils/                    # Playwright utilities (e.g., driver setup, Allure integration)
├── selenium_module/
│   ├── pages/                    # Page Object Model for Selenium
│   ├── screenplay/               # Screenplay pattern for Selenium
│   ├── tests/                    # Selenium test cases
│   └── utils/                    # Selenium utilities (e.g., WebDriver setup, Allure integration)
├── .gitignore                    # Files and directories to ignore in Git
├── pytest.ini                    # pytest configuration file
├── requirements.txt              # List of dependencies
└── README.md                     # Project documentation
```