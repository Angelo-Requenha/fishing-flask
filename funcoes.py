import sqlite3

def paginaInicial():
    caixaTexto = {'Home':['Bem-vindo ao MeuSite! Aqui você encontra design moderno, seções bem organizadas e um toque profissional em cada detalhe.', 'inicio'],
                  'Sobre':['Este site foi criado como um exemplo de navegação moderna com HTML e CSS puro. Ideal para portfólios, empresas ou landing pages simples.', 'sobre'],
                  'Servicos':['Oferecemos soluções em design de interface, desenvolvimento front-end, criação de sites institucionais, landing pages e mais.', 'servicos'],
                  'Contato':['Entre em contato pelo e-mail: <a href="mailto:contato@meusite.com">contato@meusite.com</a> ou pelas redes sociais. Estamos prontos para transformar sua ideia em realidade.', 'contato']
                  }
    
    return caixaTexto

def servicosPagina():
    paginas = {'FakeBook':['Pagina fake que imita o FaceBook', 'fakebook']
               }
    
    return paginas

def criaBanco():
    con = sqlite3.connect('DB/db.sqlite')
    cur = con.cursor() 

    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            nome TEXT NOT NULL
            )
    ''')

    con.commit()
