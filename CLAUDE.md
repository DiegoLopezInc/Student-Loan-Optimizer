# CLAUDE.md - AI Assistant Guide for Student Loan Optimizer

## Project Overview

**Student Loan Optimizer** is a Python-based application designed to help users manage and optimize their student loan debt. The project provides tools for:
- Extracting loan information from loan provider websites via web scraping
- Analyzing loan data and projecting future payments
- Calculating and comparing refinancing options
- Visualizing loan data through an interactive Streamlit interface

**Tech Stack:**
- Python 3.x
- Beautiful Soup 4 (web scraping)
- Streamlit (UI)
- Matplotlib (visualization)
- Pandas (data manipulation)
- NumPy (numerical computations)
- unittest (testing framework)

**License:** GNU General Public License v3.0

---

## Repository Structure

```
Student-Loan-Optimizer/
├── src/                          # Main source code
│   ├── __init__.py              # Package initializer
│   ├── loanClass.py             # Core Loan data model
│   ├── loan_scraper.py          # Web scraping functionality (production-ready)
│   ├── loanWebsiteExtractor.py  # Template for custom loan scraping (TODOs)
│   ├── loan_analyzer.py         # Payment analysis and graphing
│   ├── refinance_calculator.py  # Refinancing calculations
│   └── dataDisplay.py           # Streamlit UI application
│
├── tests/                        # Unit tests
│   ├── __init__.py              # Test package initializer
│   ├── test_loanClass.py        # Tests for Loan class
│   ├── test_loan_scraper.py     # Tests for web scraping
│   ├── test_loan_analyzer.py    # Tests for loan analysis
│   └── test_refinance_calculator.py  # Tests for refinancing calculator
│
├── custom_data_structure/        # C extension module (optional)
│   ├── customDataStructure.c    # C implementation
│   └── setup.py                 # Build configuration for C extension
│
├── requirements.txt              # Python dependencies
├── README.md                     # User-facing documentation
├── LICENSE                       # GNU GPL v3.0
└── .gitignore                   # Git ignore patterns

```

---

## Core Components

### 1. Loan Class (`src/loanClass.py`)

**Purpose:** Core data model representing a single student loan.

**Attributes:**
- `lender` (str): Name of the lending institution
- `id` (str): Unique loan identifier
- `principle` (float): Initial loan amount
- `interest_rate` (float): Annual interest rate (as decimal, e.g., 0.05 = 5%)
- `loan_term` (int): Duration in months
- `monthly_payment` (float): Monthly payment amount
- `total_paid` (float): Amount already paid
- `remainder` (float): Calculated remaining balance (principle - total_paid)
- `total_interest` (float): Total interest paid

**Key Methods:**
- `__str__()`: Returns formatted string representation of loan details

**Usage Pattern:**
```python
from src.loanClass import Loan

loan = Loan(
    lender="TestLender",
    id="ID123",
    principle=10000,
    interest_rate=0.05,
    loan_term=120,
    monthly_payment=100,
    total_paid=1000,
    total_interest=500
)
```

### 2. Loan Scraper (`src/loan_scraper.py`)

**Purpose:** Production-ready web scraping module for extracting loan data.

**Key Function:**
- `scrape_loan_data(url)`: Scrapes loan information from a given URL and returns a list of Loan objects

**Implementation Notes:**
- Uses BeautifulSoup4 with requests library
- Expects HTML structure with `loan-item` class containing loan details
- Returns list of Loan objects
- Selectors are placeholders and need customization per loan provider

**Important:** The selectors (CSS classes) are currently placeholders and must be adjusted based on the actual HTML structure of the target loan provider's website.

### 3. Loan Website Extractor (`src/loanWebsiteExtractor.py`)

**Purpose:** Template file for custom loan scraping implementations (contains TODOs).

**Status:** This is a template/example file with TODO placeholders for customization.

**Note for AI Assistants:** This file is intended as a starting point for implementing custom scrapers. When working with this file, preserve the TODO comments as guidance for users.

### 4. Loan Analyzer (`src/loan_analyzer.py`)

**Purpose:** Analyzes loans and generates payment projections.

**Key Functions:**
- `calculate_future_payments(loan, months)`: Calculates monthly payments over specified period
  - Uses amortization formula
  - Returns list of payment amounts

- `graph_future_payments(loan, months)`: Generates and saves payment graph
  - Creates matplotlib visualization
  - Saves to file: `loan_{loan.id}_payments.png`
  - Uses 10x6 figure size with grid

**Graph Output:** PNG files saved to current working directory

### 5. Refinance Calculator (`src/refinance_calculator.py`)

**Purpose:** Calculates refinancing scenarios with different rates and terms.

**Key Function:**
- `calculate_refinance_options(loan, new_interest_rates, new_terms)`:
  - Accepts lists of potential interest rates and terms
  - Returns list of dictionaries with refinancing options
  - Each option contains: interest_rate, term, monthly_payment, total_interest

**Formula:** Uses standard loan amortization formula:
```
monthly_payment = (P * r * (1 + r)^n) / ((1 + r)^n - 1)
where: P = principle, r = monthly rate, n = number of months
```

### 6. Data Display (`src/dataDisplay.py`)

**Purpose:** Streamlit-based web UI for the application.

**Features:**
- Displays current loan portfolio in table format
- Interactive loan selection for analysis
- Future payment projection graphs
- Refinancing options comparison table

**Running the App:**
```bash
streamlit run src/dataDisplay.py
```

**Important:** Currently hardcoded to fetch from 'https://example-loan-provider.com/loans' - this needs to be customized for actual use.

---

## Testing Framework

### Testing Conventions

**Framework:** Python's built-in `unittest` module

**Structure:**
- All tests located in `tests/` directory
- Test files prefixed with `test_`
- Test classes inherit from `unittest.TestCase`
- Test methods prefixed with `test_`

**Running Tests:**
```bash
# Run all tests
python -m unittest discover tests

# Run specific test file
python -m unittest tests/test_loanClass.py

# Run specific test class
python -m unittest tests.test_loanClass.TestLoan

# Run specific test method
python -m unittest tests.test_loanClass.TestLoan.test_loan_initialization
```

### Testing Patterns

**1. Setup Method:**
Most tests use `setUp()` to create test fixtures:
```python
def setUp(self):
    self.loan = Loan("TestLender", "ID123", 10000, 0.05, 120, 100, 1000, 500)
```

**2. Mocking:**
Tests use `unittest.mock` for external dependencies:
- `@patch` decorator for mocking imports
- `MagicMock` for mock objects
- Common mocks: HTTP requests, matplotlib plotting

**3. Assertions:**
- `assertEqual()`: Exact value matching
- `assertAlmostEqual(places=2)`: Float comparisons
- `assertIsInstance()`: Type checking
- `assertIn()`: Membership testing
- `assertGreater()`: Numerical comparisons

**Test Coverage:**
- `test_loanClass.py`: Tests Loan initialization and string representation
- `test_loan_scraper.py`: Tests web scraping with mocked HTTP responses
- `test_loan_analyzer.py`: Tests payment calculations and graphing (mocked matplotlib)
- `test_refinance_calculator.py`: Tests refinancing option generation

---

## Development Workflows

### Setting Up Development Environment

```bash
# Clone repository
git clone <repository-url>
cd Student-Loan-Optimizer

# Install dependencies
pip install -r requirements.txt

# Run tests to verify setup
python -m unittest discover tests

# Run application
streamlit run src/dataDisplay.py
```

### Dependency Management

**Current Dependencies:**
```
streamlit       # Web UI framework
pandas          # Data manipulation
matplotlib      # Graphing
beautifulsoup4  # Web scraping
requests        # HTTP client
numpy           # Numerical computations
setuptools      # Build tools (for C extension)
```

**Adding New Dependencies:**
1. Add to `requirements.txt`
2. Install with `pip install -r requirements.txt`
3. Document in README.md if user-facing

### Git Workflow

**Main Branch:** Not explicitly specified (check repository settings)

**Current Branch:** `claude/add-claude-documentation-gmEZf`

**Branch Naming:**
- Feature branches should start with `claude/` prefix
- Include descriptive suffix

**Commit Conventions:**
- Use descriptive commit messages
- Start with action verb (e.g., "Add", "Fix", "Update", "Refactor")
- Reference issue numbers when applicable

---

## Code Conventions

### Python Style

**Import Organization:**
```python
# Standard library imports
import unittest
from unittest.mock import patch, MagicMock

# Third-party imports
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

# Local imports
from loanClass import Loan
from src.loanClass import Loan  # In tests
```

**Import Patterns in Tests:**
- Use `from src.<module> import <class/function>` for importing from src
- Absolute imports preferred over relative imports

### Naming Conventions

**Files:**
- Snake_case for Python files: `loan_scraper.py`, `loan_analyzer.py`
- CamelCase for classes: `loanClass.py` (contains `Loan` class)

**Variables/Functions:**
- Snake_case: `calculate_future_payments`, `loan_term`, `interest_rate`

**Classes:**
- PascalCase: `Loan`, `TestLoan`

**Constants:**
- Currently no uppercase constants used in codebase

### Documentation

**Docstrings:**
- Module-level docstrings in `loanClass.py` explain attributes
- Inline comments for complex logic
- TODO comments mark incomplete implementations

**Comment Style:**
```python
# Single-line comments for explanations
'''
Multi-line docstrings for class/module documentation
'''
```

---

## Important Patterns and Practices

### 1. Module Imports in src/

**Issue:** Files in `src/` use relative imports without the `src.` prefix.

**Examples:**
- `dataDisplay.py`: `from loan_scraper import scrape_loan_data`
- `loanWebsiteExtractor.py`: `import loanClass`

**Impact:** Running files directly may require `PYTHONPATH` adjustments or running from project root.

**AI Assistant Guidance:** When adding imports in `src/` files, follow existing pattern (direct imports without `src.` prefix). In tests, use `from src.<module>` pattern.

### 2. Data Flow

```
User Input → Loan Scraper → Loan Objects → Analyzer/Calculator → Display
```

1. `loan_scraper.py` fetches data from websites
2. Creates `Loan` objects from scraped data
3. Passes to `loan_analyzer.py` or `refinance_calculator.py`
4. Results displayed via `dataDisplay.py` Streamlit interface

### 3. Financial Calculations

**Interest Rate Format:** Stored as decimals (0.05 = 5%)
**Display Format:** Converted to percentages for UI (`f'{rate:.2%}'`)

**Monthly vs Annual Rates:**
- Loans store annual interest rates
- Calculations convert to monthly: `rate / 12`

### 4. File Outputs

**Generated Files:**
- Payment graphs: `loan_{loan_id}_payments.png`
- Saved to current working directory
- Not tracked in git (not in .gitignore but typically temporary)

**AI Assistant Guidance:** When generating visualization files, follow the naming pattern and consider adding cleanup logic or documenting the output location.

---

## Custom C Extension (Optional)

**Location:** `custom_data_structure/`

**Purpose:** Custom C extension module (implementation details in C file)

**Building:**
```bash
cd custom_data_structure
python setup.py build_ext --inplace
```

**Current Status:**
- Setup.py creates extension named 'my_extension'
- Not currently integrated with main application
- Optional dependency

**AI Assistant Guidance:** This is a separate component. Changes here require understanding of Python C API and setuptools. Test builds before committing.

---

## Common Tasks for AI Assistants

### Adding a New Loan Source

1. Create new scraper in `src/` or customize `loanWebsiteExtractor.py`
2. Implement function returning list of `Loan` objects
3. Update `dataDisplay.py` to support multiple sources
4. Add corresponding tests in `tests/`
5. Update README.md with new source documentation

### Adding New Loan Attributes

1. Update `loanClass.py` `__init__()` and `__str__()`
2. Update all scraper functions to extract new attributes
3. Update test fixtures in `tests/test_*.py` files
4. Update display logic in `dataDisplay.py`
5. Update calculator functions if attribute affects calculations

### Modifying Calculations

1. Locate formula in `loan_analyzer.py` or `refinance_calculator.py`
2. Update calculation logic
3. Update corresponding test assertions with new expected values
4. Verify formulas are mathematically correct
5. Document any formula changes in comments

### Adding New Visualizations

1. Add function to `loan_analyzer.py` or create new module
2. Use matplotlib with consistent style (10x6 figure, grid enabled)
3. Save with descriptive filename pattern
4. Add mock tests in corresponding test file
5. Integrate into `dataDisplay.py` Streamlit interface

---

## Known Issues and TODOs

### In Code TODOs:

**loanWebsiteExtractor.py:**
- Replace placeholder URL
- Identify correct CSS classes for target loan provider
- Implement multi-loan extraction
- Add error handling for failed requests

**dataDisplay.py:**
- Replace hardcoded example URL with actual loan provider
- Add configuration for multiple loan sources
- Improve error handling for missing data

### Potential Improvements:

1. **Configuration Management:** Add config file for URLs, settings
2. **Error Handling:** More robust error handling in scraping functions
3. **Data Persistence:** Save/load loan data (mentioned in future goals)
4. **Authentication:** User auth system (mentioned in future goals)
5. **Testing:** Add integration tests, increase coverage
6. **Type Hints:** Add Python type annotations for better IDE support
7. **Logging:** Add logging instead of print statements

---

## AI Assistant Guidelines

### When Making Changes:

1. **Read First:** Always read existing files before modifying
2. **Run Tests:** Execute relevant tests after changes
3. **Follow Patterns:** Match existing code style and patterns
4. **Update Tests:** Add/modify tests for new functionality
5. **Document:** Update this file and README.md for significant changes

### Code Quality Standards:

- **No Hardcoded Credentials:** Never commit API keys, passwords, or sensitive data
- **Security:** Validate external inputs, sanitize scraped data
- **Error Handling:** Add try/except for network requests and file operations
- **Testing:** Maintain or increase test coverage
- **Dependencies:** Minimize new dependencies, justify additions

### Communication:

- **Explain Changes:** Clearly describe what was changed and why
- **Reference Locations:** Use `file:line` format (e.g., `loanClass.py:14`)
- **Document Limitations:** Note what wasn't implemented or needs follow-up
- **Suggest Improvements:** Proactively identify technical debt or issues

### Testing Best Practices:

- Mock external dependencies (HTTP, file I/O, plotting)
- Use descriptive test method names
- Test edge cases (zero values, negative numbers, empty lists)
- Keep tests independent and repeatable

### Git Best Practices:

- Commit logical units of work
- Write clear commit messages
- Don't commit generated files (graphs, pycache, etc.)
- Test before pushing

---

## Project Context

### Current Milestone Status:

✅ **Completed:**
1. Extract loan info from loan provider website
2. Analyze loan info to graph future payments
3. Provide refinancing options calculator

### Future Roadmap:

1. Multiple loan provider support
2. Standardized API for loan data
3. Plugin system for providers
4. User authentication
5. Enhanced refinancing calculator
6. Side-by-side scenario comparison
7. ML-based optimization suggestions

### Project Maturity:

- **Stage:** Early development, core features complete
- **Stability:** Functional prototype, needs production hardening
- **Testing:** Basic unit tests in place, needs integration tests
- **Documentation:** README complete, code comments moderate

---

## Quick Reference

### Key Files by Function:

| Function | File | Tests |
|----------|------|-------|
| Data Model | `src/loanClass.py` | `tests/test_loanClass.py` |
| Web Scraping | `src/loan_scraper.py` | `tests/test_loan_scraper.py` |
| Payment Analysis | `src/loan_analyzer.py` | `tests/test_loan_analyzer.py` |
| Refinancing | `src/refinance_calculator.py` | `tests/test_refinance_calculator.py` |
| UI | `src/dataDisplay.py` | None (manual testing) |

### Command Cheat Sheet:

```bash
# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run src/dataDisplay.py

# Run all tests
python -m unittest discover tests

# Run specific test
python -m unittest tests.test_loanClass

# Build C extension (optional)
cd custom_data_structure && python setup.py build_ext --inplace
```

---

## Changelog

**2026-01-01:** Initial CLAUDE.md created with comprehensive codebase documentation

---

*This document is maintained for AI assistants working on the Student Loan Optimizer codebase. Keep it updated as the project evolves.*
