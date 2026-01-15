import pytest
from tools.file_tools import read_file, write_file, list_dir


class TestReadFile:
    """Tests for the read_file function."""

    def test_read_file_success(self, tmp_path):
        """Test reading a file with contents."""
        test_file = tmp_path / "test.txt"
        expected_content = "Hello, World!"
        test_file.write_text(expected_content)

        result = read_file(str(test_file))

        assert result == expected_content

    def test_read_file_empty(self, tmp_path):
        """Test reading an empty file."""
        test_file = tmp_path / "empty.txt"
        test_file.write_text("")

        result = read_file(str(test_file))

        assert result == ""

    def test_read_file_multiline(self, tmp_path):
        """Test reading a file with multiple lines."""
        test_file = tmp_path / "multiline.txt"
        expected_content = "Line 1\nLine 2\nLine 3\n"
        test_file.write_text(expected_content)

        result = read_file(str(test_file))

        assert result == expected_content

    def test_read_file_not_found(self, tmp_path):
        """Test reading a non-existent file."""
        non_existent = tmp_path / "does_not_exist.txt"

        with pytest.raises(FileNotFoundError):
            read_file(str(non_existent))

    def test_read_file_unicode(self, tmp_path):
        """Test reading a file with unicode characters."""
        test_file = tmp_path / "unicode.txt"
        expected_content = "Hello 世界 🌍"
        test_file.write_text(expected_content, encoding="utf-8")

        result = read_file(str(test_file))

        assert result == expected_content


class TestWriteFile:
    """Tests for the write_file function."""

    def test_write_file_success(self, tmp_path):
        """Test writing content to a new file."""
        test_file = tmp_path / "output.txt"
        content = "Test content"

        result = write_file(str(test_file), content)

        assert result is True
        assert test_file.read_text() == content

    def test_write_file_overwrite(self, tmp_path):
        """Test overwriting an existing file."""
        test_file = tmp_path / "existing.txt"
        test_file.write_text("Original content")

        new_content = "New content"
        result = write_file(str(test_file), new_content)

        assert result is True
        assert test_file.read_text() == new_content

    def test_write_file_empty_content(self, tmp_path):
        """Test writing an empty string to a file."""
        test_file = tmp_path / "empty.txt"

        result = write_file(str(test_file), "")

        assert result is True
        assert test_file.read_text() == ""

    def test_write_file_multiline(self, tmp_path):
        """Test writing multiline content."""
        test_file = tmp_path / "multiline.txt"
        content = "Line 1\nLine 2\nLine 3\n"

        result = write_file(str(test_file), content)

        assert result is True
        assert test_file.read_text() == content

    def test_write_file_unicode(self, tmp_path):
        """Test writing unicode content."""
        test_file = tmp_path / "unicode.txt"
        content = "Hello 世界 🌍"

        result = write_file(str(test_file), content)

        assert result is True
        assert test_file.read_text() == content

    def test_write_file_creates_file(self, tmp_path):
        """Test that write_file creates a new file if it doesn't exist."""
        test_file = tmp_path / "new_file.txt"
        assert not test_file.exists()

        write_file(str(test_file), "content")

        assert test_file.exists()

    def test_write_file_invalid_path(self, tmp_path):
        """Test writing to an invalid path."""
        invalid_path = tmp_path / "nonexistent_dir" / "file.txt"

        with pytest.raises(FileNotFoundError):
            write_file(str(invalid_path), "content")


class TestListDir:
    """Tests for the list_dir function."""

    def test_list_dir_empty(self, tmp_path):
        """Test listing an empty directory."""
        result = list_dir(str(tmp_path))

        assert result == []

    def test_list_dir_with_files(self, tmp_path):
        """Test listing a directory with files."""
        (tmp_path / "file1.txt").write_text("content1")
        (tmp_path / "file2.txt").write_text("content2")
        (tmp_path / "file3.txt").write_text("content3")

        result = list_dir(str(tmp_path))

        assert set(result) == {"file1.txt", "file2.txt", "file3.txt"}
        assert len(result) == 3

    def test_list_dir_with_subdirs(self, tmp_path):
        """Test listing a directory with subdirectories."""
        (tmp_path / "subdir1").mkdir()
        (tmp_path / "subdir2").mkdir()
        (tmp_path / "file.txt").write_text("content")

        result = list_dir(str(tmp_path))

        assert set(result) == {"subdir1", "subdir2", "file.txt"}
        assert len(result) == 3

    def test_list_dir_mixed_content(self, tmp_path):
        """Test listing a directory with files and subdirectories."""
        (tmp_path / "dir1").mkdir()
        (tmp_path / "file1.txt").write_text("content")
        (tmp_path / ".hidden").write_text("hidden")

        result = list_dir(str(tmp_path))

        assert ".hidden" in result
        assert "dir1" in result
        assert "file1.txt" in result

    def test_list_dir_not_found(self, tmp_path):
        """Test listing a non-existent directory."""
        non_existent = tmp_path / "does_not_exist"

        with pytest.raises(FileNotFoundError):
            list_dir(str(non_existent))

    def test_list_dir_not_directory(self, tmp_path):
        """Test listing a file instead of a directory."""
        test_file = tmp_path / "file.txt"
        test_file.write_text("content")

        with pytest.raises(NotADirectoryError):
            list_dir(str(test_file))

    def test_list_dir_with_tilde(self):
        """Test that list_dir expands tilde in path."""
        # This should not raise an error if home directory exists
        result = list_dir("~")

        assert isinstance(result, list)
        assert len(result) > 0
