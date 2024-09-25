import csv

def save(cols,infile,outfile):
    with open(infile,newline='') as ifile,\
        open(outfile,"w",newline='') as ofile:
        writer = csv.writer(ofile)
        header = [c[0] for c in cols]
        writer.writerow(header)
        for line in ifile:
            line = line.strip()
            if not line:
                continue
            row = []
            pos = 0
            for c in cols:
                w = c[1]
                row.append(line[pos:pos+w].strip())
                pos += w
            writer.writerow(row)
