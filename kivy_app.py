from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class UserManagementApp(App):
    def build(self):
        # Initialize the layout
        layout = BoxLayout(orientation='vertical', padding=10)

        # Add a label with the app title
        title_label = Label(text='User Management', font_size=30)
        layout.add_widget(title_label)

        # Add a text input for the user's name
        self.name_input = TextInput(hint_text='Name', size_hint=(1, 0.2))
        layout.add_widget(self.name_input)

        # Add a text input for the user's age
        self.age_input = TextInput(hint_text='Age', size_hint=(1, 0.2), input_type='number')
        layout.add_widget(self.age_input)

        # Add a text input for the user's phone number
        self.phone_input = TextInput(hint_text='Phone Number', size_hint=(1, 0.2), input_type='number')
        layout.add_widget(self.phone_input)

        # Create a button for the drop-down menu
        dropdown_button = Button(text='Select an option', size_hint=(1, 0.2))
        dropdown_button.bind(on_release=self.show_dropdown)
        layout.add_widget(dropdown_button)

        # Create the drop-down menu with options to create or delete a user
        dropdown = DropDown()
        create_user_button = Button(text='Create a user', size_hint_y=None, height=40)
        create_user_button.bind(on_release=lambda button: self.create_user(self.name_input.text, self.age_input.text, self.phone_input.text))
        dropdown.add_widget(create_user_button)
        delete_user_button = Button(text='Delete a user', size_hint_y=None, height=40)
        delete_user_button.bind(on_release=lambda button: self.delete_user(self.name_input.text))
        dropdown.add_widget(delete_user_button)

        return layout

    def show_dropdown(self, button):
        # Show the drop-down menu when the button is pressed
        dropdown = DropDown()
        create_user_button = Button(text='Create a user', size_hint_y=None, height=40)
        create_user_button.bind(on_release=lambda button: self.create_user(self.name_input.text, self.age_input.text, self.phone_input.text))
        dropdown.add_widget(create_user_button)
        delete_user_button = Button(text='Delete a user', size_hint_y=None, height=40)
        delete_user_button.bind(on_release=lambda button: self.delete_user(self.name_input.text))
        dropdown.add_widget(delete_user_button)
        dropdown.open(button)

    def create_user(self, name, age, phone):
        # Store the user's name, age, and phone number in a text file
        with open('users.txt', 'a') as f:
            f.write(f'{name}, {age}, {phone}\n')

    def delete_user(self, name):
        # Remove the user's name, age, and phone number from the text file
        with open('users.txt', 'r') as f:
            lines = f.readlines()
        with open('users.txt', 'w') as f:
            for line in lines:
                if not line.startswith(name + ','):
                    f.write(line)



if __name__ == '__main__':
    UserManagementApp().run()
