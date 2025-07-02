import glob
import pypandoc
import os

os.makedirs("docs", exist_ok=True)
for f in sorted(glob.glob("docs_src/*.docx")):
    name = os.path.splitext(os.path.basename(f))[0]
    out = os.path.join("docs", name + ".md")
    pypandoc.convert_file(f, "gfm", outputfile=out)
    print("Converted", f, "->", out)
