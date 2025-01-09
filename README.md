Hoop Snake

Descrição:
Para o desafio técnico proposto, criei este portal de notícias sobre basquete e NBA, com o objetivo de colocar em prática os conhecimentos requisitados.

O portal possui funcionalidades de adicionar notícias, ler, editar e excluir, formando um CRUD completo desenvolvido com Django e utilizando o banco de dados padrão do framework.
Falando mais sobre o framework utilizado, desde que aprendi a desenvolver com Django, fiquei impressionado com a facilidade que ele traz para o desenvolvimento. 
Além disso, continuo me surpreendendo com as diversas funcionalidades constantemente adicionadas pela comunidade.
Uma das funcionalidades que gosto de destacar é a integração com o banco de dados. Comparado a outros frameworks e bibliotecas, o Django torna o processo muito mais simples, rápido e prático, 
o que facilita bastante a implementação de CRUDs em aplicações.

Aqui tem o link do video que gravei falando mais sobre a aplicação:

https://drive.google.com/file/d/1ZAlBfMXNi8JZKtQamXNSPWR0XWKT07aq/view?usp=sharing



===== Para rodar o projeto =====

No terminal integrado digitar

pip install .

ou

python setup.py develop

E em seguida para rodar o servidor

python manage.py runserver

===== Se algum problema relacionado ao venv =====

Isso se da por que criei um ambiente virtual para desenvolver o projeto, para solucionar basta:
- Excluir a pasta .venv do projeto
- Criar um venv na sua maquina

Para criar o .venv no terminal o comando é:

py -m venv nome_do_ambiente

Após esse comando sera criada a pasta e os arquivos necessarios para seu ambiente de desenvolvimento

Para ativar basta digitar o comando

nome_do_ambiente\Scripts\activate.bat

E ja no terminal aparece o nome do ambiente, a partir dai ja pode rodar a aplicação com:

python manage.py runserver

===== Caso problema com arquivos staticos =====

No terminal digitar:

python manage.py collectstatic

Esse comando ira compilar os arquivos estaticos do projeto e resolve o problema de leitura dos mesmo
