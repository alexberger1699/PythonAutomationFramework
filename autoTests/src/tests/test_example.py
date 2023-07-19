import pytest

@pytest.mark.usefixtures("init_driver")
class TestExample():

    def test_example_func(self):
        print("example")
        self.driver.get("https://supersqa.com")
        import pdb; pdb.set_trace()
