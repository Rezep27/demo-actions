import os 

valor = os.environ.get("INPUT_VAL")

if "GITHUB_OUTPUT" in os.environ:
    with open(os.environ["GITHUB_OUTPUT"], "a") as f: 
        print("{0}= Hola {1}".format('result', valor), file=f)

