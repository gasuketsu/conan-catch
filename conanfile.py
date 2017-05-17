from conans import ConanFile, tools


class CatchConan(ConanFile):
    name = "Catch"
    version = "1.9.4"
    description = "A modern, C++-native, header-only, framework for unit-tests, TDD and BDD C++ Automated Test Cases in Headers"
    license = "Boost"
    url = "https://github.com/gasuketsu/conan-catch"
    settings = None

    def source(self):
        tools.download("https://github.com/philsquared/Catch/releases/download/v%s/catch.hpp" % self.version, "catch.hpp")

    def build(self):
        pass

    def package(self):
        self.copy("catch.hpp", dst="include", src=".")

    def package_info(self):
        self.cpp_info.libdirs = []
