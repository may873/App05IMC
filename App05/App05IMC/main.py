import flet as ft


def main(page: ft.Page):
    page.title=("CXalculadora de IMC")
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

    btncalcular=ft.ElevatedButton(text="Calcular", )
    btnLimpiar=ft.ElevatedButton(text="limpiar", )

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
