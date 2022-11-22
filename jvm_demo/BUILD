# Specify JAR dependencies
jvm_artifact(
    name="openapi-generator",
    group="org.openapitools",
    artifact="openapi-generator-cli",
    version="6.2.1",
)


# Python files to be inspected by external tool
python_source(
    name="python-library-with-api-annotations", 
    source="print_schema.py",
)


# Define an executable tool with 3rd party dependencies. This could be entirely
# `python_requirement`s and the pex entry point could be a module from those requirements
python_requirement(
    name="setuptools",
    requirements=["setuptools>=56.2.0,<57",],
)

python_requirement(
    name="pyfiglet",
    requirements=["pyfiglet==0.7",],
)

python_source(
    name="generate-schema",
    source="generate_schema.py",
    dependencies=[":setuptools",],
)

pex_binary(
    name="generate-schema-pex", 
    entry_point="generate_schema.py",
)


# Define a JVM executable target that reifies the `jvm_artifact`
deploy_jar(
    name="openapi-generator-cli-tool",
    main="org.openapitools.codegen.OpenAPIGenerator",
    dependencies=[
        ":openapi-generator",
    ],
)


# Generate the schema
experimental_shell_command(
    name="openapi-schema",
    tools=["python3.9",],  # Not managed by pants interpreter constraints, may be incompatible
    command="python3.9 generate-schema-pex.pex > generated-schema.yaml", # You need to know the pex filename
    dependencies=[":generate-schema-pex", ":python-library-with-api-annotations"],
    outputs=["generated-schema.yaml"],
)


# Generate the openapi bindings from a schema produced by a different step
experimental_shell_command(
    name="generate-openapi-js-bindings",
    tools=["java", "python3.9",],  # <--- Not the Pants-managed JVM toolchain. May be incompatible.
    command="java -jar openapi-generator-cli-tool.jar generate -i generated-schema.yaml -g javascript -o ./js-bindings",
    dependencies=[":openapi-generator-cli-tool", ":openapi-schema",],
    outputs=["js-bindings/",]
)


# Move the files so that the resulting archive doesn't resemble our monorepo
relocated_files(
    name="openapi-js-bindings-files",
    files_targets=[":generate-openapi-js-bindings",],
    src="jvm_demo/js-bindings",
    dest="",
)


# The output artifact
archive(
    name="openapi-js-bindings",
    format="tar.gz",
    description="Open api bindings from sample schema",
    files=[":openapi-js-bindings-files",],
)


####
#### UTILITY RULES FOR TESTING/DEBUGGING
####

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
    dependencies=[":openapi-bindings", ":generate-schema", ":generate-schema-pex",],
)