import flet as ft

def calcular_imc(txtPeso,txtAltura,lblIMC,page):
    try:
        peso=float(txtPeso.value)
        altura=float(txtAltura.value)
        imc=peso/(altura**2)
        lblIMC.value=f"tu IMC es de: {imc:.2f}"
        page.update()
        
        #funcion para cerrar el cuadro de dialogo
        def cerrar_dialogo():
            page.dialog.open=False
            page.update()
        #Validacion de IMC
        if imc<18.5:
            dialog=ft.AlertDialog(
            title="Bajo peso ",
            content="Tu IMC indica que tienes bajo peso",
            accions=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ],
            )
        elif imc>=18.5 and imc<24.9:
            dialog=ft.AlertDialog(
                title="Peso Normal",
                content="Tu IMC indica que tienes un peso normal",
                accioms=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ],
            )
        elif imc>=25 and imc<30:
            dialog=ft.AlertDialog(
                title="Sobrepeso",
                content="Tu IMC indica que tienes Obesidad",
                accioms=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ],
            )
        else:
            dialog=ft.AlertDialog(
                title="Obesidad ",
                content="Tu IMC indica que tienes Sobrepeso",
                accioms=[
                    ft.TextButton(text="Cerrar",on_click=cerrar_dialogo)
                ],
            )
        page.dialog=dialog
        page.dialog.open=False
        page.update()  
    except ValueError:
        page.dialog.open= False
        page.update()
        



        
        

def main(page: ft.Page):
    page.title=("Calculadora de IMC")
    page.bgcolor="Blue"
    
    txtPeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("Tu IMC es de: ")
    
    IMG=ft.Image (
        src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def on_calcular(e):
        calcular_imc(txtPeso,txtAltura,lblIMC,page)
        
    def limpiar(e):
        txtPeso.value=""
        txtAltura.value=""
        lblIMC.value=""
        page.update()
        

    btncalcular=ft.ElevatedButton(text="Calcular",on_click=on_calcular() )
    btnLimpiar=ft.ElevatedButton(text="limpiar",on_click=limpiar)

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
