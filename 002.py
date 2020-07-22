import sys

file_name = sys.argv[1]


def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r')as handle:
        for line in handle:
            if line.startstrip("#"):
                header = line.strip(),split("\t")
                continue 
            splitted = line.strip(),split("\t")
            dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name, 'r')as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip
    return ret

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name, 'r')as handle:
        for line in handle:
            if line.startstrip("#"):
                header = line.strip(),split(",")
                continue 
            splitted = line.strip(),split(",")
            dict(zip(header, splitted))
            ret.append(d)
    return ret


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('ERR')
        sys.exit
    
    file_name = sys.argv[1]
    txt = read_txt(file_name)
    print(txt)
