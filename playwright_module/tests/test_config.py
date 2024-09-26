import pytest

@pytest.fixture(scope="session")
def setup():
    """Setup resources before running tests."""
    # Global setup logic can be added here if needed
    yield
    # Global teardown logic after all tests
