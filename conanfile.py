from conans import ConanFile, CMake, tools
import os


class StrawberryperlConan(ConanFile):
    name = "strawberryperl"
    version = "5.28.1.1"
    license = "https://raw.githubusercontent.com/StrawberryPerl/Perl-Dist-Strawberry/master/LICENSE"
    author = "KudzuRunner"
    url = "https://github.com/kudzurunner/conan-strawberryperl"
    description = "Perl environment for MS Windows"
    settings = "os", "arch"

    def _arch_type(self):
        return "32bit" if self.settings.arch == "x86" else "64bit"

    def configure(self):
        if self.settings.os != "Windows":
            raise Exception("Strawberry perl are only supported for MS Windows")

    def build(self):
        archive_name = "strawberry-perl-{0}-{1}-portable.zip".format(self.version, self._arch_type())
        url = "http://strawberryperl.com/download/{0}/{1}".format(self.version, archive_name)

        tools.download(url, filename=archive_name)
        tools.unzip(archive_name)
        os.remove(archive_name)

    def package(self):
        self.copy("*", keep_path=True)
        self.copy("licenses/License.rtf*", dst=".", keep_path=False, ignore_case=True)

    def package_info(self):
        self.env_info.PATH.append(os.path.join(self.package_folder, "perl", "bin"))
        self.env_info.PATH.append(os.path.join(self.package_folder, "c", "bin"))

