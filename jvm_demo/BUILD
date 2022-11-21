# Specify JAR dependencies
jvm_artifact(
    name="openapi-generator",
    group="org.openapitools",
    artifact="openapi-generator-cli",
    version="6.2.1",
)

# Files dependencies
file(
    name="openapi-schema",
    source="openapi-schema.yaml",
)

# Define a target that reifies the JAR dependencies into something that gets exported
deploy_jar(
    name="openapi-generator-cli-tool",
    main="org.openapitools.codegen.OpenAPIGenerator",
    dependencies=[
        ":openapi-generator",
    ],
)

# Generate the openapi-bindins from a schema
experimental_shell_command(
    name="generate-openapi-bindings",
    tools=["java", ],  # <--- Not the Pants-managed JVM toolchain. May be incompatible.
    command="java -jar openapi-generator-cli-tool.jar generate -i openapi-schema.yaml -g javascript -o ./js-bindings",
    dependencies=[":openapi-generator-cli-tool", ":openapi-schema",],
    outputs=["js-bindings/",]
)

relocated_files(
    name="openapi-bindings-files",
    files_targets=[":generate-openapi-bindings",],
    src="jvm_demo/js-bindings",
    dest="",
)

archive(
    name="openapi-bindings",
    format="tar.gz",
    description="Open api bindings from sample schema",
    files=[":openapi-bindings-files",],
)

# Allow end-users to run the tool using Pants
experimental_run_shell_command(
    name="run-openapi-generator",
    command="java -jar {chroot}/jvm_demo/openapi-generator-cli-tool.jar list",
    dependencies=[":openapi-generator-cli-tool",],
)

# Demo consuming an output from running Java in the sandbox
experimental_run_shell_command(
    name="list-outputs",
    command="ls -laR {chroot}",
    dependencies=[":openapi-generator-js-bindings",],
)