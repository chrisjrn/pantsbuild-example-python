# Specify JAR dependencies
jvm_artifact(
    name="openapi-generator",
    group="org.openapitools",
    artifact="openapi-generator-cli",
    version="6.2.1",
)

# Define a target that reifies the JAR dependencies into something that gets exported
deploy_jar(
    name="openapi-generator-cli-tool",
    main="org.openapitools.codegen.OpenAPIGenerator",
    dependencies=[
        ":openapi-generator",
    ],
)

# Demonstrate running JVM in a sandbox
experimental_shell_command(
    name="openapi-generator-help-text",
    tools=["java",],  # <--- Not the Pants-managed JVM toolchain. May be incompatible.
    command="(java -jar openapi-generator-cli-tool.jar > helptext.txt) || true",
    dependencies=[":openapi-generator-cli-tool",],
    outputs=["helptext.txt",]
)

# Allow end-users to run the tool using Pants
experimental_run_shell_command(
    name="run-openapi-generator",
    command="java -jar {chroot}/jvm_demo/openapi-generator-cli-tool.jar",
    dependencies=[":openapi-generator-cli-tool",],
)

# Demo consuming an output from running Java in the sandbox
experimental_run_shell_command(
    name="openapi-show-help",
    command="cat {chroot}/jvm_demo/helptext.txt",
    #command="ls -laR {chroot}",
    dependencies=[":openapi-generator-help-text",],
)