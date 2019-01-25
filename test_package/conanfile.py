from conans import ConanFile


class StrawberryperlTestConan(ConanFile):
    def test(self):
        self.run("perl --version")
