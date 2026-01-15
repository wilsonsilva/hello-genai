import pytest
from utils import log_function_call


class TestLogFunctionCallDecorator:
    """Tests for the log_function_call decorator."""

    def test_decorator_preserves_function_name(self):
        """Test that decorator preserves the original function name."""

        @log_function_call
        def sample_function():
            return "result"

        assert sample_function.__name__ == "sample_function"

    def test_decorator_preserves_docstring(self):
        """Test that decorator preserves the original docstring."""

        @log_function_call
        def sample_function():
            """This is a docstring."""
            return "result"

        assert sample_function.__doc__ == "This is a docstring."

    def test_decorator_logs_function_call_no_args(self, capsys):
        """Test that decorator logs function calls with no arguments."""

        @log_function_call
        def no_args_function():
            return "result"

        result = no_args_function()

        captured = capsys.readouterr()
        assert "[Function Call] no_args_function()" in captured.out
        assert result == "result"

    def test_decorator_logs_positional_arguments(self, capsys):
        """Test that decorator logs positional arguments."""

        @log_function_call
        def positional_args(arg1, arg2):
            return f"{arg1}, {arg2}"

        result = positional_args("hello", "world")

        captured = capsys.readouterr()
        assert "[Function Call] positional_args" in captured.out
        assert "'hello'" in captured.out
        assert "'world'" in captured.out
        assert result == "hello, world"

    def test_decorator_logs_keyword_arguments(self, capsys):
        """Test that decorator logs keyword arguments."""

        @log_function_call
        def keyword_args(name=None, value=None):
            return f"{name}={value}"

        result = keyword_args(name="key", value=42)

        captured = capsys.readouterr()
        assert "[Function Call] keyword_args" in captured.out
        assert "name: 'key'" in captured.out
        assert "value: 42" in captured.out
        assert result == "key=42"

    def test_decorator_logs_mixed_arguments(self, capsys):
        """Test that decorator logs both positional and keyword arguments."""

        @log_function_call
        def mixed_args(pos1, pos2, key1=None, key2=None):
            return (pos1, pos2, key1, key2)

        result = mixed_args("a", "b", key1="c", key2="d")

        captured = capsys.readouterr()
        assert "[Function Call] mixed_args" in captured.out
        assert "'a'" in captured.out
        assert "'b'" in captured.out
        assert "key1: 'c'" in captured.out
        assert "key2: 'd'" in captured.out
        assert result == ("a", "b", "c", "d")

    def test_decorator_logs_numeric_arguments(self, capsys):
        """Test that decorator logs numeric arguments."""

        @log_function_call
        def numeric_args(integer, floating):
            return integer + floating

        result = numeric_args(42, 3.14)

        captured = capsys.readouterr()
        assert "[Function Call] numeric_args" in captured.out
        assert "42" in captured.out
        assert "3.14" in captured.out
        assert result == 45.14

    def test_decorator_logs_list_arguments(self, capsys):
        """Test that decorator logs list arguments."""

        @log_function_call
        def list_args(items):
            return len(items)

        result = list_args([1, 2, 3])

        captured = capsys.readouterr()
        assert "[Function Call] list_args" in captured.out
        assert "[1, 2, 3]" in captured.out
        assert result == 3

    def test_decorator_logs_dict_arguments(self, capsys):
        """Test that decorator logs dictionary arguments."""

        @log_function_call
        def dict_args(data):
            return data["key"]

        result = dict_args({"key": "value"})

        captured = capsys.readouterr()
        assert "[Function Call] dict_args" in captured.out
        assert "{'key': 'value'}" in captured.out
        assert result == "value"

    def test_decorator_returns_correct_value(self):
        """Test that decorator returns the correct value from the wrapped function."""

        @log_function_call
        def return_value_function():
            return 42

        result = return_value_function()
        assert result == 42

    def test_decorator_propagates_exceptions(self):
        """Test that decorator propagates exceptions from the wrapped function."""

        @log_function_call
        def exception_function():
            raise ValueError("Test exception")

        with pytest.raises(ValueError, match="Test exception"):
            exception_function()

    def test_decorator_works_with_none_return(self, capsys):
        """Test that decorator works with functions that return None."""

        @log_function_call
        def none_return():
            pass

        result = none_return()

        captured = capsys.readouterr()
        assert "[Function Call] none_return()" in captured.out
        assert result is None

    def test_decorator_with_empty_string_argument(self, capsys):
        """Test that decorator logs empty string arguments."""

        @log_function_call
        def empty_string_arg(text):
            return len(text)

        result = empty_string_arg("")

        captured = capsys.readouterr()
        assert "[Function Call] empty_string_arg" in captured.out
        assert "''" in captured.out
        assert result == 0

    def test_decorator_with_boolean_arguments(self, capsys):
        """Test that decorator logs boolean arguments."""

        @log_function_call
        def boolean_args(flag1, flag2):
            return flag1 and flag2

        result = boolean_args(True, False)

        captured = capsys.readouterr()
        assert "[Function Call] boolean_args" in captured.out
        assert "True" in captured.out
        assert "False" in captured.out
        assert result is False

    def test_decorator_multiple_calls(self, capsys):
        """Test that decorator logs multiple calls to the same function."""

        @log_function_call
        def multi_call(value):
            return value * 2

        multi_call(5)
        multi_call(10)

        captured = capsys.readouterr()
        assert captured.out.count("[Function Call] multi_call") == 2
        assert "5" in captured.out
        assert "10" in captured.out
