import os, glob, subprocess
from config import HISAT2_OUT, STRINGTIE_OUT, ANNOTATION_GTF, THREADS

os.makedirs(STRINGTIE_OUT, exist_ok=True)

def run_stringtie():
    bam_files = glob.glob(f"{HISAT2_OUT}/*.sorted.bam")

    for bam in bam_files:
        sample = os.path.basename(bam).replace(".sorted.bam", "")
        out_gtf = f"{STRINGTIE_OUT}/{sample}.gtf"

        subprocess.run([
            "stringtie", bam,
            #"-G", ANNOTATION_GTF,
            "-o", out_gtf,
            "-p", str(THREADS)
        ], check=True)

        print(f"✅ StringTie assembly done: {sample}")

