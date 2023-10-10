from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper
from kivymd.uix.dialog import MDDialog

username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x: None
    width:300
"""


class DemoApp(MDApp):
    # def build(self):
    # label = MDLabel(text='Hello World',
    #                 halign='center',
    #                 theme_text_color='Custom',
    #                 text_color=(236/255.0, 98/255.0, 82/255.0, 1),
    #                 font_style='Caption')
    #
    # icon_label = MDIcon(icon='library-video',
    #                     halign='center')
    #
    # return icon_label  // Here ends the second video.
    ###############################################################################

    # def build(self):
    #     screen = Screen()  # application window on which you can add stuff
    #     btn_flat = MDRectangleFlatButton(text='Hello World', pos_hint={'center_x': 0.5, 'center_y': 0.5})
    #     icon_btn = MDFloatingActionButton(icon='language-python', pos_hint={'center_x': 0.5, 'center_y': 0.5})
    #     # screen.add_widget(btn_flat)
    #     screen.add_widget(icon_btn)
    #     return screen

    ############################################################################### Video 3 ended here
    # def build(self):
    #     self.theme_cls.primary_palette = "Green"
    #     self.theme_cls.primary_hue = "A700"
    #     self.theme_cls.theme_style = "Dark"
    #     screen = Screen()
    #     btn_flat = MDRectangleFlatButton(text='Hello World',
    #                                      pos_hint={'center_x': 0.5, 'center_y': 0.5})
    #
    #     screen.add_widget(btn_flat)
    #     return screen
    ############################################################################### Video 4 ended here
    # def build(self):
    #     screen = Screen()
    #     self.theme_cls.primary_palette = "Green"
    #     # username = MDTextField(text='Enter username',
    #     #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #     #                        size_hint_x = None, width=300)
    #     username = Builder.load_string(username_helper)
    #     screen.add_widget(username)
    #     return screen
    ############################################################################### Video 5 ended here
    # def build(self):
    #     screen = Screen()
    #     self.theme_cls.primary_palette = "Green"
    #     # username = MDTextField(text='Enter username',
    #     #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
    #     #                        size_hint_x = None, width=300)
    #     button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
    #                                    on_release=self.show_data)
    #     self.username = Builder.load_string(username_helper)
    #     screen.add_widget(self.username)
    #     screen.add_widget(button)
    #     return screen
    #
    # def show_data(self, obj):
    #     print(self.username.text)

    ############################################################################### Video 6 ended here
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                        size_hint_x = None, width=300)
        button = MDRectangleFlatButton(text='Show', pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + 'does not exist'
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username Check', text=check_string, buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()
    ############################################################################### Video 7 ended here

DemoApp().run()
