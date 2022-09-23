import os
from glob import glob
from tqdm import tqdm
import re
import json
from multiprocessing import Pool


# TODO: Re-write main operation to be adjusted to any file path or dir

WRITE_FILE = "./korean_corpus.txt"


def cleanse_corpus(txt):
    def convert_to_comma(txt):
        special_char = ["▲", "△", "◇"]
        for c in special_char:
            if txt.count(c) > 1:
                split_txt = txt.split(c)
                split_txt = [split_txt[0] + split_txt[1]] + split_txt[2:]
                result_txt = re.sub(r"\s,", ",", ", ".join(split_txt))
                return result_txt
        return txt
    # listed (not with comma) case
    txt = convert_to_comma(txt)
    # journal and reporter case
    txt = re.sub(r"[\[\(【].*=.*[\]\)】][\s가-힣\(\)]+=", " ", txt)
    # copyright case with bracket
    txt = re.sub(r"<저작.*금지.*>", " ", txt)
    # journal name with email case
    txt = re.sub(r"◎[\s가-힣ㄱ-ㅎa-zA-Z]+@\(이메일\)", " ", txt)
    # raw email case
    txt = re.sub(r"[a-zA-Z0-9]+@\([가-힣]+\)", " ", txt)
    # html tag case
    txt = re.sub(r"</[a-zA-Z]+.*[가-힣]>", " ", txt)
    # copyright with special char case in korean
    txt = re.sub(r"<[\s가-힣0-9\(\)]+[\=ⓒ][가-힣a-zA-Z0-9\s]+>", " ", txt)
    # copyright alarm case
    txt = re.sub(r"무단\s.*재배포.*\s금지", " ", txt)
    # copyright with special char case
    txt = re.sub(r"copyright.*ⓒ.*\([가-힣]+\)", " ", txt)
    # start-with-special-char case
    txt = re.sub(r"^[^가-힣ㄱ-ㅎa-zA-Z0-9]", " ", txt)
    # hyperlink case
    txt = re.sub(r"\(www\..*\.[a-z]+\)", " ", txt)
    # money week case
    txt = re.sub(r"☞[\s가-힣ㄱ-ㅎ]+<머니위크>.*입니다\.", "", txt)

    txt = re.sub(r"\(\\[a-zA-Z0-9]+\)", "", txt)
    

    # unnecessary word after all followed filtering
    txt = txt.replace("(사진)", "")
    txt = txt.replace("(이메일)", "")
    txt = txt.replace("◎공감언론 뉴시스", "")

    txt = txt.replace("\n", " ")

    # mixture of dot and space case
    txt = re.sub(r"\.\s+\.", "", txt)
    txt = re.sub(r"\.{2,}", ".", txt)
    txt = txt.replace(" .", ".")

    txt = " ".join(txt.split())
    return txt


def save_sent_text(path):
    with open(path, "r") as f:
        dict_file = json.load(f)["SJML"]["text"]
    for doc in tqdm(dict_file, total=len(dict_file)):
        content = cleanse_corpus(doc["content"])
        sents = re.sub(r"\.[\s]", ".\n", content)
        with open(WRITE_FILE, "a") as txt:
            txt.write(sents)
            txt.write("\n\n")


if __name__ == "__main__":
    raw_json_path = []
    base_train_raw = "./data/Training/raw/TS1/"
    base_valid_raw = "./data/Validation/raw/VS1/"
    train_raw_cat = glob(os.path.join(base_train_raw, "*"))
    valid_raw_cat = glob(os.path.join(base_valid_raw, "*"))
    all_row_dir = train_raw_cat + valid_raw_cat
    for path in all_row_dir:
        curr_path = sorted(glob(os.path.join(path, "*")))
        raw_json_path.extend(curr_path)

    pool = Pool(processes=os.cpu_count())
    pool.map(save_sent_text, raw_json_path)
    pool.close()
    pool.join()