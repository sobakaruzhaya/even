#pip install flet pandas
import flet as ft
from flet import Page, Text, Dropdown, ElevatedButton, dropdown, Container
import pandas as pd

def main(page: Page):
    page.window_height = 640
    page.window_width = 600
    page.fonts = {
        "Sofia Sans Semi" : "/fonts/SofiaSansSemiCondensed-BoldItalic.ttf"
    }




    title_text = Container(
        content= Text(value="ЭВИН",color="black", 
                      style=ft.TextThemeStyle.TITLE_LARGE, 
                      font_family= "Sofia Sans Semi",
                      text_align=ft.TextAlign.CENTER, size=70),
        alignment= ft.alignment.top_center,
        width= 600,
        height=200,
    )
    

    pick_region_text = Text(value="Выберете интересующее вложение:",size=24)

    pick_region_dropdown = Dropdown(
        width=600,
        label="Вложение",
        hint_text="Выбрать вложение",
        options=[
            dropdown.Option("134.1000.01 ДГУ. Оплата за электроэнергию по тарифам Океанский пр-т, 34"),
            dropdown.Option("134.1000.01 Анадырь Оплата потребления электроэнергии ул.Колхозная 32б(склад)"),
            dropdown.Option("134.1000.02 Столовая ХБ Оплата за отопление по тарифам ул. М.Амурского, 42"),
        ],
    )



    def pick_region_submit_button_clicked(e):
        def show_menu(e):
            page.remove(title_pick_region, rashodu_pred_text, chart,back_submit_button)
            page.add(title_text, pick_region_text,pick_region_dropdown, pick_region_submit_button)
            page.update()
        page.remove(title_text, pick_region_text,pick_region_dropdown, pick_region_submit_button)

        if f"{pick_region_dropdown.value}" == "134.1000.01 ДГУ. Оплата за электроэнергию по тарифам Океанский пр-т, 34":
            nedvizhka = 1
        elif f"{pick_region_dropdown.value}" == "134.1000.01 Анадырь Оплата потребления электроэнергии ул.Колхозная 32б(склад)":
            nedvizhka = 2
        elif f"{pick_region_dropdown.value}" == "134.1000.02 Столовая ХБ Оплата за отопление по тарифам ул. М.Амурского, 42":
            nedvizhka = 3
        
        df = pd.read_csv("output.csv",encoding="windows-1251",delimiter=";")

        feb = df.at[nedvizhka-1+2*(nedvizhka-1), 'Отнесено']
        mar = df.at[nedvizhka+2*(nedvizhka-1), 'Отнесено']
        apr = df.at[nedvizhka+1+2*(nedvizhka-1), 'Отнесено']

        typen = df.at[nedvizhka+2*(nedvizhka-1), 'Наименование вида расходов']

        title_pick_region = Text(value=f"{pick_region_dropdown.value}")
        rashodu_pred_text = Text(f"Тип расходов: {typen}")

        chart = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=0,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=feb,
                            width=40,
                            color=ft.colors.AMBER,
                            tooltip=f"{feb}",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=1,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=mar,
                            width=40,
                            color=ft.colors.BLUE,
                            tooltip=f"{mar}",
                            border_radius=0,
                        ),
                    ],
                ),
                ft.BarChartGroup(
                    x=2,
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=apr,
                            width=40,
                            color=ft.colors.RED,
                            tooltip=f"{apr}",
                            border_radius=0,
                        ),
                    ],
                ),
            ],
            border=ft.border.all(1, ft.colors.GREY_400),
            left_axis=ft.ChartAxis(
                labels_size=40, title=ft.Text("Отнесено"), title_size=40
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        value=0, label=ft.Container(ft.Text("Февраль"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=1, label=ft.Container(ft.Text("Март"), padding=10)
                    ),
                    ft.ChartAxisLabel(
                        value=2, label=ft.Container(ft.Text("Апрель"), padding=10)
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=ft.colors.GREY_300, width=1, dash_pattern=[3, 3]
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, ft.colors.GREY_300),
            max_y=1000,
            interactive=True,
            expand=True,
        )

        back_submit_button = ElevatedButton(text="Назад",on_click=show_menu)

        page.add(title_pick_region, rashodu_pred_text, chart,back_submit_button)


        page.update




    pick_region_submit_button = ElevatedButton(text="Выбрать",on_click=pick_region_submit_button_clicked)


    page.add(title_text, pick_region_text,pick_region_dropdown, pick_region_submit_button)


 

ft.app(target=main, assets_dir="assets")