class Editor:

    functionality_list=["open","save","edit"]

    def get_context(self):
        return self.functionality_list

    def print_funtions(self):
        print(self.get_context())

class Vscode(Editor):
# debug, execute

    def get_context(self):
        self.context=super().get_context()#["open", "save", "edit"]
        self.context.append("debug")
        self.context.append("execute")
        return self.context

ch=Vscode()
ch.print_funtions()

