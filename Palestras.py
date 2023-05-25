import datetime


class Palestra:
    def __init__(self, date_time: datetime, date_time_text: str, headline: str, text: str, local: str):
        self.date_time = date_time
        self.date_time_text = date_time_text
        self.headline = headline
        self.text = text
        self.local = local

    def __str__(self):
        return "*{}*\n*{}*\n\n{}".format(self.date_time_text, self.headline, self.text)


palestras = {
    "Darcy Ribeiro - *01/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 1, 9, 0, 0),
                 "9h - 9h30",
                 "Boas Vindas NEon",
                 "O maior evento de inovação do Nordeste está no ar!",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 9, 30, 0),
                 "9h30 - 10h00",
                 "Liderança de equipes de tecnologia avançada",
                 "Convidado: Armando Lucrécio - Diretor de Gestão e Desenvolvimento de Produto da E Space",
                 "Darcy Ribeiro")
    ],
    # "Darcy Ribeiro - *02/06* 📅": [
    #
    # ]
}
