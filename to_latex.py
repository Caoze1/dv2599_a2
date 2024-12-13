import pandas as pd

def main():
    A = pd.read_csv('df_scores_2.csv')
    A = A.to_latex(index=False, float_format="%.4f")
    L = [x for x in A.split('\n')]
    
    Lhead = L[2].split('&')
    Lhead = [l.replace('\\', '') for l in Lhead]
    Lhead = [l.strip() for l in Lhead]
    Lhead = ["\\textit{"+l+"}" for l in Lhead]
    L[2] = " & ".join(Lhead) + " \\\\"

    L[0] = "\\begin{tabular}{ccccc}"
    L[1] = "\\hline"
    L[3] = "\\hline"
    L[-3] = "\\hline"
    L.insert(-5, "\\hline")

    L.insert(0, "\\begin{table}[htbp!]")
    L.insert(1, "\\centering\\scriptsize")
    L[-1] = "\\end{table}"

    for l in L:
        print(l)

if __name__ == '__main__':
    main()