from conan import ConanFile
from conan.tools.build import can_run
from conan.tools.cmake import cmake_layout

class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def layout(self):
        cmake_layout(self)

    def test(self):
        if can_run(self):
            self.run("re2c --version", env="conanrun")
