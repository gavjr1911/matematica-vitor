# 📚 Português Divertido do Vitor — Módulo 2

App de jogos educativos para o Vitor (6 anos) estudar para a prova de **Língua Portuguesa do 1º ano** (livro Bernoulli Sistema de Ensino, **Capítulos 2 e 3**).

É o **Módulo 2** do projeto (o Módulo 1 é a Matemática, na pasta raiz). Mesma estrutura: **um único `index.html`**, sem instalação e sem internet depois de aberto. Funciona em celular, tablet e computador.

## 🎮 Os 9 mini-games

| Jogo | O que treina (conteúdo da prova) |
|------|----------------------------------|
| 🔤 **Letra que Repete** | Letra, sílaba e palavra — achar a letra que se repete |
| 🔠 **Ordem do ABC** | Colocar letras na ordem do alfabeto |
| 👏 **Conta Sílabas** | Contar sílabas batendo palmas |
| 🧩 **Junta Sílabas** | Montar a palavra colocando as sílabas na ordem |
| 🎵 **Rima** | Sons finais parecidos (balão/pão, gato/pato) |
| 🅱️ **P ou B?** | Sons parecidos de P e B (bola, pipa) |
| 🎉 **Convite** | Ler convite: dia, hora e local |
| ✉️ **Bilhete** | Quem escreveu, para quem e para quê |
| 📸 **Legenda** | Escolher a legenda que descreve a figura |

## 🎨 Ilustrações de verdade (não emojis)

As figuras são **ilustrações vetoriais SVG** coloridas e desenhadas para o app (bola, pipa, sorvete, borboleta, bolo, convite, bilhete etc.) — **37 ilustrações** embutidas no próprio `index.html`. Vantagens: ficam **nítidas em qualquer tela**, são leves e funcionam **100% offline**, e o objeto fica claramente reconhecível (importante para os jogos de associação).

## 👶 Pensado para quem ainda não lê

- 🔊 **Narração com voz natural** — a pergunta **e todas as respostas** são faladas em voz alta (português), com **voz neural**. O áudio é **pré-gravado em MP3** (pasta `audio/`), então **funciona em qualquer aparelho, sem depender de voz instalada** no navegador.
- 🗣️ **Cada opção fala** — ao tocar numa resposta, o app fala o nome dela, ajudando a aprender mesmo errando.
- ⭐ **Estrelas e pontos** — recompensa a cada acerto, com confete e som de vitória (as estrelas ficam guardadas no aparelho).
- 🧩 **Jogável sozinho** — perguntas sorteadas, sempre tem treino novo, e a criança brinca sem precisar de adulto ao lado.

### 🔈 Sobre o áudio
- Os áudios ficam em `audio/` (≈ 150 arquivos `.mp3`) — tocam em iPhone, Android, Chrome, Safari, Edge e Firefox, online ou offline.
- **Toque sempre em "▶ COMEÇAR" primeiro** — esse toque libera o som (regra dos navegadores).
- **iPhone/iPad**: tire do **modo silencioso** e suba o volume.
- Para **repetir** a leitura, toque no botão amarelo **🔊** ao lado da pergunta.

### 🎙️ Regerar os áudios (opcional)
Os áudios já estão prontos. Foram gerados com **vozes neurais** (`edge-tts`, grátis, sem chave). Para regravar (ex.: trocar a voz):
```bash
# a partir da pasta raiz do projeto (que tem a .venv):
cd "Prova Vitor"
.venv/bin/python portugues2/gerar-audios.py                          # voz Francisca (padrão)
VOZ=pt-BR-AntonioNeural .venv/bin/python portugues2/gerar-audios.py  # voz masculina
RATE=-15% .venv/bin/python portugues2/gerar-audios.py                # mais devagar
```
O script lê os textos do objeto `VOICE` dentro do `portugues2/index.html` e gera um MP3 por frase.

## 📁 Estrutura
```
portugues2/
  index.html        ← o jogo (abra este arquivo)
  audio/            ← narração pré-gravada (.mp3)
  gerar-audios.py   ← regerador de áudios (opcional)
  _art/             ← código-fonte das 37 ilustrações SVG (já embutidas no index.html)
  IMG_*.heic        ← fotos do conteúdo da prova (material de origem)
```

## 🚀 Como usar
Abra o `index.html` no navegador (celular, tablet ou computador), toque em **▶ COMEÇAR** e deixe o Vitor brincar! Para publicar no GitHub Pages, é só enviar a pasta `portugues2/` junto com `audio/`.

---
Feito com 💜 para o Vitor.
