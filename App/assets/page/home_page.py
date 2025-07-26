from flet import *
from assets.database import *
from assets.components import *

class Home (Container):
    def __init__(self, page):
        super().__init__()

        self.page = page
        items = update_listview(page)

        self.content = Column(
            [
                Divider(
                    height=5,
                    color=Colors.WHITE
                ),

                Row(
                    [
                        Text(
                            'Trabalhos',
                            size=35, 
                            color=Colors.BLACK, 
                            font_family='Power Calm', 
                            opacity=0.8
                        ),
                    ],alignment=MainAxisAlignment.CENTER
                ),

                Divider(
                    height=10,
                    color=Colors.WHITE,
                ),

                items
            ]
        )
