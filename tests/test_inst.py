import pytest

from src.ste.inst import Experiement


@pytest.fixture(scope="session")
def experiment():
    """
    Creates an experiment object.

    Returns:
        Experiment: The created experiment object.
    """
    experiment = Experiement()
    return experiment


def test_create_exp(experiment):
    """
    Test the creation of an experiment.

    Args:
        experiment (Experiment): The experiment object to be tested.

    Returns:
        None
    """


def test_create_exp(experiment):
    assert isinstance(experiment, Experiement)


def test_empty_exp(experiment):
    """
    Test case to verify that the snapshot of the experiment's station is empty.

    Args:
        experiment: The experiment object.

    Returns:
        None
    """
    snpshot = experiment.show_station()
    assert all(v == {} or v == None for v in snpshot.values())


if __name__ == "__main__":
    test_create_exp()
    test_empty_exp()
