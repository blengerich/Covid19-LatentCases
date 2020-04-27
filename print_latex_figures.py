import os

with open("all_figures.tex", 'w') as outfile:
    for i, filename in enumerate(sorted(list(os.listdir("results")))):
        if i % 6 == 0:
            print("\\begin{figure}[tp]", file=outfile)
            print("\t \\centering", file=outfile)
        if "pdf" in filename:
            if i % 6 != 0:
                print("\t ~", file=outfile)
            print("\t \\begin{subfigure}[b]{0.49\\textwidth}", file=outfile)
            print("\t \\centering", file=outfile)
            print("\t \\includegraphics[width=\\textwidth]{{figs/{}}}".format(filename), file=outfile)
            print("\t \\caption{{ {} }}".format(filename.split(".")[0]), file=outfile)
            print("\t \\end{subfigure}", file=outfile)
        if i % 6 == 5:
            print("\\end{figure}", file=outfile)

    print("\\end{figure}", file=outfile)