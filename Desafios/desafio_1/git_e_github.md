## Github + Git Básico

Antes mesmo de começar a programar, precisamos de um meio de todos enviarem seus códigos de forma eficiente e integrada para que possa ser feito o acompanhamento. Por isso, a primeira ferramenta que será apresentada é o famoso [GitHub](http://github.com). O que é o GitHub?

> GitHub é uma plataforma de **hospedagem de código-fonte** com **controle de versão** usando o **Git**.

Calma. Eu vou explicar cada parte.

A primeira é fácil, hospedagem de código-fonte é basicamente guardar os programinhas que vc fez, mas isso não é um diferencial. O Google Drive pode ser considerada uma plataforma de hospedagem de código-fonte, é só você colocar seus códigos-fonte lá. 

A segunda parte já é bem mais interessante, controle de versão diz respeito a conseguir dividir seu projeto em versões. Assim como em um jogo que possui vários "patches" ou atualizações. Isso tudo é feito pelo [Git](https://git-scm.com/). Cada vez que você termina uma parte ou implementa uma nova funcionalidade no seu programa você faz um "commit", basicamente esse commit é como salvar o arquivo e você precisa adicionar uma mensagem que descreva brevemente o que foi feito ou alterado.

O interessante disso é que cada commit funciona como uma versão do seu programa e caso você faça futuras alterações que causem algum bug no programa ou não sejam desejadas é só voltar para um commit anterior, ou seja, uma versão anterior.

**Resumo**: O **GitHub** é a plataforma que irá hospedar os arquivos e mostrar o que foi feito pelo **Git**. Ele funciona também como uma espécie de rede social ou banco de dados em que é possível encontrar vários outros projetos e seguir pessoas. O **Git** é o responsável por fazer os commits, enviar o código-fonte do seu computador para o **GitHub** e realizar o controle de versões e de branches.

# Dúvidas sobre o Git

É possível que você tenha encontrado alguma dificuldade ao fazer o desafio, então aqui estão as respostas para algumas dúvidas mais frequentes:

1. **O que eu preciso marcar no instalador do Git para Windows?**

    Esse site tem tudo o que você vai precisar https://dicasdeprogramacao.com.br/como-instalar-o-git-no-windows/

2. **Onde consigo o endereço do repositório que será clonado?**

    Entre no repositório no site do github, no caso estamos usando esse [aqui](https://github.com/ieee-saocarlos/desafios-cs). Lá há um botão verde em que está escrito "Clone or download", ai é só copiar a URL para clonar utilizando o "git clone URL". É possível também baixar o repositório como um .zip.

3. **queria entender melhor o passo a passo da terceira tarefa**
    
    Isso exige um pouco da visão geral de tudo, então vamos lá:

    Como é feito um commit? Pensa assim, existe o **repositório principal** no GitHub e os **repositórios remotos** no computador de cada um.
        
    Ao clonar ou dar um "git pull" (puxar), você está pegando os arquivos do **Repositório principal** e colocando no **repositóro remoto** que se encontra na pasta do seu computador. Ai você é livre para fazer o que quiser dentro da sua versão do repositório. 
    
    Quando estiver satisfeito com as suas modificações é preciso seguir um passo a passo para não haver conflitos:
    
    * Primeiramente, você precisa avisar o Git de quais arquivos quer adicionar, para isso utilizamos o "git add". Ao utilizar "git add ." aquele ponto significa que você quer adicionar todas as suas pastas, o que é a mesma coisa que adicionar só aquilo que modificou, pois os arquivos repetidos serão ignorados.
    
    * Após avisar o git de quais arquivos quer modificar é hora de dizer o que você fez para ser fácil voltar para uma versão e lembrar o que havia sido modificado até aquele ponto. Para fazer isso vamos fazer um commit. O commit inclui uma mensagem nas modificações que você quer fazer.

    * Antes de enviar os arquivos é bom usar o "git pull" antes para ter certeza de que ninguém modificou o repositório e o seu repositório remoto está atualizado. Caso contrário o Git não irá aceitar o seu push.
    
    * Finalmente, você deve fazer o upload do seu commit utilizando o "git push" só agora as outras pessoas podem ver o seu commit e ver os arquivos que adicionou com o push.

4. **E se alguém der um git push junto comigo?**

    Perceba que um push é algo que pode gerar muitos conflitos. Imagina que você decide dar um commit ao mesmo tempo que o seu amigo, e os dois modificam o mesmo arquivo, como vai ficar o repositório depois disso?
    
    Na verdade apenas um deles será aceito, aquele que enviar primeiro, mesmo que por uma fração de segundo, enviará o seu "git push" com sucesso, de forma que o repositório principal terá sido modificado. Aquele que enviou o push um pouco depois receberá uma mensagem de erro avisando que o seu repositóro local está desatualizado. Então ele precisará dar um git pull novamente e verificar se não há conflito entre as modificações que os dois fizeram.
