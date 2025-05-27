import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from GramaticaMKSLexer import GramaticaMKSLexer
from GramaticaMKSParser import GramaticaMKSParser
from MKSVisitor import MyVisitor

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Leer desde un archivo si se proporciona un argumento
        input_stream = FileStream(sys.argv[1], encoding="utf-8")
    else:
        # Leer toda la entrada estándar hasta EOF
        try:
            # Leer todo el contenido de stdin
            stdin_content = sys.stdin.read()
            input_stream = InputStream(stdin_content)
        except KeyboardInterrupt:
            # Manejar interrupciones del usuario (Ctrl + C)
            print("\nInterrupción por el usuario.")
            sys.exit(0)

    lexer = GramaticaMKSLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = GramaticaMKSParser(token_stream)
    tree = parser.program()

    visitor = MyVisitor()
    visitor.visit(tree)
