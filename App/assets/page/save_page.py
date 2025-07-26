from flet import *
from assets.database import *
from assets.components import *

class Save (Container):
    def __init__(self):
        super().__init__()

        self.content = Column(
            [
                Divider(
                    height=5,
                    color=Colors.TRANSPARENT
                ),

                Row(
                    [
                        Text(
                            'Salvar Trabalho',
                            size=35, 
                            color=Colors.BLACK, 
                            font_family='Power Calm', 
                            opacity=0.8
                        ),
                    ],alignment=MainAxisAlignment.CENTER
                ),

                Column(
                    [
                        Divider(
                            height=3,
                            color=Colors.TRANSPARENT
                        ),
                        Row(
                            [
                                CustomTextfield(label='Dia', width=84, max_length=2, inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER),
                                CustomTextfield(label='Mês', width=84, max_length=2, inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER),
                                CustomTextfield(label='Ano', width=84, max_length=4, inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER)
                            ],alignment=MainAxisAlignment.CENTER
                        ),

                        CustomTextfield(label='Hora inicial', inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER),

                        CustomTextfield(label='Hora final', inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER),
                        
                        CustomTextfield(label='Valor hora', inputfilter=NumbersOnlyInputFilter(), keyboardtype=KeyboardType.NUMBER),

                        CustomTextfield(label='contratante'),

                        CustomButton(self,),

                        Divider(height=40, color=Colors.TRANSPARENT)
                    ],horizontal_alignment='Center',
                      spacing=30,
                      width=350,
                      height=805,
                      scroll=ScrollMode.AUTO,
                )
            ]
        )
