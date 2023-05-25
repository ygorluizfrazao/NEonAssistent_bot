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
        Palestra(datetime.datetime(2023, 6, 2, 18, 0, 0),
                 "18h00 - 19h00",
                 "Como captar investimento: Diferença entre investimento anjo, fundo, crowdfunding e equity.",
                 "Convidado: João Kepler - CEO da Bossa Nova Investimentos",
                 "Darcy Ribeiro"),
        Palestra(datetime.datetime(2023, 6, 2, 19, 0, 0),
                 "19h00 - 20h00",
                 "Encerramento NEon: NEon veio para ficar! (anúncio do evento em 2024)",
                 "Convidados: Diretoria e Autoridades",
                 "Darcy Ribeiro")
    ],
    "Terezinha Jansen - *01/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 1, 10, 30, 0),
                 "10h30 - 11h30",
                 "Transformação digital",
                 "Convidado: Felipe Cabral - Gerente de Marketing de Produtos para Infraestrutura da Dell",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 11, 30, 0),
                 "11h30 - 12h30",
                 "Se quer ir longe, vá em grupo: aprendizados após 1 ano de M&A.",
                 "Convidado: Rômulo Martins - Diretor Geral da Unidade de Negócios de Educação Corporativa da Gupy",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 14, 00, 0),
                 "14h00 - 15h00",
                 "Job to be done: Como as startups podem identificar e atender as necessidades não atendidas dos "
                 "consumidores, criando soluções que ofereçam valor?",
                 "Convidados: Mayara Pimentel - CEO da Transforma Nayana Cambraia - Gerente de portfólio na NESsT "
                 "Polyanna Cintra - Co-fundadora do Lab Griô (Moderadora) Dani Estevam - Coordenadora de Governança e "
                 "Articulação do Ecossistema de Inovação CDT/UNB",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 15, 00, 0),
                 "15h00 - 16h00",
                 "Websérie Inova Amazônia - Negócios sustentáveis e lucrativos",
                 "Convidado: Philippe Figueiredo - Gestor de projetos de inovação no Sebrae Nacional (moderador)",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 16, 00, 0),
                 "16h00 - 17h00",
                 "Nova Economia: Modelos de negócios inovadores e exponenciais.",
                 "Convidado: Alexandre Uehara - Head de Inovação - Innov8",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 17, 00, 0),
                 "17h00 - 18h00",
                 "Cultura Maker: O potencial da cultura maker nas empresas.",
                 "Convidado: Edgar Andrade - Juntador de Gente e CEO FabLab Recife Head da Startupbootcamp no Brasil",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 1, 18, 00, 0),
                 "18h00 - 19h00",
                 "Do zero ao exit: Acredite no impossível.",
                 "Convidado: Marcus Varandas - Founder da Menew",
                 "Terezinha Jansen")
    ],
    "Terezinha Jansen - *02/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 2, 10, 00, 0),
                 "10h00 - 11h00",
                 "Websérie Inova Amazônia - Negócios sustentáveis e lucrativos",
                 "Convidado: Felipe Cabral - Gerente de Marketing de Produtos para Infraestrutura da Dell",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 2, 11, 00, 0),
                 "11h00 - 12h00",
                 "Cidades Inteligentes: Como o Marco Legal das Startups vem desenvolvendo cidades brasileiras através "
                 "da inovação aberta.",
                 "Convidado: Hideraldo Almeida - Vice-Presidente da Rede Brasileira de Cidades Inteligentes e Humanas",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 2, 14, 00, 0),
                 "14h00 - 15h00",
                 "A Inovação como diferencial segundo uma visão Sistêmica",
                 "Convidado: André Rolim - Diretor de RH da Alcoa",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 2, 15, 00, 0),
                 "15h00 - 16h00",
                 "Regulamentação: um obstáculo ou uma oportunidade para empresas inovadoras.",
                 "Convidado: Rafael Rebelo - Especialista em em Inteligência Operacional na Remessa Online",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 2, 16, 00, 0),
                 "16h00 - 17h00",
                 "A ambivalência da Inteligência Artificial: mudar ou destruir o mundo? Qual é o nosso papel?",
                 "Convidado: Paulo Calçada - Vice Presidente da Rede Européia de Smart Cities - OASC",
                 "Terezinha Jansen"),
        Palestra(datetime.datetime(2023, 6, 2, 17, 00, 0),
                 "17h00 - 18h00",
                 "Desenvolver produtos de IOT",
                 "Convidado: Armando Lucrécio - Diretor de Gestão e Desenvolvimento de Produto da E Space",
                 "Terezinha Jansen")
    ],
    "Espaço João Berto - *01/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 1, 10, 30, 0),
                 "10h30 - 11h00",
                 "Caminhos para o sucesso das mulheres no empreendedorismo",
                 "Convidado: Lilian Natal - Diretora de Marketing e Relações com Investidores da Bossa Nova "
                 "Investimentos",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 11, 00, 0),
                 "11h00 - 11h30",
                 "Como a conexão com o ecossistema de inovação e startups pode ser um caminho pro Open Innovation em "
                 "empresas muito tradicionais",
                 "Convidado: Luiza Luth - Consultora de Inovação Sênior da Andrade Gutierrez S.A",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 11, 30, 0),
                 "11h30 - 12h30",
                 "Educação Empreendedora é o futuro - Despertando o comportamento empreeendedor",
                 "Convidado: Alexandre Mori - MVPlay",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 14, 00, 0),
                 "14h00 - 15h00",
                 "O que são ecossistemas de inovação e quais oportunidades eles trazem para meu negócio",
                 "Convidados: Rodrigo Paolilo - CEO do Grupo Rede+ Cláudio Marinho - CEO da Porto Marinho Diógenes "
                 "Júnior - Gerente do Sebrae de Balsas e Representante do Ecossistema de Inovação de Balsas Içara "
                 "Moreira Bajadares - CEO do Hub Aprimore e Representante do Ecossistema de Inovação de Imperatriz",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 15, 00, 0),
                 "15h00 - 16h00",
                 "Pitch Perfect",
                 "Convidado: Alexandre Uehara - Head de Inovação - Innov8",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 16, 00, 0),
                 "16h00 - 17h00",
                 "O segredo dos unicórnios! Como construir startups de sucesso.",
                 "Convidado: Leandro Piazza - 49Educação",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 1, 17, 00, 0),
                 "17h00 - 18h00",
                 "Ainda temos tempo? Startups de impacto e desafios socioambientais",
                 "Convidados: Jair Mendes (moderador) - PonteAPonte Saville Alves (moderador) - Solos Ítalo Carvalho "
                 "- iBlack",
                 "Espaço João Berto")
    ],
    "Espaço João Berto - *02/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 2, 10, 00, 0),
                 "10h00 - 10h30",
                 "O reposicionamento de conteúdo como resposta para o grande volume de informações nas redes sociais",
                 "Convidado: Gerson Soares Diniz - Agente de Marketing na Aduela Ventures",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 10, 30, 0),
                 "10h30 - 11h00",
                 "Apresentação sobre programas Inovacred e Mulheres Inovadoras da Finep",
                 "Convidado: Rafaelly Fortunato - Gerente Substituta do Departamento Regional Nordeste da Finep",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 11, 00, 0),
                 "11h00 - 12h00",
                 "O Afroempreendedorismo de excelência: Como conquistá-lo.",
                 "Convidado: Marcelo Arruda - CEO - Dreamer & Fouder da Diversidade.io",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 14, 00, 0),
                 "14h00 - 15h00",
                 "Recursos desenrolados para sua empresa inovar.",
                 "Convidado: José Henrique Videira Menezes - Gerente de Mobilização Empresarial da Embrapii",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 15, 00, 0),
                 "15h00 - 16h00",
                 "Mentoria coletiva",
                 "Convidado: Filipe Garcia - Head de aceleração - WOW Aceleradora",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 16, 00, 0),
                 "16h00 - 17h00",
                 "O potencial de negócios espaciais",
                 "Convidados: Eng. Alano - Chefe da Divisão de Suporte Operacional - Centro de Lançamento de "
                 "Alcântara Leka Hattori - CEO da Space Terra e Líder local da Nasa Space",
                 "Espaço João Berto"),
        Palestra(datetime.datetime(2023, 6, 2, 17, 00, 0),
                 "17h00 - 18h00",
                 "Parcerias para alavancar os ecossistemas de inovação",
                 "Convidados: Ariana Pimentel - Marandu Fernanda Furtado - Analista Operacional na Vale Crisley "
                 "Pacheco - Líder dos Hubs de Inovação na Vale Greyce Franzmann - Líder de projetos de inovação na "
                 "Vale",
                 "Espaço João Berto")
    ],
    "SEBRAELAB - *01/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 1, 10, 30, 0),
                 "10h30 - 11h30",
                 "Ferramentas para o Desenvolvimento de Startups: Criando, Entregando e Comunicando Valor",
                 "Convidado: Jorge Henrique Gadelha - Diretor de Planejamento - NúcleoHub",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 11, 30, 0),
                 "11h30 - 12h30",
                 "Superando a Tradição: Oxe, Startups também surgem nas escolas!",
                 "Convidado: Mônica Mariano - SENAI",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 14, 00, 0),
                 "14h00 - 15h00",
                 "Academia & Startups: Investimento e Aceleração com SmartMoney Acadêmico",
                 "Convidado: Jacson Tiola - Head de Integração e Aceleração do Hub FUCAPE",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 15, 00, 0),
                 "15h00 - 16h00",
                 "É coisa de Mulher ser CEO",
                 "Convidados: Camilla Telles - Angels Wallet Ivy Cristiny - Mentora do Ano pelo Startup Awards Marina "
                 "Vaz - CEO da Scooto Lilian Natal - Diretora de Marketing e Relações com Investidores da Bossa Nova "
                 "Investimentos Cris Pelegrino - Head de Pessoas da Ventiur",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 16, 00, 0),
                 "16h00 - 17h00",
                 "Desenvolvimento de habilidades criativas para times de tecnologia e inovação",
                 "Convidado: Mel Campos - Designer estratégica de inovação da Natura",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 17, 00, 0),
                 "17h00 - 18h00",
                 "No-code: crie sua startup em 7 dias ou seu dinheiro de volta",
                 "Convidado: Ederson Dé Manoel - Founder da startup No Code School",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 1, 18, 00, 0),
                 "18h00 - 19h00",
                 "Conheça as Comunidades de Inovação Maranhenses e Conecte-se com o Poder da Colaboração.",
                 "Convidado: Lai Amorim - Líder de comunidade na Soluises",
                 "SEBRAELAB")
    ],
    "SEBRAELAB - *02/06* 📅": [
        Palestra(datetime.datetime(2023, 6, 2, 9, 00, 0),
                 "09h00 - 12h00",
                 "Maratona Só Inova Quem Faz",
                 "Convidado: Alexandre Mori - Co-Founder da MVPlay e Co- Founder da Angel Investor Club",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 2, 14, 00, 0),
                 "14h00 - 16h30",
                 "Rodada mão na massa",
                 "Convidado: Alexandre Mori - Co-Founder da MVPlay e Co- Founder da Angel Investor Club",
                 "SEBRAELAB"),
        Palestra(datetime.datetime(2023, 6, 2, 17, 00, 0),
                 "17h00 - 18h00",
                 "Criatividade e Inovação - Ideathons e seus resultados",
                 "Convidado: Alexandre Mori - Co-Founder da MVPlay e Co- Founder da Angel Investor Club",
                 "SEBRAELAB"),
    ]
}
