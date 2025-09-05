from antlr4 import *
from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser

# === Entrada de prueba ===
#input_text = "if (x > 10) { y = y + 1; } else { y = y - 1; };"

input_text = """i = 0;
while (i < 10) {
  if (i == 5) {
    break;
  }
  i = i + 1;
  continue;
}"""

# Crear flujo de entrada
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = WhileLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## 🔤 TOKENS")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        print(f"  - {lexer.symbolicNames[token.type]} ('{token.text}') @line {token.line}:{token.column}")

print("\n## 🌳 ÁRBOL SINTÁCTICO (toStringTree)")
parser = WhileLangParser(token_stream)
tree = parser.program()
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    if isinstance(node, TerminalNode):
        return "  " * level + f"TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = "  " * level + rule_name
        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)
        return result

print("\n## 🌲 ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))