# Dependencies and source files
files(
    name="package-config",
    sources=["package.json", "yarn.lock",],
    dependencies=[],
)

# The source files themselves
files(
    name="js-sources",
    sources=["*.js",],
    dependencies=[],
)

# Fetch the dependencies and produce a `node_modules` directory
experimental_shell_command(
    name="node-modules",
    command="yarn install --immutable",
    tools=[
        "yarn",
        "node",
    ],
    dependencies=[
        ":package-config",
    ],
    outputs=["node_modules/"],
    timeout=300,
)

# Minify the JS sources and dependencies into a single js file.
experimental_shell_command(
    name="_build-js-app",
    command="yarn parcel build",
    tools=[
        "yarn",
        "node",
    ],
    dependencies=[":node-modules", ":js-sources",],
    outputs=["index.js", "index.js.map",],
)

# Move the output out of the source tree location
relocated_files(
    name="build-js-app",
    files_targets=[":_build-js-app", ],
    src="js_demo",  # <--- Awkward. Requires knowledge of this BUILD file's location
    dest="",
)

# Run the resulting JS file
experimental_run_shell_command(
    name="run-js-app",
    command="node {chroot}/index.js",
    dependencies=[":build-js-app",],
)

# Demonstrate using the JS file as an input to an artifact
archive(
    name="packaged-js",
    format="tar",
    description="Package containing `index.js` file",
    files=[":build-js-app",],
)