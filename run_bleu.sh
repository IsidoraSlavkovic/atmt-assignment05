#!/bin/bash

# Loop for different beam sizes
for k in {1..25}; do
    echo "Running beam size $k ..."

    # Run translate beam
    python translate_beam.py \
        --dicts data/en-fr/prepared \
        --data data/en-fr/prepared \
        --checkpoint-path assignments/03/baseline/checkpoints/checkpoint_best.pt \
        --output translation_results/model_translations_k$k.txt \
        --beam-size $k
    
    # Run postprocess
    bash scripts/postprocess.sh translation_results/model_translations_k$k.txt translation_results/model_translations_k$k.p.txt en
    
    # Run sacrebleu and save the JSON output
    cat translation_results/model_translations_k$k.p.txt | sacrebleu data/en-fr/raw/test.en > translation_results/bleu_output_k$k.json
done

echo "All BLEU calculations completed!"