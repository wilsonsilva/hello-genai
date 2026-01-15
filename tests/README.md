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
uv run pytest --cov=tools --cov-report=term-missing
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
