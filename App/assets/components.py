from tkinter import HIDDEN
from flet import *
from assets.database import *

def update_listview(page):
        works = db.get_all_works()
        items = ListView(expand=1, spacing=10, padding=15)

        for work in works:
            items.controls.append(
                CustomContainer(
                    id=work[0], data=work[1], hora_inicial=work[2], 
                    hora_final=work[3], minutos_trabalhados=work[4], valor_hora=work[5], 
                    valor_total=work[6], contratante=work[7], page=page
                )
            )
        return items

def focus_effect(e, color):
    control = e.control

    control.scale = 1.05
    control.opacity = 0.95
    control.border_color = color
    control.update()

def blur_effect(e, color):
    control = e.control

    control.scale = 1  
    control.opacity = 1
    control.border_color = color
    control.update()

def hover_effect(e):
    control = e.control

    if e.data == "true":
        control.scale = 1.02
        control.opacity = 0.95
        control.shadow = BoxShadow(
            blur_radius=2,
            color=Colors.BLACK
        )

    else:  
        control.scale = 1
        control.opacity = 1

    control.update()


class CustomButton (ElevatedButton):
    def __init__(self, save_instance):
        super().__init__()

        self.save_instance = save_instance
        self.text = 'Salvar'
        self.width = 200
        self.scale = 1
        self.height = 40
        self.style = ButtonStyle(
            text_style=TextStyle(color=Colors.WHITE, font_family='Power Calm', size=20),
            bgcolor=Colors.BLUE_100
        )
        self.on_click = self.save
        self.on_hover = hover_effect

    def save(self, e):
            all_filled = True
            value = []

            for control in self.save_instance.content.controls[2].controls:
                if isinstance(control, Row):
                    for sub_control in control.controls:
                        if isinstance(sub_control, CustomTextfield):
                            if len(sub_control.value.strip()) == 0:
                                sub_control.error_text = 'Preencha este campo'
                                all_filled = False

                            else:
                                value.append(sub_control.value)
                                sub_control.error_text = None 

                elif isinstance(control, CustomTextfield):
                    if len(control.value.strip()) == 0:
                        control.error_text = 'Preencha este campo'
                        all_filled = False

                    else:
                        value.append(control.value)
                        control.error_text = None

            self.save_instance.page.update()

            if all_filled:
                for control in self.save_instance.content.controls[2].controls:
                    if isinstance(control, CustomTextfield):
                        control.value = ''

                    elif isinstance(control, Row):
                        for sub_control in control.controls:
                            if isinstance(sub_control, CustomTextfield):
                                sub_control.value = ''

                self.save_instance.page.update()

                data = f'{value[0]}/{value[1]}/{value[2]}'
                hora_inicial = int(value[3])
                hora_final = int(value[4])
                valor_hora = int(value[5])
                contratante = value[6]
                valor_total, minutos = self.horímetro(hora_inicial, hora_final, valor_hora)

                db.save_work(
                        data=data,
                        hora_inicial=hora_inicial, 
                        hora_final=hora_final, 
                        minutos_trabalhados=minutos,
                        valor_hora=valor_hora,
                        valor_total=valor_total,
                        contratante=contratante
                    )

    def horímetro(self, hora_inicial: int, hora_final: int, valor_hora: float):
        diferenca_horimetro = hora_final - hora_inicial
    
        minutos = (diferenca_horimetro % 10) * 6

        minutos_totais = (diferenca_horimetro // 10) * 60 + minutos 

        valor_total = (minutos_totais / 60) * valor_hora 

        return round(valor_total, 2), minutos_totais
            

class CustomTextfield (TextField):
    def __init__(self, label=None, width=270, 
                 max_length=None, inputfilter=None, 
                 keyboardtype=KeyboardType.TEXT):
        super().__init__()

        self.label = label
        self.width = width
        self.max_length = max_length
        self.color = Colors.BLACK
        self.border_color = Colors.BLUE_100
        self.border_radius = 7
        self.border_width = 2
        self.cursor_height = 13
        self.scale = 1
        self.opacity = 1
        self.autocorrect = True
        self.enable_suggestions = True
        self.label_style = TextStyle(font_family='Power Calm')
        self.text_style = TextStyle(color=Colors.BLUE, font_family='Power Calm')  
        self.keyboard_type = keyboardtype
        self.input_filter = inputfilter
        self.error_style = TextStyle(
            font_family='Power Calm'
        )
        self.animate_scale = Animation(500, AnimationCurve.DECELERATE)
        self.animate_opacity = Animation(500, AnimationCurve.DECELERATE)

        self.on_focus = lambda e: focus_effect(e, color=Colors.BLUE_400)
        self.on_blur = lambda e: blur_effect(e, color=Colors.BLUE_100)


class CustomContainer (Container):
    def __init__(self, id, data, hora_inicial, 
                 hora_final, minutos_trabalhados, valor_hora, 
                 valor_total, contratante, page):
        super().__init__()

        self.page = page
        self.id = id
        self.data = data
        self.hora_inicial = hora_inicial
        self.hora_final = hora_final
        self.minutos_trabalhados = minutos_trabalhados
        self.valor_hora = valor_hora
        self.valor_total = valor_total
        self.contratante = contratante

        self.height = 80
        self.width = 300
        self.scale = 1
        self.opacity = 1
        self.bgcolor = Colors.BLUE_300
        self.border_radius = 8
        self.shadow = BoxShadow(
            blur_radius=1,
            color=Colors.BLACK)
        self.alignment = alignment.center
        self.on_hover = hover_effect
        self.on_click = self.info
        self.animate_scale = Animation(400, AnimationCurve.DECELERATE)
        self.animate_opacity = Animation(400, AnimationCurve.DECELERATE)
        self.animate = Animation(500, AnimationCurve.DECELERATE)
        self.content = Text(
            value=f"Data: {self.data} - Valor Hora: R${self.valor_hora} - Contratante: {str(self.contratante).split()[0]}",
            size=19,
            font_family='Power Calm',
            color=Colors.WHITE
        )

    def info (self, e):
        if self.height < 260:
            self.height = 260
            self.scale = 1.03
            self.opacity = 0.95
            self.content = Column(
                [
                    Text(
                        value=f'''Data: {self.data}
Hora Inicial: {self.hora_inicial}
Hora Final: {self.hora_final}
Total horas: {f'{self.minprhora(self.minutos_trabalhados)[0]} horas e {self.minprhora(self.minutos_trabalhados)[1]} minutos' }
Valor Hora: R${self.valor_hora}
Valor total: R${self.valor_total}
Contratante: {self.contratante}''',
                        size=20,
                        font_family='Power Calm',
                        color=Colors.WHITE
                    ),

                    Row(
                        [
                            ElevatedButton(
                                text='Excluir',
                                width=90,
                                height=30,
                                scale=1,
                                style= ButtonStyle(
                                    text_style=TextStyle(color=Colors.WHITE, font_family='Power Calm', size=15),
                                    bgcolor=Colors.RED_200
                                ),
                                on_hover=hover_effect,
                                on_click= lambda e :self.alert(self.id, self.page)
                            )
                        ],alignment=MainAxisAlignment.CENTER
                    )
                ],scroll=ScrollMode.HIDDEN
            )
            self.alignment = alignment.center_left

        else:
            self.height = 80
            self.scale = 1
            self.opacity = 1
            self.content = Text(
                value=f"Data: {self.data} - Valor Hora: R${self.valor_hora} - Contratante: {str(self.contratante).split()[0]}",
                size=19,
                font_family='Power Calm',
                color=Colors.WHITE
            )
            self.alignment = alignment.center
        self.update()

    def minprhora(self, minutos):
        horas = minutos // 60
        minutos = round((minutos / 60 - horas) * 60)

        if minutos >= 60:
            horas += 1
            minutos = 0

        return horas, minutos
    
    def alert (self, id, page):

        def conform_delete(e):
            db.dell_work(id)
            page.close(alert)
            update_listview(page)
            
        def cancel_delete(e):
            page.close(alert)

        alert = AlertDialog(
            title=Text('Tem certeza?', font_family='Power Calm'),
            content=Text('Essa ação não pode ser desfeita.', font_family='Power Calm', size=15),
            bgcolor=Colors.BLUE_100,
            actions=[
                TextButton(content=Text('Camcelar', font_family='Power Calm'), on_click=cancel_delete),
                TextButton(content=Text('Excluir', font_family='Power Calm', color=Colors.RED), on_click=conform_delete)
            ]
        )
        
        page.open(alert)
        alert.open = True
        page.update(self)
