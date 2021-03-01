import os
from antlr4 import *
from gen.parser.KotlinLexer import KotlinLexer
from gen.parser.KotlinParser import KotlinParser


def main():
    input_stream = FileStream("data/box/classes/kt8011a.kt")
    lexer = KotlinLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KotlinParser(stream)
    tree = parser.kotlinFile()

    # Process tree


if __name__ == "__main__":
    main()
