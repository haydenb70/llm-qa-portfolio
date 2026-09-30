"""Guard tests for the chatbot's source data.

The evals treat data/product-info.md as the truth. If that file is missing a
required fact, every eval built on it is meaningless, so we check it first.

Coming from Java + JUnit:
- No test class is required. Any function named test_* is a test.
- Plain `assert` replaces assertEquals / assertTrue.
- @pytest.fixture replaces @BeforeEach setup.
- @pytest.mark.parametrize replaces @ParameterizedTest.
"""

from pathlib import Path

import pytest

DATA_FILE = Path(__file__).parent.parent / "data" / "product-info.md"


@pytest.fixture
def product_info() -> str:
    """Load the source file once per test (like @BeforeEach)."""
    return DATA_FILE.read_text(encoding="utf-8").lower()


def test_data_file_exists():
    assert DATA_FILE.exists(), f"Missing source data: {DATA_FILE}"


@pytest.mark.parametrize(
    "required_fact",
    ["filter life", "certified to reduce", "not certified to remove", "warranty", "returns"],
)
def test_source_includes_required_fact(product_info, required_fact):
    assert required_fact in product_info, f"Source data is missing: {required_fact}"
