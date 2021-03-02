from gensim.models import Word2Vec

from antlr4 import *
from antlr4.tree.Trees import Trees
from os import walk, path

from gen.parser.KotlinLexer import KotlinLexer
from gen.parser.KotlinParser import KotlinParser


def rule_representation(tree, rule_names):
    result = [str(tree.getRuleIndex())]

    parent = Trees.getNodeText(tree, rule_names)
    nodes = [parent]
    for child in tree.getChildren():
        nodes.append(Trees.getNodeText(child, rule_names))

    result.append('_'.join(nodes))
    result.append(parent)

    return '_'.join(result)


def ast_to_rule_seq(tree, rule_names, rule_repr):
    if isinstance(tree, TerminalNode):
        return []

    rule_seq = [rule_repr(tree, rule_names)]

    for child in tree.getChildren():
        rule_seq.extend(ast_to_rule_seq(child, rule_names, rule_repr))

    return rule_seq


def process_file(file_name):
    input_stream = FileStream("data/box/classes/kt8011a.kt")
    lexer = KotlinLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = KotlinParser(stream)

    root = parser.kotlinFile()
    rule_names = parser.ruleNames

    return ast_to_rule_seq(root, rule_names, rule_representation)


def main():
    kt_files = []
    for root, dirs, files in walk("data/box"):
        for file in files:
            if file.endswith(".kt"):
                kt_files.append(path.join(root, file))

    data = list(map(process_file, kt_files))

    model = Word2Vec(data,
                     size=64,
                     window=10).wv

    vec = model.get_vector(data[0][0])
    print(vec)
    # process vector


if __name__ == "__main__":
    main()
