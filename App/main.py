from flet import *
from assets.page.save_page import *
from assets.page.home_page import *
from assets.database import *
from assets.components import *

def main(page: Page):
    page.title = 'Trabalhos'
    page.horizontal_alignment = 'Center'
    page.window.width = 390
    page.window.height = 844
    page.padding = 0
    page.spacing = 12
    page.window.maximizable = False
    page.window.resizable = False
    page.fonts = {
        'Brown Cake' : 'fonts/Brown Cake.otf',
        'Power Calm' : 'fonts/Power Calm.otf'
                 }
    
    page.theme_mode = ThemeMode.LIGHT
    page.theme = Theme(
        scrollbar_theme=ScrollbarTheme(
            thumb_color={
                ControlState.HOVERED: Colors.BLUE_300,
                ControlState.DEFAULT: Colors.BLUE_100,
            },
            thickness=6,
            radius=5,
            main_axis_margin=7,
            cross_axis_margin=7,
        ),
        font_family='Power Calm'
    )
    

    def save(e):        
        main_container.content.controls[1].content = Save()
        main_container.update()

    def home(e, page):
        main_container.content.controls[1].content = Home(page)
        main_container.update()


    appbar = Container(
        bgcolor=Colors.BLUE_500,
        width=page.width,
        height=80,
        border_radius=border_radius.only(bottom_left=15, bottom_right=15),
        content=Row(
            [
                IconButton(
                    scale=1,
                    opacity=1,
                    icon=Icons.ADD, 
                    icon_color='White', 
                    icon_size=40, 
                    on_click=save,
                    ),

                Text(
                    'TRABALHOS', 
                    size=40, 
                    color=Colors.WHITE, 
                    font_family='Power Calm'
                    ),

                IconButton(
                    scale=1,
                    opacity=1,
                    icon=Icons.HOME, 
                    icon_color='White', 
                    icon_size=35, 
                    on_click=lambda e: home(e, page),
                    )

            ],alignment=MainAxisAlignment.CENTER
        ),
        alignment=alignment.center
    )

    content = Container(
        height=805,
        width=350,
        bgcolor=Colors.WHITE,
        border_radius=10,
        content=Home(page)
    )

    main_container = Container(
        height=page.height,
        width=page.width,
        gradient=LinearGradient(
            colors=[Colors.BLUE_500, Colors.BLUE_300],
            begin=alignment.top_center,
            end=alignment.bottom_center
        ),
        content=Column(
            [
                appbar,
                content
            ],horizontal_alignment='Center'
        )
    )

    page.add(main_container)
    page.on_close = lambda: db.close_connection()
    
if __name__ == '__main__':
    app(target=main)
