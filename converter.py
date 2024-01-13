import markdown
import os
import sys


def main(argv):
    inputfile = argv[1]
    outputfile = argv[2]

    if not os.path.exists(inputfile): raise sys.stdout.buffer.write(b"Error inputfile doesn't exist")
    elif len(argv) != 3: raise sys.stdout.buffer.write(b"Wrong. convertmd.py inputfile outputfile")
    else: 
        html = ""
        with open(inputfile) as f:
            html = markdown.markdown(f.read())
        with open(outputfile, "w") as f:
            f.write(html)


if __name__ == "__main__":
    main(sys.argv)
