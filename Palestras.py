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
                 "09h00 - 09h30",
                 "Boas Vindas NEon",
                 "O maior evento de inovação do Nordeste está no ar!",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 9, 30, 0),
                 "09h30 - 10h30",
                 "Liderança de equipes de tecnologia avançada",
                 "Convidado: Armando Lucrécio - Diretor de Gestão e Desenvolvimento de Produto da E Space",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 10, 30, 0),
                 "10h30 - 11h30",
                 "Marco Legal das Startups: Como as startups podem vender para o governo com a LC 182 e Lei de SandBox.",
                 "Convidados: Keicielle Oliveira - Coordenadora Geral de Gestão do conhecimento, tecnologia e prêmio "
                 "da Escola Nacional de Administração Pública ENAP Leonel Rodrigues - Analista de Negócios e Inovação "
                 "do Parque Tecnológico de Itaipú Cláudio Nascimento Co-Fundador Urbanicidades / Labgriô (Moderador) "
                 "Newton Cerezini - Diretor do Instituto de Gestão Pública de Pernambuco - IG Bruno Portela - "
                 "Procurador Federal, membro da Advocacia-Geral da União – AGU",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 11, 30, 0),
                 "11h30 - 12h30",
                 "Bioeconomia no contexto da economia circular: tendências e oportunidades para o Nordeste.",
                 "Convidados: Claudia Lima - Diretora Presidente do Instituto Tecnológico das Cadeias "
                 "Biossustentáveis (ITCBio) Uedja Tatyane Guimarães - Coordenadora de Pesquisa do Hub de Economia "
                 "Circular do Brasil Patrícia Villela Marino - CEO do Hub Civi-co Juliana Serafim - Consultora de ESG "
                 "do CESAR (Moderadora) Marcelo Pompemayer - Pesquisador e assessor de políticas públicas na "
                 "Universidade Federal Fluminense",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 14, 0, 0),
                 "14h00 - 15h00",
                 "Do zero aos 7 digitos.",
                 "Convidados: Abraão Sena - Sócio e Embaixador da Rocketseat Sérgio All - Co-Ceo e Chairman na Black "
                 "X Investimentos & Inovação da Conta Black Maiko Pinheiro - Partner da The BEC Bárbara Lopes - CEO "
                 "da Bensà Educação Empreendedora Afrocentrada e Bolsista no Programa Startup NE",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 15, 0, 0),
                 "15h00 - 16h00",
                 "Aceleração no Startup NE: colocando o Nordeste no mapa global da inovação.",
                 "Convidados: Marcus Buson - CEO da MOA Ventures Marília Diniz - Líder de projetos na Tropos Lab "
                 "Letícia Vitorino - Líder de projetos na Tropos Lab Vinicius Roman - Diretor técnico e Sócio da "
                 "Neoventures Marcel Boff - Sócio e Head de Aceleração de Startups da Semente Negócios Carlos Novinho "
                 "- CEO da Avati Aceleradora Rafael Ribeiro - CEO da Dealist Leonardo Mezzomo - CEO da Ventiur "
                 "Vanessa Pessoa - CEO da InoveNow",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 15, 0, 0),
                 "15h00 - 16h00",
                 "Aceleração no Startup NE: colocando o Nordeste no mapa global da inovação.",
                 "Convidados: Marcus Buson - CEO da MOA Ventures Marília Diniz - Líder de projetos na Tropos Lab "
                 "Letícia Vitorino - Líder de projetos na Tropos Lab Vinicius Roman - Diretor técnico e Sócio da "
                 "Neoventures Marcel Boff - Sócio e Head de Aceleração de Startups da Semente Negócios Carlos Novinho "
                 "- CEO da Avati Aceleradora Rafael Ribeiro - CEO da Dealist Leonardo Mezzomo - CEO da Ventiur "
                 "Vanessa Pessoa - CEO da InoveNow",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 16, 0, 0),
                 "16h00 - 17h00",
                 "Captação pré-seed e seed.",
                 "Convidados: Maitê Lourenço - CEO da BlackRocks Startups Rafael Ribeiro - CEO da Dealist Douglas "
                 "Vidal - Global Ecosystem Manager - The Black Entrepreneurs Club",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 17, 0, 0),
                 "17h00 - 18h00",
                 "Do Open call para a contratação de uma startup: Case VALE.",
                 "Convidados: Greyce Franzmann - Líder de projetos de inovação na Vale Crisley Pacheco - Líder dos "
                 "Hubs de Inovação na Vale",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 18, 0, 0),
                 "18h00 - 19h00",
                 "Zoho for Startups.",
                 "Convidados: Hellym Ribeiro - Gerente Zoho for Startups Brasil Kuppulakshmi Krishnamoorthy - Head "
                 "Global Zoho for Startups",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 1, 19, 0, 0),
                 "19h00 - 20h00",
                 "O Mundo muda. A palestra muda.",
                 "Convidados: Dado Schneider - Professor, Pesquisador e Escritor",
                 "Darcy Ribeiro")
    ],
    "Darcy Ribeiro - *02/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 2, 9, 0, 0),
                 "09h00 - 10h00",
                 "Desmistificando a bioeconomia: da teoria à estratégia de marca.",
                 "Raoni Cusma - Estrategista da Orolab",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 10, 0, 0),
                 "10h00 - 11h00",
                 "Green Nobel: United Heart Amazonia.",
                 "Convidados: Marcus Nobel - Presidente da UNITED EARTH SON OF CLAES NOBEL Sergio Lopes - Project "
                 "Sponsor and Global Stakeholder Relationship Manager Paulo Renato Cabral - Gerente de inovação do "
                 "Sebrae Nacional (Moderador) Alberto Traiger - Diretor de Produção e Business Affairs da LCTM "
                 "Brandbuilders Adriana Pacchielle - CEO da Pangaea Management Consulting e ex Diretora sênior do "
                 "Burger King Corporation nos EUA",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 11, 0, 0),
                 "11h00 - 12h00",
                 "O que os investidores pensam? Investimentos, startups de impacto e retorno.",
                 "Convidados: Monique Moraes - CEO da Su Causa, Mi Causa (Moderadora) Monique Evelle - Investidora na "
                 "Inventivos Angels Andreia Cardoso - Diretora Executiva da Somos Um",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 14, 0, 0),
                 "14h00 - 15h00",
                 "Desenvolvimento de parcerias locais para a promoção da ciência, inovação e empreendedorismo.",
                 "Convidado: Paulo Calçada - Vice-Presidente da Rede Européia de Smart Cities - OASC",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 15, 0, 0),
                 "15h00 - 16h00",
                 "Bancarização para todas e todos: conheça a história de um dos maiores cases de empreendedorismo do "
                 "Brasil, o Banco Digital Will Bank.",
                 "Convidados: Rodrigo Marques - CEO do Grupo COC São Luís Felipe Felix - CEO do Banco Will Bank",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 16, 0, 0),
                 "16h00 - 17h00",
                 "Bioeconomia: A economia que vai mudar o futuro dos negócios.",
                 "Convidados: Tatiane Simão - Idealizadora da empresa Somos Todos Amazônia Raoni Cusma - Estrategista "
                 "da Orolab Mayra Castro - Fundadora da InvestAmazonia Philippe Figueiredo - Gestor de projetos de "
                 "inovação no Sebrae Nacional (moderador)",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 17, 0, 0),
                 "17h00 - 18h00",
                 "Inovação, mudança e cidades.",
                 "Convidado: Edgar Andrade - Juntador de Gente e CEO Fab Lab Rec Head da Startupbootcamp no Brasil",
                 "Darcy Ribeiro"),
    ],
    "Terezinha Jansen - *02/06* 📅": [

    ]
}
