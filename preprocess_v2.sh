
add_auxiliary_data=true

if $add_auxiliary_data ; then
    python preprocess_v2.py \
        --add_auxiliary_data True \
        --languages "CJE"
else
    python preprocess_v2.py \
        --languages "CJE"
fi