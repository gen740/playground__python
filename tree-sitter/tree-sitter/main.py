import os
from tree_sitter import Language, Parser
import sys
from pathlib import Path
import re

this_dir = Path(os.path.abspath(__file__)).parent
bin_dir = os.path.join(str(this_dir), "bin")
test_data_path = os.path.join(str(this_dir), "test/device.hpp")

Language.build_library(
    output_path=os.path.join(bin_dir, "tree-sitter-cpp.so"),
    repo_paths=[os.path.join(str(this_dir), "tree-sitter-cpp")]
)

CPP_LANGUAGE = Language('./bin/tree-sitter-cpp.so', 'cpp')
parser = Parser()
parser.set_language(CPP_LANGUAGE)

data = ""

with open(test_data_path) as f:
    data = f.read()

tree = parser.parse(bytes(data, "utf8"))


node = tree.root_node

child_detected = False
for i in tree.root_node.children:
    # print(i.type, i.children[1].text)
    if i.type == "namespace_definition" and i.children[1].text.decode() == "Shell":
        child_detected = True
        node = i
if not child_detected:
    print("PyShell の namespace が定義されていません nampspace Shell に書いてください")
    exit()

child_detected = False
for i in node.children:
    if i.type == "declaration_list":
        child_detected = True
        node = i
if not child_detected:
    print("Shell 名前空間に関数が定義されていません")
    exit()

child_detected = False

comment: list[str] = []
func_list: list[list[str]] = []
num_buf = 0
for i in node.children:
    if i.type == "comment":
        print(i.text.decode())
        if "@brief" in i.text.decode():
            com_text = ""
            com_text = re.sub(
                '@brief ',
                '', re.search('@brief .+$', i.text.decode()).group())
            comment.append(com_text)
            if i.start_point[0] - num_buf > 1:
                comment = [com_text]
            num_buf = i.start_point[0]
    if i.type == "declaration":
        func_list.append(
            [i.children[1].children[0].text.decode(), '\n'.join(comment)])
        comment = []

print(func_list)
