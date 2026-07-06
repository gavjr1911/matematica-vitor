# 🦉 English Fun! — Inglês Divertido

App de jogos educativos para o Vitor (6 anos) estudar para a prova de **Inglês do 1º ano** (livro Bernoulli Sistema de Ensino, **Chapters 3 e 4**).

Feito como **um único arquivo `index.html`** — sem instalação, sem internet depois de aberto. Funciona em celular, tablet e computador.

## 🎮 Os 9 mini-games

| Jogo | O que treina (conteúdo da prova) |
|------|----------------------------------|
| 🎮 **Brincadeiras** | Vocabulário de brincadeiras: *play ball, ride a bike, jump rope, assemble puzzles, skateboard, fly a kite, building blocks...* |
| 🗣️ **Eu Gosto** | Opinião e preferência: *I like to... / I don't like to...* |
| 🔎 **Instrumentos** | Instrumentos do cientista: *microscope, telescope, magnifying glass, scale* (e para que servem) |
| ⏳ **Antes ou Agora** | Invenções *Then & Now* (passado × presente): carriage→car, letter→cellphone, books→computer... |
| 🌱 **Vivo ou Não** | *Living / Non-living things* + do que precisam (*food, water, air*) |
| 🧸 **Macio ou Duro** | Classificar objetos: *soft / hard* |
| 🍃 **Natural?** | Classificar objetos: *natural / manmade* |
| 🤸 **Flexível?** | Classificar objetos: *flexible / rigid* |
| 🧑‍🔬 **Cientistas** | Cientistas famosos: Marie Curie (X-ray), Santos Dumont (airplane) |

## 👶 Pensado para quem ainda não lê — e está aprendendo inglês

- 🇺🇸 **Respostas 100% em inglês (imersão)** — os boxes de resposta mostram e falam **só inglês** (voz nativa `en-US`), **sem tradução em português**. Assim a criança precisa aprender de verdade, sem "colar" pela tradução.
- 🇧🇷 **Perguntas em português** — a instrução ("Como se diz…?", "Isto é macio ou duro?") é falada em português (voz `pt-BR`), para a criança entender a tarefa. Só a **resposta** é que é em inglês.
- 🗣️ **Cada opção fala em inglês** — ao tocar numa resposta, o app pronuncia a palavra em inglês, ajudando a aprender mesmo errando.
- ⭐ **Estrelas e pontos** — recompensa a cada acerto, com confete e som de vitória.
- 🎨 **Visual grande e colorido** — emojis grandes no enunciado e botões enormes, fáceis de tocar.
- 🔁 **Repetição infinita** — as perguntas são sorteadas, sempre tem treino novo.

### 🔈 Sobre o áudio
- 106 arquivos `.mp3` na pasta `audio/` (33 perguntas/instruções em português + 73 palavras em inglês).
- **Toque sempre em "▶ START / COMEÇAR" primeiro** — esse toque libera o som (regra dos navegadores).
- **iPhone/iPad**: tire do **modo silencioso** (chavinha lateral) e suba o volume.
- Para **repetir** a leitura, toque no botão amarelo **🔊** ao lado da pergunta.
- Tem um botão **🔈 Testar som** na tela inicial para conferir.

### 🎙️ Regerar os áudios (opcional)
Os áudios já estão prontos. Foram gerados com **vozes neurais** (`edge-tts`, grátis, sem chave de API). O script lê os **dois dicionários** do `index.html` (`VOICE` em pt-BR e `VOICE_EN` em en-US) e usa a voz certa de cada idioma:

```bash
python3 -m venv .venv && .venv/bin/pip install edge-tts   # 1ª vez
.venv/bin/python gerar-audios.py                          # vozes Francisca (pt) + Ana (en)
VOZ_PT=pt-BR-AntonioNeural VOZ_EN=en-US-GuyNeural .venv/bin/python gerar-audios.py  # vozes masculinas
RATE_EN=-12% .venv/bin/python gerar-audios.py             # inglês mais devagar
```

## 💡 Dicas para usar com a criança
- No **iPhone/iPad**, toque uma vez em "START" para liberar o som da narração.
- Incentive a criança a **repetir em voz alta** a palavra em inglês que ouviu.
- As estrelas ⭐ ficam guardadas no aparelho — ele acumula a cada partida.

---
Feito com 💙 para o Vitor aprender inglês brincando.
