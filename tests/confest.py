

from src.processing import state_inform


@pytest.fixture
def test_info_state() -> str:
    return "EXECUTED"


@pytest.fixture
def test_info_state_1() -> list[dict[str, object]]:
    return state_inform