import flet

class Authentication(flet.UserControl):
    def __init__(self):
        self.auth_box = flet.Container(
        	width=300,
        	height=300,
            bgcolor="#ffffff",
            animate=flet.animation.Animation(550, "easeOutBlack"),
            border_radius=10,
            padding=15,
        )

        super().__init__()

    def build(self):
        self.auth_box.content = flet.Column(
        	controls=[
        		flet.Text("Log In", color="black", size=24, weight="bold"),
        		flet.TextField(label="Username", color="black", text_size=16),
        		flet.TextField(label="Password", color="black", text_size=16),
        		flet.ElevatedButton(text="Log In", width=280, height=40),
        		flet.ElevatedButton(text="Register", width=280, height=40)
        	]
        )
        return self.auth_box


def main(page: flet.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.add(Authentication())
    page.update()


# Web testing
# flet.app(target=main, view=flet.WEB_BROWSER, port=9000)

# App testing
flet.app(target=main)