SYNTHETIC ALZHEIMER TEACHING SEQUENCE DATASET
================================================

Purpose
-------
Teaching dataset linked to the 1,000-patient synthetic clinical table.
It contains the same five Alzheimer-associated genes for every patient:
APP, PSEN1, PSEN2, APOE, and TREM2.

IMPORTANT
---------
These DNA sequences are entirely synthetic teaching fragments.
They are NOT authentic human genomic sequences and the variant IDs are NOT
real clinical variants. Do not use this dataset for biomedical or clinical inference.

Main FASTA
----------
File: alzheimer_synthetic_1000_patients_5genes.fasta
Records: 5000
Patients: 1000
Genes per patient: 5
Header example:
>P0001|gene=APP|chr=21|source=synthetic

The Alzheimer label is intentionally NOT stored in FASTA headers.
Join patient_id against the original clinical CSV to recover case/control status.

Reference FASTA
---------------
File: alzheimer_synthetic_reference_5genes.fasta
Contains one synthetic reference fragment per gene.

Variant design
--------------
- Reproducible random seed: 20260828
- Background SNPs occur in both cases and controls.
- Background insertions/deletions occur in both groups.
- Selected synthetic hotspots are enriched among Alzheimer cases.
- Some controls carry risk hotspots and some cases do not, so genotype does
  not trivially encode the class.
- APOE contains a synthetic two-SNP linked risk haplotype.
- Sequences represent one synthetic consensus allele per patient/gene, not a
  diploid phased genome.

Instructor-only files
---------------------
alzheimer_synthetic_variants_INSTRUCTOR_KEY.csv
    Exact synthetic variant truth table.

alzheimer_synthetic_patient_variant_summary_INSTRUCTOR_KEY.csv
    Per-patient synthetic variant burden summary.

Class distribution inherited from the clinical table
-----------------------------------------------------
Controls (alzheimer=0): 657
Cases    (alzheimer=1): 343

Recommended student workflow
----------------------------
1. Parse the multifasta.
2. Separate patient_id and gene from each FASTA header.
3. Compare each patient sequence with the corresponding synthetic reference.
4. Detect substitutions and simple indels.
5. Build patient-level variant features.
6. Join those features to the clinical CSV by patient_id.
7. Compare variant frequencies/burdens between healthy and Alzheimer groups.
