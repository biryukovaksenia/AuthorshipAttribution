import stanza
import pandas as pd
from tqdm import tqdm
from multiprocessing import Pool, cpu_count

stanza.download('en')
stanza.download('ru')

nlp_en = stanza.Pipeline('en', processors='tokenize,pos,lemma,depparse', use_gpu=True)
nlp_ru = stanza.Pipeline('ru', processors='tokenize,pos,lemma,depparse', use_gpu=True)


def process_text(item):
    text = item['text']
    lang = item['language']

    if lang == 'en':
        doc = nlp_en(text)
    elif lang == 'ru':
        doc = nlp_ru(text)
    else:
        raise ValueError(f"Unsupported language: {lang}")

    data = []
    for sentence in doc.sentences:
        tokens = [word.text for word in sentence.words]
        lemmas = [word.lemma for word in sentence.words]
        pos_tags = [word.upos for word in sentence.words]
        dependencies = [word.deprel for word in sentence.words]
        heads = [sentence.words[word.head - 1].text if word.head > 0 else 'ROOT' for word in sentence.words]

        data.append({
            'Text_ID': item['text_id'],
            'Sentence_Number': sentence.index + 1,
            'Sentence': sentence.text,
            'Tokens': tokens,
            'Lemmas': lemmas,
            'POS_Tags': pos_tags,
            'Dependencies': dependencies,
            'Heads': heads,
            'Language': lang
        })
    return data


def read_texts_from_file(file_path, lang):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        texts = content.split('\n\n')
    return [{'text': text, 'language': lang, 'text_id': i+1} for i, text in enumerate(texts) if text.strip()]


def main():
    texts_en = read_texts_from_file('/data/en/Lolita_en.txt', 'en')
    texts_ru = read_texts_from_file('/data/ru/Lolita_ru.txt', 'ru')

    texts = texts_en + texts_ru

    with Pool(cpu_count()) as pool:
        all_data = list(tqdm(pool.imap_unordered(process_text, texts), total=len(texts), desc="Processing texts"))

    flat_data = [item for sublist in all_data for item in sublist]
    df = pd.DataFrame(flat_data)
    df.to_csv('lolita_syntactic_dependencies.csv', index=False)


if __name__ == "__main__":
    main()
