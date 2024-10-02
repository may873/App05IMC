import flet as ft

#funcion para calcular el IMC
def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)#62
        altura=float(txtAltura.value)#1.64
        imc=peso/(altura**2)#62/2.6896
        lblIMC.value=f"tu IMC es de: {imc:.2f}"#23.05
        page.update()
        
        #funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        #Validacion de IMC
        if imc<18.5:
            dialog=ft.AlertDialog(
            title=ft.Text("Bajo peso "),
            content=ft.Text("Tu IMC indica que tienes bajo peso"),
            actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar_dialogo())
                ],
            )
        elif imc>=18.5 and imc<24.9:
            dialog=ft.AlertDialog(
                title=ft.Text("Peso Normal"),
                content=ft.Text("Tu IMC indica que tienes un peso normal"),
                actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e: cerrar_dialogo())
                ],
            )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
                title=ft.Text("Sobrepeso"),
                content=ft.Text("Tu IMC indica que tienes Sobrepeso"),
                actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar_dialogo())
                ],
            )
        else:
            dialog=ft.AlertDialog(
                title=ft.Text("Obesidad "),
                content=ft.Text("Tu IMC indica que tienes Obesidad"),
                actions=[
                    ft.TextButton(text="Cerrar",on_click=lambda e:cerrar_dialogo())
                ],
            )
        page.dialog=dialog
        page.dialog.open=True
        page.update()  
        
    except ValueError:
        page.dialog.open= False
        page.update()

#funcion principal es donde se agregan el color,titulo,botones,cuadros de texto,funciones etc       
def main(page: ft.Page):
    page.title=("Calculadora de IMC")
    page.bgcolor="Blue"
    
    txtPeso=ft.TextField(label="ingresa tu peso en kg")
    txtAltura=ft.TextField(label="ingresa tu altura en metros")
    lblIMC=ft.Text("Tu IMC es de: ")
    
    IMG=ft.Image (
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    #funcion para que llama ala funcion para calcular el IMC
    def on_calcular(e):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        page.update()
            
     #Funcion para limpiar los cuadros de texto 
    def limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value=""
        page.update()
        

    btncalcular=ft.ElevatedButton("Calcular",
                                  on_click=lambda e:on_calcular(e))
    btnLimpiar=ft.ElevatedButton(text="limpiar",on_click=lambda e:limpiar(e))

    page.add(
        ft.Column(
            controls=[
                txtPeso,txtAltura,lblIMC
                ],alignment="CENTER"),
        ft.Row(
            controls=[
                IMG
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btncalcular,btnLimpiar
            ],alignment="CENTER")
    )

ft.app(target=main,view=ft.AppView.WEB_BROWSER)
