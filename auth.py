import flet


class Authentication(flet.UserControl):
    def __init__(self):
        self.auth_box = flet.Container(
            width="400",
            bgcolor="secondary",
            animate=flet.animation.Animation(550, "easeOutBlack"),
            alignment=flet.alignment.center,
            border_radius=10,
            padding=20,
            shadow=flet.BoxShadow(spread_radius=1, blur_radius=5),
        )

        self.login_form = flet.Column(
            controls=[
                flet.Text("Log In", size=24, weight="bold"),
                flet.TextField(label="Username", text_size=16),
                flet.TextField(label="Password", text_size=16),
                flet.Row(
                    controls=[
                        flet.ElevatedButton(
                            on_click=self.show_login, text="Log In", expand=2
                        ),
                        flet.ElevatedButton(
                            on_click=self.show_register, text="Register", expand=1
                        ),
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                ),
            ]
        )

        self.register_form = flet.Column(
            controls=[
                flet.Text("Register", size=24, weight="bold"),
                flet.TextField(label="Username", text_size=16),
                flet.TextField(label="Password", text_size=16),
                flet.TextField(label="Confirm password", text_size=16),
                flet.Row(
                    controls=[
                        flet.ElevatedButton(
                            on_click=self.show_register, text="Create Account", expand=2
                        ),
                        flet.ElevatedButton(
                            on_click=self.show_login, text="Back", expand=1
                        ),
                    ],
                    alignment=flet.MainAxisAlignment.CENTER,
                ),
            ]
        )

        super().__init__()

    def build(self):
        self.auth_box.content = self.login_form
        return self.auth_box

    def show_register(self, e):
        self.auth_box.content = self.register_form
        self.auth_box.update()

    def show_login(self, e):
        self.auth_box.content = self.login_form
        self.auth_box.update()




def main(page: flet.Page):
    page.theme = flet.Theme(
        color_scheme=flet.ColorScheme(
            primary="#7289da",
            on_primary="white",
            primary_container="#424549",
            secondary="#282b30",
            on_secondary="#5865f2",
        ),
    )
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(Authentication())
    page.update()


# Web testing
# flet.app(target=main, view=flet.WEB_BROWSER, port=9000)

# App testing
flet.app(target=main)
