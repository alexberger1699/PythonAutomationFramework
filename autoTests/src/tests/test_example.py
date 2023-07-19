import pytest

@pytest.mark.usefixtures("init_driver")
class TestExample():

    def test_example_func(self):
        print("example")

        import pdb; pdb.set_trace()
