import json
import re

def process_to_sentences(samples, v = False):
    start = -1
    sub_start = -1
    sentence = ""
    sub_sentence = ""
    sentences = []
    sub_sentences = []

    for sample in samples:
        if start == -1:
            start = sample["offsets"]["from"]

        if sub_start == -1:
            sub_start = sample["offsets"]["from"]

        sentence += sample["text"]
        sub_sentence += sample["text"]
        
        now = sample["offsets"]["to"]
        # if now - sub_start > 4000:
        #     sub_sentences.append({"ms_pos": sub_start, "ms_length": now - sub_start,  "text": sub_sentence})
        #     sub_sentence = ""
        #     sub_start = -1

        if sample["text"] in [".", "?", ".\"", "?\""]:
            # if len(sub_sentences) and sub_start != -1:
            #     sub_sentences.append({"ms_pos": sub_start, "ms_length": now - sub_start,  "text": sub_sentence})

            sentences.append({"s_pos": start/1000, "s_length": (now - start)/1000,  "text": sentence})
            # sentences.append({"ms_pos": start, "ms_length": now - start,  "text": sentence, "sub_sentences": sub_sentences})
            sub_sentences = []
            sub_sentence = ""
            sub_start = -1
            sentence = ""
            start = -1

    if v:
        for sentence in sentences:
            print(sentence)
    
    return sentences

def show_short_tokens(samples, length = 2):
    tokens = {}

    for sample in samples:
        if len(sample["text"]) < length:
            if sample["text"] in tokens:
                tokens[sample["text"]] += 1
            else:
                tokens[sample["text"]] = 1

    for key in tokens:
        print(f"{key}: {tokens[key]}")


def process_to_full_text_and_split(samples, v = False):
    sliced_text = [sample["text"] for sample in samples]
    full_text = "".join(sliced_text)
    sentences = re.split(r'(?<=\. )|(?<=\? )', full_text)

    if v:
        for sentence in sentences:
            print(sentence)

def main():
    file = 'fs/_record_transcribed/hoe_math_levels_basic.json.json'
    out_sentence_file = 'fs/_video_yt_split/hoe_math_levels_basic.sentence.json'

    json_data = open(file).read()
    data = json.loads(json_data)

    samples = data['transcription']
    # process_to_full_text_and_split(samples)
    # show_short_tokens(samples, 3)
    sentence_transcription = process_to_sentences(samples, True)

    json_data = json.dumps(sentence_transcription, indent=4)

    f = open(out_sentence_file,"w")
    f.write(json_data)
    f.close()


main()




    