from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.toast import androidtoast as at


class MainApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")
        
    def alert(self):
        pass
        
if __name__ == "__main__":
    MainApp().run()
