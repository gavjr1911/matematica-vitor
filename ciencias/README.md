# 🔬 Ciências Divertida

App de jogos educativos para o Vitor (6 anos) estudar para a prova de **Ciências do 1º ano** (conteúdo do livro Bernoulli Sistema de Ensino — Capítulos 2 e 3).

Feito como **um único arquivo `index.html`** — sem instalação, sem internet depois de aberto. Funciona em celular, tablet e computador.

## 🎮 Os 8 mini-games

| Jogo | O que treina (conteúdo da prova) |
|------|----------------------------------|
| 👀 **Cinco Sentidos** | Visão→olhos, audição→orelhas, olfato→nariz, paladar→língua, tato→pele |
| 🧍 **Partes do Corpo** | Cabeça, tronco e membros — onde fica cada parte |
| 💪 **Braços e Pernas** | Membros superiores × inferiores (ombro, cotovelo, joelho, tornozelo...) |
| ❤️ **Por Dentro** | Órgãos internos: onde ficam (tórax/abdome) e o que fazem |
| 🌞 **Dia e Noite** | Manhã, tarde e noite; sol, lua e estrelas |
| 📅 **Dias da Semana** | Os 7 dias, o que vem antes e depois |
| 🧼 **Higiene** | Escova/pasta, xampu, sabonete, lavar as mãos, cárie, unhas |
| 🥗 **Alimentação** | Saudável × pouco saudável; a principal refeição do dia |

## 👶 Pensado para quem ainda não lê

- 🔊 **Narração com voz natural** — a pergunta **e todas as respostas** são faladas em voz alta (português), com uma **voz neural natural** (não robótica). O áudio é **pré-gravado em arquivos MP3** (pasta `audio/`), então **funciona em qualquer aparelho, sem depender de voz instalada** no navegador.
- 🗣️ **Cada opção fala** — quando o Vitor toca numa resposta, o app fala o nome dela (ex.: "o coração!"), ajudando a aprender mesmo errando.
- ⭐ **Estrelas e pontos** — recompensa a cada acerto, com confete e som de vitória.
- 🎨 **Visual grande e colorido** — emojis e botões enormes, fáceis de tocar.
- 🔁 **Repetição infinita** — as perguntas são sorteadas, então sempre tem treino novo.

### 🔈 Sobre o áudio
- O áudio fica em **arquivos `.mp3`** na pasta `audio/` (≈ 2,4 MB no total) — toca em iPhone, Android, Chrome, Safari, Edge e Firefox, **online ou offline**.
- **Toque sempre em "▶ COMEÇAR" primeiro** — esse toque libera o som (regra dos navegadores).
- **iPhone/iPad**: tire do **modo silencioso** (chavinha lateral) e suba o volume.
- Para **repetir** a leitura, toque no botão amarelo **🔊** ao lado da pergunta.
- Tem um botão **🔈 Testar som** na tela inicial para conferir.

### 🎙️ Regerar os áudios (opcional)
Os áudios já estão prontos na pasta `audio/`. Foram gerados com **vozes neurais** (`edge-tts`, grátis, sem chave de API). Para regravar (ex.: trocar a voz):
```bash
python3 -m venv .venv && .venv/bin/pip install edge-tts   # 1ª vez
.venv/bin/python gerar-audios.py                          # voz Francisca (padrão)
VOZ=pt-BR-AntonioNeural .venv/bin/python gerar-audios.py  # voz masculina
RATE=-15% .venv/bin/python gerar-audios.py                # mais devagar
```
O script lê os textos do próprio `index.html` (objeto `VOICE`) e gera um MP3 por frase. Vozes pt-BR: `pt-BR-FranciscaNeural` (feminina), `pt-BR-AntonioNeural` (masculina), `pt-BR-ThalitaMultilingualNeural` (feminina).

## 🚀 Como publicar no GitHub Pages

Você pode publicar **só a pasta `ciencias/`** num repositório novo, ou junto com os outros módulos (Matemática e Português) no mesmo repositório.

**Opção A — repositório só de Ciências:**
```bash
# de dentro da pasta ciencias/
git init
git add index.html README.md gerar-audios.py audio/
git commit -m "Jogos de Ciências do Vitor"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/ciencias-vitor.git
git push -u origin main
```
Depois, em **Settings → Pages**, escolha branch `main` e pasta `/ (root)`. O jogo estará em:
`https://SEU_USUARIO.github.io/ciencias-vitor/`

**Opção B — junto com os outros módulos:** deixe a pasta `ciencias/` dentro do repositório do projeto e acesse por:
`https://SEU_USUARIO.github.io/REPO/ciencias/`

## 💡 Dicas para usar com a criança

- No **iPhone/iPad**, toque uma vez no botão "COMEÇAR" para liberar o som da narração.
- Se a voz não falar, é só tocar no botão amarelo 🔊 ao lado da pergunta.
- As estrelas ⭐ ficam guardadas no aparelho — ele acumula a cada partida.

---
Feito com 💜 para o Vitor.
