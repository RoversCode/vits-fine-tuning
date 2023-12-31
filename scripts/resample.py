import os
import json
import torchaudio

sampled_audio4ft_path = "./data/sampled_audio4ft"
def main():
    with open("./configs/finetune_speaker.json", 'r', encoding='utf-8') as f:
        hps = json.load(f)
    target_sr = hps['data']['sampling_rate']
    filelist = list(os.walk(sampled_audio4ft_path))[0][2]
    if target_sr != 22050:
        for wavfile in filelist:
            wav, sr = torchaudio.load(sampled_audio4ft_path + "/" + wavfile,
                                      frame_offset=0,
                                      num_frames=-1,
                                      normalize=True,
                                      channels_first=True)
            wav = torchaudio.transforms.Resample(orig_freq=sr,
                                                 new_freq=target_sr)(wav)
            torchaudio.save(sampled_audio4ft_path + "/" + wavfile,
                            wav,
                            target_sr,
                            channels_first=True)


if __name__ == "__main__":
    main()
