import pandas as pd
import os

def print_table(file):
    A = pd.read_csv(file)
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
    L.insert(14-len(L), "\\hline")

    L.insert(0, "\\begin{table}[H]")
    L.insert(1, "\\centering\\scriptsize")
    L.insert(2, "\\caption{"+file[:-4].replace('_', ' ')+"}")
    L.insert(3, "\\label{"+file[:-4]+"}")
    L[-1] = "\\end{table}"

    L.insert(0, "\\newcommand{\\"+ file[:-4].replace('_', '') + "}{")
    L.append("}")

    return L

def main():
    files = ["df_time.csv", "df_acc.csv", "df_f.csv", "friedman_fit_time.csv", "friedman_accuracy_score.csv", "friedman_f_score.csv"]
    document = []
    for file in files:
        document.extend(print_table(file))

    with open('tables.txt', 'w') as file:
        for line in document:
            file.write(line)
            file.write("\n")

    

if __name__ == '__main__':
    main()
