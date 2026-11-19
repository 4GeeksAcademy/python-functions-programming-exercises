"""
Validation tests to ensure the testing infrastructure is working correctly.
"""
import pytest
import sys
from pathlib import Path


@pytest.mark.unit
def test_pytest_is_working():
    """Test that pytest is working correctly."""
    assert True


@pytest.mark.unit  
def test_temp_dir_fixture(temp_dir):
    """Test that the temp_dir fixture works."""
    assert temp_dir.exists()
    assert temp_dir.is_dir()
    
    # Create a test file
    test_file = temp_dir / "test.txt"
    test_file.write_text("test content")
    assert test_file.exists()
    assert test_file.read_text() == "test content"


@pytest.mark.unit
def test_mock_config_fixture(mock_config):
    """Test that the mock_config fixture works."""
    assert isinstance(mock_config, dict)
    assert "test_mode" in mock_config
    assert mock_config["test_mode"] is True


@pytest.mark.unit
def test_sample_data_fixture(sample_data):
    """Test that the sample_data fixture works."""
    assert "numbers" in sample_data
    assert "strings" in sample_data
    assert "mixed" in sample_data
    assert len(sample_data["numbers"]) == 5


@pytest.mark.unit
def test_mock_file_system_fixture(mock_file_system):
    """Test that the mock_file_system fixture works."""
    assert mock_file_system.exists()
    assert (mock_file_system / "test.txt").exists()
    assert (mock_file_system / "test.txt").read_text() == "Hello, World!"


@pytest.mark.unit
def test_capture_stdout_fixture(capture_stdout):
    """Test that the capture_stdout fixture works."""
    with capture_stdout() as captured:
        print("test output")
        output = captured.getvalue()
        assert "test output" in output


@pytest.mark.unit
def test_mock_print_fixture(mock_print):
    """Test that the mock_print fixture works."""
    print("test message")
    mock_print.assert_called_once_with("test message")


@pytest.mark.integration
def test_project_structure():
    """Test that the project has the expected structure."""
    project_root = Path("/workspace")
    
    # Check that key directories exist
    assert (project_root / "exercises").exists()
    assert (project_root / "tests").exists()
    assert (project_root / "tests" / "unit").exists()
    assert (project_root / "tests" / "integration").exists()
    
    # Check that key files exist
    assert (project_root / "pyproject.toml").exists()
    assert (project_root / "tests" / "conftest.py").exists()


@pytest.mark.integration
def test_exercises_structure():
    """Test that exercises have the expected structure."""
    exercises_dir = Path("/workspace/exercises")
    
    # Find at least one exercise directory
    exercise_dirs = [d for d in exercises_dir.iterdir() if d.is_dir()]
    assert len(exercise_dirs) > 0
    
    # Check first exercise has expected files
    first_exercise = exercise_dirs[0]
    expected_files = ["README.md", "app.py"]
    
    for expected_file in expected_files:
        file_path = first_exercise / expected_file
        if file_path.exists():
            assert file_path.is_file()


@pytest.mark.slow
def test_performance_placeholder():
    """Placeholder test for performance testing (marked as slow)."""
    import time
    time.sleep(0.1)  # Simulate a slow operation
    assert True


class TestInfrastructureClass:
    """Test class to verify class-based testing works."""
    
    @pytest.mark.unit
    def test_class_based_testing(self):
        """Test that class-based tests work."""
        assert hasattr(self, 'test_class_based_testing')
    
    @pytest.mark.unit
    def test_with_fixture(self, sample_data):
        """Test that fixtures work in class-based tests."""
        assert sample_data is not None