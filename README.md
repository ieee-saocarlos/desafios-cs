# Primeiro desafio

Olá membros do CS! 
Espero que estejam animados para trabalhar em equipe e aprender com alguns desafios. A ideia aqui é que todos se ajudem. Aqui estão algumas regras gerais:

* Um desafio apenas será liberado assim que todos completarem o anterior.
* Para o desafio ser considerado completo, todas as tarefas devem ser completadas.

Agora vamos ao que interessa. O desafio de hoje é...

## Github + Git Básico

Caso queira uma introdução a essas ferramentas abra o arquivo "git_github.md" neste mesmo repositório, caso contrário pode avançar para as tarefas. Neste arquivo há também uma sessão para tirar dúvidas é recomendável ler a pergunta 3, mesmo para quem não tiver dúvidas sobre as tarefas.

## Primeira tarefa

A primeira tarefa é algo que a maioria já deve ter feito. Você deve:

1. Criar uma conta no GitHub (Caso não possua).
2. Mandar o nick na thread do slack (Caso não esteja na organização).
3. Baixar o Git:
    * Windows: Utilize o link do Git abaixo para baixar o instalador.
    * MacOS: Utilize o link abaixo para macOS.
    * Linux: 
        * $ sudo apt-get update
        * $ sudo apt-get install git

| Ferramenta | Link |
| ------ | ------ |
| Github | http://github.com |
| Git for Windows | https://git-scm.com |
| Passo-a-passo Git for Windows | https://dicasdeprogramacao.com.br/como-instalar-o-git-no-windows/|
| Git for macOS | https://sourceforge.net/projects/git-osx-installer/files/ |
| Caso nada funcione | https://www.atlassian.com/br/git/tutorials/install-git |

Se não sabe o que marcar no instalador entre no arquivo "duvidas_git.md" dentro deste mesmo repositório.

## Segunda tarefa

Agora vamos configurar o **Git**. A maioria das IDEs possui meios de utilizar o **Git** de forma simplificada e o próprio **GitHub** possui um programa voltado para isso, mas ele é muito bugado. 

No entanto, o que essas ferramentas fazem é basicamente digitar os comandos no **Git** pra você, então nada substitui você entender como ele funciona. Se souber utilizar o **Git** vai entender facilmente como funciona qualquer ferramenta baseada nele.

1. Crie uma pasta no seu computador para armazenar o repositório.
2. (No Windows pode pular para o passo 3) Abra o terminal (ou o Windows Power Shell) e navegue pelas pastas utilizando os comandos "cd nome_do_arquivo", "cd .." e "ls".
3. (Windows) Clicar com o botão direito nessa pasta e selecionar "Git Bash Here" .
4. No terminal que foi aberto digitar os seguintes comandos para dizer quem você é:
    * git config --global user.name "seu Nome e Sobrenome"
    * git config --global user.email "seu_email@email.com"
5. Para não ter que ficar logando toda vez crie uma chave ssh para se conectar ao GitHub:	
    * ssh-keygen -o -t rsa -C "seu_email@email.com"
6. Para ver a sua chave:
    * (Windows) notepad ~/.ssh/id_rsa.pub
    * (Linux) 
	* eval "$(ssh-agent -s)"
	* ssh-add ~/.ssh/id_rsa
	* cat ~/.ssh/id_rsa.pub
    * Copie essa chave. Dica: ctrl + a , ctrl + c.
7. Logue no GitHub, clique no icone do seu perfil e vá em:
   * "Settings" > "SSH and GPG keys" > "new SSH key".
8. Coloque um nome que identifique o seu computador e cole a chave no espaço 'Key'. Ao clicar em 'Add key' o seu trabalho está terminado.
9.  Se quiser verificar é só digitar "ssh -T git@github.com".

Caso tenha dúvidas no tópico 2: clique [aqui](https://www.lucascaton.com.br/2018/01/07/comandos-para-o-terminal-windows-macos-e-linux/);
Caso tenha dúvidas para adicionar a chave clique [aqui](https://jdblischak.github.io/2014-09-18-chicago/novice/git/05-sshkeys.html).

Pronto, o Git está configurado. É meio chato, mas você só precisará fazer isso uma vez em um computador. Está segunda tarefa é basicamente o passo a passo para ligar o GitHub ao seu computador.

## Terceira tarefa

Agora você irá contribuir para o projeto!
A ideia agora é que você faça sua contribuição e dê um commit no projeto

1. digite "git clone https://github.com/ieee-saocarlos/desafios-cs.git" no terminal ou no git bash. Agora o seu computador tem uma cópia do repositório dos desafios.
2. Essa pasta clonada apareceu dentro da pasta em que você usou o "git bash", então vá para essa nova pasta chamada "desafios-cs" e use o "git bash" nela ou então use o terminal para avançar para essa pasta com o comando "cd desafios-cs".
3. Dentro desse repositório remoto crie uma pasta com seu nome e um sobrenome.
4. Agora crie um arquivo .txt com o nome de uma figura que você admira.
5. Dentro do .txt escreva uma frase dessa pessoa
6. Voltando ao git bash ou ao terminal setado na pasta digite os seguintes comandos:
    * git add .
    * git commit -m "Adicionada uma frase de {figura}"
    * "git pull" para atualizar seu repositório local antes de enviar
    * "git push -u origin master"

Pronto! Agora é só ir no repositório do GitHub para verificar se sua pasta está lá. Se não estiver tente novamente ou procure ajuda na internet ou com outros membros. No arquivo "git_github.md" há uma sessão de respostas para algumas dúvidas comuns.









