# Tests

This directory contains tests for the hello-genai project.

## Running Tests

### Run all tests
```bash
uv run pytest
```

### Run tests with verbose output
```bash
uv run pytest -v
```

### Run specific test file
```bash
uv run pytest tests/test_file_tools.py
```

### Run specific test class
```bash
uv run pytest tests/test_file_tools.py::TestReadFile
```

### Run specific test method
```bash
uv run pytest tests/test_file_tools.py::TestReadFile::test_read_file_success
```

### Run with coverage
```bash
# Run tests with coverage
uv run coverage run -m pytest

# View coverage report
uv run coverage report

# Generate HTML report
uv run coverage html
# Then open coverage/html/index.html in browser

# Generate all reports (lcov, HTML, XML)
uv run coverage lcov && uv run coverage html && uv run coverage xml
```

## Test Structure

- `test_file_tools.py` - Tests for file operations in `tools/file_tools.py`
  - `TestReadFile` - Tests for `read_file()` function
  - `TestWriteFile` - Tests for `write_file()` function
  - `TestListDir` - Tests for `list_dir()` function
  - `TestLogFunctionCallDecorator` - Tests for the `@log_function_call` decorator

## Test Coverage

The test suite covers:
- Happy path scenarios (successful operations)
- Edge cases (empty files, empty directories, unicode content)
- Error cases (file not found, invalid paths, wrong file types)
- Decorator functionality (logging, function name preservation)
