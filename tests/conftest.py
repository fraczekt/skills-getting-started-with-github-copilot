import copy

import pytest

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    original_activities = copy.deepcopy(app_module.activities)

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))

    yield

    app_module.activities.clear()
    app_module.activities.update(copy.deepcopy(original_activities))
