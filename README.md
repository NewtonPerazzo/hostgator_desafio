# Desafio HostGator 🚀

<h4>Este respositório tem como propósito cumprir o desafio técnico proposto pela empresa Hostgator para vaga de backend.</h4>
<h5>Para o desafio, utilizei os seguintes conhecimentos: </h5>

* Desenvolvimento Web 💻
* Manipulação de API ⚙
* Manipulação do ORM do Django 🐍
* Manipulação de Banco de Dados 🏢
* Utilização de bibliotecas 📚
* Desenvolvimento Frontend 🎨


<h3>Linguagem, Frameworks, Bibliotecas e Frontend utilizados 💼</h3>

```
* Linguagem: Python 3;
* Gerenciador de Tarefas: Pip3
* Framework Web: Django;
* Bibliotecas:
    - requests;
* Bootstrap, HTML e CSS.

````

<h3>Como rodar o projeto em sua máquina 🛠</h3> 

<h5>
Você pode baixar o repositório pelo próprio GitHub, cloná-lo através do Git + sua chave SSH ou do Git + link do repositório no GitHub, utilizando o comando:

 
`git clone {chave SSH}` ou `git clone https://github.com/NewtonPerazzo/hostgator_desafio` 
    
Após baixar o repositório em sua máquina e abri-lo com uma IDE de sua preferência, vamos para a parte de instalação de requisitos para que o sistema funcione.
<p>Para isso, rode o comando: </p>

```
    pip3 install -r requirements.txt
```
<p>Para ativar a VirtualEnv no Windows: </p> 

    .venv\Scripts\activate.bat  
<p>Para ativar a VirtualEnv no Linux ou Mac: </p>

```
    source .venv/bin/activate
```
<p>Caso não possua a VirtualEnv, é somente instalá-la com o pip e depois criar seu próprio ambiente virtual.</p>

```
    pip3 install virtualenv 
    virtualenv {nome_da_virtualenv}
```
<p>Ativada a VirtualEnv, basta passar os comandos, também no terminal:</p>
 
```
    python3 manage.py makemigrations
    python3 manage.py migrate
```
<p>

Com as migrations realizadas, ative o servidor com o comando `python3 manage.py runserver`. Será informado o link 
`http://127.0.0.1:8000/` e basta acessá-lo para ver o site funcionando.
</p>

<p>Caso não possua o Python e o Pip instalado em sua máquina, se estiver no Linux ou MacOS, rode:</p>
<p>Para Linux:</p>

```
    sudo apt-get install python3
    sudo apt-get install python3-pip3
    
```
<p>Para MacOS:</p>

```
    brew install python3
    brew install pip3
```
<p>OBS.: para esses dois sistemas o Python já vem pré-instalado.</p>

<p>

Caso esteja no Windows, acesse o link `https://www.python.org/downloads/` e baixe de acordo a sua máquina. Após seguir a
instalação padrão, abra o CMD, rode `python --version` e `pip --version` para ver se foi instalado com sucesso (o Pip já
vem junto ao Python).
</p>

<p>Com o Python e o Pip instalado, é só voltar para a instalação dos requisitos e virtualenv.</p>
</h5>

<h3>Explicando a funcionalidade do sistema ⛅</h3>

<h5>
<p>

O código gira em torno, basicamente, da API. Criei o model de Domínio para receber o link passado pelo usuário e através
dele pesquiso na API as informações.
</p> 

<p>

Como a regra de negócio é bastante complicada e cheia de possibilidades, fui implementando o código e retornando as informações
junto com o template de acordo com as mesmas.
</p>

<p>

Ao adicionar o domínio, os dados vão para o Banco de Dados SQLite padrão e, posteriormente, são passados como
argumento de pesquisa na API. As informações encontradas são tratadas na ```view.verDominio()```, de acordo primeiramente se o que foi
enviado pelo usuário não é vazio (None). Caso não seja, verificamos se o tamanho do link se enquada nos requisitos (no máximo 
26 e no mínimo 8 - o mínimo foi implatado por mim para facilitar e isso é informado no template).
</p> 

<p>

Estando de acordo, verifica o `status` do domínio e, para o caso de estar disponível, fazemos as verificações da regra 
de negócio (se tiver hostgator, endurance, loja ou premium no domínio) para atribuir os valores de `available`, `price` 
e `reason`.
</p>

<p>

Caso o domínio esteja indisónivel, atribuo também a regra de negócio no fim do código e passo mensagens como context para
os casos de não poder pesquisar o domínio na API. Vale ressaltar que a cada domínio inserido no banco, ele é processado 
e no fim deletado para evitar o excesso de dados desnecessários.
</p>

<p>

A `view.home` serve apenas para renderizar o formulário de criação do model para pesquisa na API. A parte de template
foi divida em base, onde encontra-se o código raíz para que os outros HTML herdem da própria base, com o CSS criado. Já
os demais módulos (URL, admin, forms, settings, etc.) foi seguido o padrão do Django.
</p>

</h5>

<h3>Conclusão ✅</h3>
<h5>
<p>

O projeto foi bastante proveitoso, pois exigiu bastante entendimento da regra de negócio e de bastante conhecimento
básico da linguagem.
</p>
    
<p>

Foi possível mais uma vez trabalhar e reforçar os conceitos de desenvolvimento web, como parte do CRUD e a 
manipulação de dados no banco, bem como os conceitos lógicos e básicos de programação para que o sistema funcionasse 
(exemplos: listas, index,funções de string e formatação).
</p>

<p>

Por fim, pude praticar e mostrar também a programação frontend, que não é necessariamente minha melhor skill (visto
que sou mais adepto ao backend), mas que é crucial entender, tanto a parte de exibição em templates, quando a de
estilização com CSS, para facilitar o entendimento geral de um sistema.
</p>
</h5>


