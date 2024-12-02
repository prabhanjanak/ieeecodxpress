from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ExtractDataApp(App):
    def build(self):
        # Initialize the layout
        layout = BoxLayout(orientation='vertical', padding=10)

        # Add a label with the app title
        title_label = Label(text='Extract Data from Text File', font_size=30)
        layout.add_widget(title_label)

        # Read the data from the text file
        with open('users.txt', 'r') as f:
            data = f.read()

        # Add a label with the extracted data
        data_label = Label(text=data, font_size=20)
        layout.add_widget(data_label)

        return layout

if __name__ == '__main__':
    ExtractDataApp().run()
