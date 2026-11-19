import pytest
import tempfile
import shutil
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch
from typing import Any, Dict, Generator


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Provide a temporary directory that gets cleaned up after the test."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def mock_config() -> Dict[str, Any]:
    """Provide a mock configuration dictionary."""
    return {
        "test_mode": True,
        "debug": False,
        "timeout": 30,
        "retries": 3
    }


@pytest.fixture
def app():
    """Import and return the app module from exercises."""
    import importlib.util
    
    # Get the current test file path
    frame = sys._getframe()
    while frame:
        filename = frame.f_code.co_filename
        if 'exercises/' in filename and filename.endswith('.py'):
            # Extract exercise directory from test file path
            exercise_dir = filename.split('exercises/')[1].split('/')[0]
            app_path = f"/workspace/exercises/{exercise_dir}/app.py"
            
            if os.path.exists(app_path):
                # Load the module dynamically
                spec = importlib.util.spec_from_file_location("app", app_path)
                if spec and spec.loader:
                    app_module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(app_module)
                    return app_module
            
            pytest.skip(f"No app.py found at {app_path}")
        frame = frame.f_back
    
    pytest.skip("Not running in an exercise context")


@pytest.fixture
def mock_print():
    """Mock the print function for testing console output."""
    with patch('builtins.print') as mock:
        yield mock


@pytest.fixture
def mock_input():
    """Mock the input function for testing user input."""
    with patch('builtins.input') as mock:
        yield mock


@pytest.fixture
def capture_stdout():
    """Capture stdout for testing printed output."""
    from io import StringIO
    import contextlib
    
    captured_output = StringIO()
    
    @contextlib.contextmanager
    def _capture():
        old_stdout = sys.stdout
        sys.stdout = captured_output
        try:
            yield captured_output
        finally:
            sys.stdout = old_stdout
    
    return _capture


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        "numbers": [1, 2, 3, 4, 5],
        "strings": ["hello", "world", "test"],
        "mixed": [1, "two", 3.0, True, None]
    }


@pytest.fixture(autouse=True)
def reset_modules():
    """Reset imported modules before each test to avoid state pollution."""
    modules_to_remove = [
        mod for mod in sys.modules.keys() 
        if mod.startswith('app') and 'exercises' in str(sys.modules.get(mod, ''))
    ]
    for mod in modules_to_remove:
        sys.modules.pop(mod, None)


@pytest.fixture
def exercise_path():
    """Get the path to the current exercise directory."""
    test_file = os.environ.get('PYTEST_CURRENT_TEST', '')
    if 'exercises/' in test_file:
        exercise_name = test_file.split('exercises/')[1].split('/')[0]
        return Path(f"/workspace/exercises/{exercise_name}")
    return None


@pytest.fixture
def mock_file_system(temp_dir):
    """Create a mock file system structure for testing."""
    test_files = {
        "test.txt": "Hello, World!",
        "data.json": '{"key": "value"}',
        "empty.txt": "",
        "numbers.txt": "1\n2\n3\n4\n5"
    }
    
    for filename, content in test_files.items():
        (temp_dir / filename).write_text(content)
    
    return temp_dir


@pytest.fixture
def environment_vars():
    """Mock environment variables for testing."""
    test_env = {
        "TEST_MODE": "true",
        "DEBUG_LEVEL": "info"
    }
    
    with patch.dict(os.environ, test_env):
        yield test_env