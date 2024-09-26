import pytest

@pytest.fixture(scope="session")
def setup():
    """Setup resources before running tests."""
    # You can add global setup logic here
    yield
    # Teardown logic after all tests
