# Copyright 2022 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

jvm_artifact(
    name="antlr4",
    group="org.antlr",
    artifact="antlr4",
    version="4.11.1",
)

files(name="grammars", sources=["*.g4"])

python_source(
    name="antlr_demo",
    source="antlr_demo.py",
    dependencies=[":expr_parser_py", ":antlr4-python3-runtime",],
)

experimental_run_in_sandbox(
    name="run_antlr",
    runnable=":antlr4",
    args=["Expr.g4", "-Dlanguage=Python3"],
    output_files=["*.py"],
    execution_dependencies=[":grammars"],
    workdir=".",
)

relocated_files(
    name="expr_parser_py_files",
    files_targets=[":run_antlr"],
    src=f"{build_file_dir()}",
    dest="expr_parser",
)

experimental_shell_command(
    name="make_expr_parser_package",
    tools=["touch"],
    command="touch expr_parser/__init__.py",
    output_files=["expr_parser/__init__.py",],
)

experimental_wrap_as_python_sources(name="expr_parser_py", inputs=[":expr_parser_py_files", ":make_expr_parser_package"])

python_requirement(
    name="antlr4-python3-runtime",
    modules=["antlr4",],
    requirements=["antlr4-python3-runtime==4.11.1",],   
)
