from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit
import sys
from pathlib import Path

app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = QWidget()
window.show()  
textEdit = QTextEdit()


fork_string   = '├──'
corner_string = '└──'
wall_string   = '│  '
space_string  = '   '

def drawtree(path, seen, head='', tail=''):
    if path.resolve() not in seen:
        yield head + path.name
        seen.add(path.resolve())
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                yield from drawtree(entry, seen, tail + fork_string, tail + wall_string)
            else:
                yield from drawtree(entry, seen, tail + corner_string, tail + space_string)

def tree(my_path='.'):
    for line in drawtree(Path(my_path), set()):
        print(line)

path = input("Enter path:")
tree(path)
textEdit.append(tree(path))
app.exec()
