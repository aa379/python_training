import sys
for line in sys.stdin:
    if not line.strip():
        continue
    d={}
    d["e"]="q"
    d["r"]="w"
    d["t"]="e"
    d["y"]="r"
    d["u"]="t"
    d["i"]="y"
    d["o"]="u"
    d["p"]="i"
    d["["]="o"
    d["]"]="p"
    d["\\"]="["
    d["d"]="a"
    d["f"]="s"
    d["g"]="d"
    d["h"]="f"
    d["j"]="g"
    d["k"]="h"
    d["l"]="j"
    d[";"]="k"
    d["\'"]="l"
    d["c"]="z"
    d["v"]="x"
    d["b"]="c"
    d["n"]="v"
    d["m"]="b"
    d[","]="n"
    d["."]="m"
    d["/"]=","
    d["2"]="`"
    d["3"]="1"
    d["4"]="2"
    d["5"]="3"
    d["6"]="4"
    d["7"]="5"
    d["8"]="6"
    d["9"]="7"
    d["0"]="8"
    d["-"]="9"
    d["="]="0"
    result=""
    for char in line:
        if char in d:
            result+=d[char]
        else:
            result+=char
    print(result)