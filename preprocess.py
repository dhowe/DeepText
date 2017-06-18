import glob, re, sys

count = 0
read_files = glob.glob("../DadaBase/texts/*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            txt = infile.read()
            txt = re.sub('\n  *', '\n', txt);
            txt = re.sub('[^*]*\*\*\*\*\!\*\*\*\*\n','', txt);
            txt = txt.replace('~~~~!~~~\n', '')
            txt = txt.replace('\n\n','')
            outfile.write(txt)
            sys.stdout.write('.')
            sys.stdout.flush()
            count = count + 1
            if count == 80:
                count = 0
                sys.stdout.write('\n')
