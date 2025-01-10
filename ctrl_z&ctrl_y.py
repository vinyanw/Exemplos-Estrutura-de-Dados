class UndoRedoStack:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def executarAcao(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear() 
        print(f'Ação "{action}" executada.')

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            print(f'Desfez a ação "{action}".')
        else:
            print("Nada para desfazer.")

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            print(f'Refez a ação "{action}".')
        else:
            print("Nada para refazer.")

undo_redo = UndoRedoStack()
undo_redo.executarAcao("Ação 1")
undo_redo.executarAcao("Ação 2")
undo_redo.executarAcao("Ação 3")

print("\nCtrl + z")
undo_redo.undo()
print("Ctrl + z")
undo_redo.undo() 
print("Ctrl + y")
undo_redo.redo()
undo_redo.executarAcao("Ação 4")
print("Ctrl + z")
undo_redo.undo() 
