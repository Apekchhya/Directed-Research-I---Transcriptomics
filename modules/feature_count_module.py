import os
import subprocess
from config import (
    HISAT2_OUT,
    ANNOTATION_GTF,
    EXPR_OUT,
    THREADS
)

def run_featurecounts():
    """
    Run featureCounts using config.py paths
    (GFF3-aware for Verticillium dahliae)
    """

    os.makedirs(EXPR_OUT, exist_ok=True)
    output_file = os.path.join(EXPR_OUT, "featurecounts.txt")

    bam_files = sorted([
        os.path.join(HISAT2_OUT, f)
        for f in os.listdir(HISAT2_OUT)
        if f.endswith(".bam")
    ])

    if not bam_files:
        raise FileNotFoundError("❌ No BAM files found in HISAT2 output directory")

    cmd = [
        "featureCounts",
        "-T", str(THREADS),
        "-a", ANNOTATION_GTF,
        "-o", output_file,
        "-s", "0",          # unstranded
        "-p",               # paired-end
        "-t", "gene",       # count genes
        "-g", "gene_id"     # use clean gene IDs (VDAG_00001)
    ]

    cmd.extend(bam_files)

    print("\nRunning featureCounts:")
    print(" ".join(cmd))

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError("❌ featureCounts failed")

    print("✅ featureCounts completed successfully")
    print(f"📄 Output written to: {output_file}")
