from curri.curri import Curri
import json
import subprocess

if __name__ == "__main__":
    with open('real.json') as f:
        j = json.load(f)

    c = Curri(j)

    with open('output.tex', 'w') as f:
        f.write(c.latex())

    subprocess.call('pdflatex output.tex', shell=True)