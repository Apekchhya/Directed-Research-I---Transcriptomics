import os
import subprocess
from config import ANNOTATION_GTF, GFFCOMPARE_OUT, MERGE_OUT

def run_gffcompare():
    # make sure output directory exists
    os.makedirs(GFFCOMPARE_OUT, exist_ok=True)

    subprocess.run([
        "gffcompare",
        "-r", ANNOTATION_GTF,
        "-o", f"{GFFCOMPARE_OUT}/merged",
        f"{MERGE_OUT}/stringtie_merged.gtf"
    ], check=True)

    print("✅ gffcompare finished")