import os, glob, subprocess
from config import STRINGTIE_OUT, MERGE_OUT, ANNOTATION_GTF

os.makedirs(MERGE_OUT, exist_ok=True)

def run_merge():
    mergelist = f"{MERGE_OUT}/mergelist.txt"
    gtf_files = glob.glob(f"{STRINGTIE_OUT}/*.gtf")

    with open(mergelist, "w") as f:
        f.write("\n".join(gtf_files))

    subprocess.run([
        "stringtie", "--merge",
        #"-G", ANNOTATION_GTF,
        "-o", f"{MERGE_OUT}/stringtie_merged.gtf",
        mergelist
    ], check=True)

    print("✅ StringTie merge completed")

