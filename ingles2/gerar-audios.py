#!/usr/bin/env python3
# ============================================================
#  GERADOR DE ÁUDIOS NEURAIS BILÍNGUE — English Fun!
#  Usa edge-tts (vozes neurais da Microsoft, grátis, sem chave).
#  Lê DOIS dicionários de dentro do index.html:
#    - VOICE     -> voz pt-BR (perguntas, traduções, feedback)
#    - VOICE_EN  -> voz en-US (as palavras/frases em inglês)
#  e gera um arquivo audio/<chave>.mp3 para cada frase, com a
#  voz certa de cada idioma.
#
#  Uso:
#    .venv/bin/python gerar-audios.py
#    VOZ_PT=pt-BR-AntonioNeural VOZ_EN=en-US-GuyNeural .venv/bin/python gerar-audios.py
# ============================================================
import os, re, sys, asyncio
import edge_tts

ROOT = os.path.dirname(os.path.abspath(__file__))
VOICE_PT = os.environ.get("VOZ_PT", "pt-BR-FranciscaNeural")
VOICE_EN = os.environ.get("VOZ_EN", "en-US-AnaNeural")   # voz infantil, clara p/ criança
RATE_PT  = os.environ.get("RATE_PT", "-8%")              # mais devagar p/ a criança acompanhar
RATE_EN  = os.environ.get("RATE_EN", "-6%")
PITCH    = os.environ.get("PITCH", "+0Hz")
OUT = os.path.join(ROOT, "audio")
CONCURRENCY = 8

def ler_dict(html, nome):
    m = re.search(r"const "+nome+r"\s*=\s*\{(.*?)\n\};", html, re.S)
    if not m:
        print(f"❌ Não encontrei o objeto {nome} no index.html"); sys.exit(1)
    # captura pares  chave:"texto"  (todos os valores usam aspas duplas)
    pares = re.findall(r'(\w+)\s*:\s*"((?:[^"\\]|\\.)*)"', m.group(1))
    # desescapa \" e \\
    return {k: v.replace('\\"', '"').replace("\\\\", "\\") for k, v in pares}

def ler_vozes():
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    pt = ler_dict(html, "VOICE")
    en = ler_dict(html, "VOICE_EN")
    return pt, en

async def gerar(sem, key, texto, voz, rate):
    async with sem:
        path = os.path.join(OUT, key + ".mp3")
        try:
            comm = edge_tts.Communicate(texto, voz, rate=rate, pitch=PITCH)
            await comm.save(path)
            print(f"✅ {key:<18} ({voz.split('-')[0]}-{voz.split('-')[1]}) “{texto}”")
            return True
        except Exception as e:
            print(f"❌ {key}: {e}")
            return False

async def main():
    pt, en = ler_vozes()
    os.makedirs(OUT, exist_ok=True)
    total = len(pt) + len(en)
    print(f"🎙️  Gerando {total} áudios: {len(pt)} em pt-BR ({VOICE_PT}) e {len(en)} em en-US ({VOICE_EN})...\n")
    sem = asyncio.Semaphore(CONCURRENCY)
    tarefas = [gerar(sem, k, t, VOICE_PT, RATE_PT) for k, t in pt.items()]
    tarefas += [gerar(sem, k, t, VOICE_EN, RATE_EN) for k, t in en.items()]
    res = await asyncio.gather(*tarefas)
    ok = sum(1 for r in res if r)
    print(f"\nPronto! {ok}/{total} áudios gerados em /audio (voz natural bilíngue).")

if __name__ == "__main__":
    asyncio.run(main())
