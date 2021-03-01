#!/bin/bash

JAVA_POPSTACK=" if (!_modeStack.isEmpty()) { popMode(); } "
PYTHON_POPSTACK="\nif len(self._modeStack) != 0:\n    self._modeStack.pop()\n"
WORKING_DIR=$(pwd)
OUTPUT_DIR="$WORKING_DIR/gen/parser"
LIB_DIR="$WORKING_DIR/kotlin-spec/grammar/src/main/antlr"

sed -i "s/$JAVA_POPSTACK/$PYTHON_POPSTACK/" ./kotlin-spec/grammar/src/main/antlr/KotlinLexer.g4

antlr4 -o "$OUTPUT_DIR" -Dlanguage=Python3 -no-listener -no-visitor -lib "$LIB_DIR" "$LIB_DIR/UnicodeClasses.g4"
antlr4 -o "$OUTPUT_DIR" -Dlanguage=Python3 -no-listener -no-visitor -lib "$LIB_DIR" "$LIB_DIR/KotlinLexer.g4"
antlr4 -o "$OUTPUT_DIR" -Dlanguage=Python3 -no-listener -no-visitor -lib "$LIB_DIR" "$LIB_DIR/KotlinParser.g4"