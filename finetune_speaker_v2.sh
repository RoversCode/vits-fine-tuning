#!/bin/bash

CONTINUE=false # 或者你可以设置为 false
Maximum_epochs=200

if $CONTINUE ; then
    python finetune_speaker_v2.py \
        -m "./ckpts" \
        --max_epochs $Maximum_epochs \
        --drop_speaker_embed False \
        --cont True
else
    python finetune_speaker_v2.py \
        -m "./ckpts" \
        --max_epochs $Maximum_epochs \
        --drop_speaker_embed True 
fi
