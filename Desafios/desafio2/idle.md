# O que é uma IDE?
**IDE**, do inglês Integrated Development Environment ou Ambiente de Desenvolvimento Integrado é qualquer programa que une três ferramentas imprescindíveis para facilitar a vida de um programador. São elas:
* Editor de texto
* Compilador
* Depurador (Debugger)

## Editor de texto
Uma linguagem de programação pode ser escrita em um guardanapo com um pedaço de carvão, mas é muito mais fácil escrever em um editor de texto. 

Isso porque o editor possui diversas facilidades como:   
- **Formatação de texto**. 
- **Realce de sintaxe**.
- **Pesquisa e substituição** (ctrl + f). 
- **Desfazer e refazer** (ctrl +z, ctrl + y). 
- **Recortar, copiar e colar** (ctrl + x, ctrl + c, ctrl + v). 
- Alguns ainda possibilitam o **uso integrado com o terminal, cmd ou power shell**.

## Compilador

Compilador é o programa que transforma o belo programa escrito no editor de texto em linguagem de máquina para ser processado pelo processador.

No caso do Python existe o interpretador, que lê o seu programa e o interpreta linha a linha ao invés de compilar o código inteiro. 

Para mais informações a respeito da diferença entre os dois clique [aqui](https://www.oficinadanet.com.br/artigo/1527/diferencas_entre_compiladores_e_interpretadores) .

## Depurador

O depurador é um programa que testa outros programas para encontrar defeitos, com ele é possível a partir de uma linha específica observar cada passo que o seu programa dá, facilitando assim encontrar erros na lógica ou nas entradas do seu programa.

# O que é o IDLE?

O IDLE (**Integrated Development and Learning Environment**) é uma IDE escrita totalmente em Python e que é instalada junto quando você baixa o Python pelo site. Caso esteja utilizando o Linux, basta utilizar o comando "sudo apt-get install idle" no terminal.

Assim como o nome da linguagem é baseada na séria de comédia *Monty Python's Flying Circus*, o nome IDLE provavelmente é baseado em Eric Idle, um dos membros do grupo. O IDLE é uma ferramenta amigável para quem está aprendendo Python. 

## Abrindo o IDLE

Windows: O IDLE aparece como um executável na pasta do Python. então basta executar o .exe que está nessa pasta ou procurar "idle" no menu iniciar.

macOS e Linux: Digitar "idle" ou "idle3" no terminal deve funcionar.

## Utilizando o IDLE

Assim que abrir o IDLE  você verá o [REPL](https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop) (Read–eval–print loop) do Python, ele pode ser acessado também ao abrir o terminal e digita "python". Ele possui esse nome, pois faz exatamente isso. Lê uma linha de comando, calcula, depois escreve a resposta e reinicia o processo.

Esse é o método mais simples de acessar o interpretador do Python, e pode ser utilizado como uma espécie de calculadora como foi comentado durante a capacitação. No entanto, nós queremos agora escrever um programa, e para isso é muito melhor usar um editor de texto.

Para abrir o editor de texto do IDLE basta ir em **File > New File** E o editor será aberto. Vamos então começar escrevendo **print("Hello World!")** e apertando **F5** ou indo em **Run > Run Module**. Salve o arquivo e pronto! Você fez o seu primeiro programa em Python!

Agora você pode mudar as cores do IDLE em **Options > Configure IDLE** da forma que desejar.

*Observações: Arquivos em Python devem ser salvos com a extensão .py da mesma forma que aquivos em c possuem a extensão .c e arquivos do bloco de notas são salvos em .txt*





