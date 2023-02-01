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
    args=["Expr.g4", "-Dlanguage=Python3", "-o", "../expr_parser", "-package", "expr_parser",],
    output_directories=["../expr_parser",],
    execution_dependencies=[":grammars"],
    workdir=".",
)

experimental_wrap_as_python_sources(name="expr_parser_py", inputs=[":run_antlr", ])

python_requirement(
    name="antlr4-python3-runtime",
    modules=["antlr4",],
    requirements=["antlr4-python3-runtime==4.11.1",],   
)
