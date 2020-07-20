
d = {}

with open("write_sample.txt", "w") as handle:
    handle.write(f"A: {d['A']}\n")
    handle.write(f"C: {d['C']}\n")
    handle.write(f"T: {d['T']}\n")
    handle.write(f"G: {d['G']}\n")

