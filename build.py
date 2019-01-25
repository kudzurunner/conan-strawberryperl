from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="kudzurunner")
    builder.add(settings={"arch": "x86_64", "os": "Windows"}, options={}, env_vars={}, build_requires={})
    builder.add(settings={"arch": "x86", "os": "Windows"}, options={}, env_vars={}, build_requires={})
    builder.run()
