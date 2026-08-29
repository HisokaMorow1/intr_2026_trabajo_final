SYNTHETIC ALZHEIMER PROTEIN TEACHING DATASET
================================================

Purpose
-------
Protein-level counterpart of the synthetic 1,000-patient Alzheimer dataset.
The same five genes/proteins are present for every patient:
APP, PSEN1, PSEN2, APOE, and TREM2.

IMPORTANT
---------
All underlying nucleotide fragments and translated protein sequences are
synthetic teaching data. They are NOT authentic human protein sequences and
must not be used for clinical or biomedical inference.

Translation
-----------
All DNA fragments were translated with the standard genetic code from
nucleotide 1 (frame 1). Incomplete terminal codons were trimmed.

Because the original synthetic DNA fragments were not designed as canonical
coding sequences, literal translation produces internal stop symbols (*).
For this reason two protein FASTA versions are provided:

1. RAW FASTA
   alzheimer_synthetic_1000_patients_5proteins_raw.fasta
   Exact frame-1 translation. Internal stop codons are represented as '*'.

2. CLEAN FASTA
   alzheimer_synthetic_1000_patients_5proteins_clean.fasta
   The same translated sequences, but internal '*' symbols are replaced by 'X'.
   This version is recommended for general sequence processing, descriptors,
   embeddings, alignments, and introductory ML exercises.

Dataset dimensions
------------------
Patients: 1000
Proteins per patient: 5
Protein FASTA records: 5000

FASTA header example
--------------------
>P0001|gene=APP|chr=21|translation=frame1|internal_stop=X|source=synthetic

The Alzheimer label is intentionally not included in FASTA headers.
Join by patient_id against:
synthetic_alzheimer_patients_1000.csv

Reference protein FASTA
-----------------------
alzheimer_synthetic_reference_5proteins_raw.fasta
alzheimer_synthetic_reference_5proteins_clean.fasta

Protein variant instructor key
------------------------------
alzheimer_synthetic_protein_variants_INSTRUCTOR_KEY.csv

This file maps the known synthetic DNA variants to expected protein-level
effects:
- synonymous
- missense
- nonsense
- stop_lost
- inframe_insertion
- inframe_deletion
- frameshift_insertion
- frameshift_deletion

Patient-level summary
---------------------
alzheimer_synthetic_patient_protein_variant_summary_INSTRUCTOR_KEY.csv

Tabular sequence file
---------------------
alzheimer_synthetic_protein_sequences_5000.csv

Contains patient_id, gene, sequence, lengths, internal-stop count, and the
Alzheimer label. This is convenient for pandas-based exercises.

Recommended student workflow
----------------------------
1. Parse the protein multifasta.
2. Extract patient_id and gene from headers.
3. Compare each protein with its synthetic reference.
4. Detect substitutions and indel-associated sequence changes.
5. Build mutation or sequence-derived features.
6. Join with the clinical patient table.
7. Compare healthy and Alzheimer groups.
8. Optionally calculate descriptors, embeddings, similarity, PCA, or clustering.
