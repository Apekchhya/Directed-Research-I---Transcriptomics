import os, glob, subprocess
from config import HISAT2_OUT, MERGE_OUT, EXPR_OUT, THREADS

os.makedirs(EXPR_OUT, exist_ok=True)

def run_quantification():
    bam_files = glob.glob(f"{HISAT2_OUT}/*.sorted.bam")

    for bam in bam_files:
        sample = os.path.basename(bam).replace(".sorted.bam", "")
        sample_dir = f"{EXPR_OUT}/{sample}"
        os.makedirs(sample_dir, exist_ok=True)

        subprocess.run([
            "stringtie", bam,
            "-e", "-B",
            "-G", f"{MERGE_OUT}/stringtie_merged.gtf",
            "-o", f"{sample_dir}/{sample}.gff3",
            "-p", str(THREADS)
        ], check=True)

        print(f"✅ Quantification done: {sample}")

