import sys
import json

def read_txt(file_name: str) -> str:
    ret = ""
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            ret += line.strip()
    return ret

def read_csv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split(",")
                continue
            splitted = line.strip().split(",")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def read_tsv(file_name: str) -> list:
    ret = []
    with open(file_name,'r') as handle:
        for line in handle:
            if line.startswith("#"):
                header = line.strip().split("\t")
                continue
            splitted = line.strip().split("\t")
            d = dict(zip(header, splitted))
            ret.append(d)
    return ret

def to_json(l: list, file_name) -> None: # json파일로 변환하기 위해선 반드시 리스트형태여야 한다.
    with open(file_name,'w') as handle:
        json.dump(l, handle, indent=4) #json.dump은 json에 있는데json을 만들어주는 데 관여한다. 

def to_json(file_name: str) -> list:
    with open(file_name, 'r') as handle:
        l = json.load(handle)
    return l

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("#usage: python {sys.argv[0]} [txt]")
        sys.exit()

    file_name = sys.argv[1]
    #txt = read_txt(file_name)
    #print(txt)
    #ret = read_csv(file_name)
    ret = read_tsv(file_name)
    to_json(ret)

