email_tmpl = """"
Olá, %(nome)s
Tem interesse em comprar %(produto)s?
Este produto é ótimo para
%(texto)s
Clique agora em %(link)s
Apenas %(quantidade)d disponível!!
Preco promocional %(preco).2f
"""

clientes = ["Michel", "Henrique", "Joao", "Maria"]

for cliente in clientes:
    print(email_tmpl % {"nome": cliente, "produto": "caneta", "texto": "Ela escreve muito bem", "link":
    "https://www.mundobic.com.br", "quantidade":  1, "preco": 50.5  })