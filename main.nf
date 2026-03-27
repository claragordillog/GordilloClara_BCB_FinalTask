#!/usr/bin/env nextflow
params.sam = null

process analyze_sam {

    input:
    path sam_file

    output:
    stdout

    script:
    """
    uv run python main.py ${sam_file}
    """
}

workflow {
    analyze_sam(params.sam)
}
