import glob
import os
import pathlib
import re
import time
from argparse import ArgumentParser
import fitz

import lxml.etree as etree
import pandas as pd


# xml parsing is copied from:
# https://www.kaggle.com/code/yutongzhang20080108/full-regex-based-solution
def xml_kind(xml_path: pathlib.Path):
    head = xml_path.open("rb").read(2048).decode("utf8", "ignore")
    if "www.tei-c.org/ns" in head:
        return "tei"
    if re.search(r"(NLM|TaxonX)//DTD", head):
        return "jats"
    if "www.wiley.com/namespaces" in head:
        return "wiley"
    if "BioC.dtd" in head:
        return "bioc"
    return "unknown"


def xml2txt(xml_dir):
    article_ids = []
    article_texts = []
    for xml in os.listdir(xml_dir):
        xml_path = pathlib.Path(os.path.join(xml_dir, xml))
        kind = xml_kind(xml_path)
        root = etree.parse(str(xml_path)).getroot()
        if kind in ("tei", "bioc", "unknown"):
            text = " ".join(root.itertext())
        elif kind == "jats":
            elems = root.xpath("//body//sec|//ref-list")
            text = " ".join("\n".join(e.itertext()) for e in elems)
        elif kind == "wiley":
            elems = root.xpath('//*[local-name()="body"]|//*[local-name()="refList"]')
            text = " ".join("\n".join(e.itertext()) for e in elems)
        else:
            text = " ".join(root.itertext())

        article_ids.append(xml.split(".xml")[0].strip())
        article_texts.append(text)
    return pd.DataFrame({"article_id": article_ids, "text": article_texts})


def pdf2txt(pdf_dir: pathlib.Path):
    article_ids = []
    article_texts = []
    for pdf in os.listdir(pdf_dir):
        article_ids.append(pdf.split(".pdf")[0].strip())
        pdf_path = os.path.join(pdf_dir, pdf)

        with fitz.open(pdf_path) as doc:
            text = []
            for page in doc:
                page_text = page.get_text()  # type: ignore
                text.append(page_text)
            article_texts.append(f"\n{'='*60}\n".join(text))

    return pd.DataFrame({"article_id": article_ids, "text": article_texts})


def main(args: dict):
    # text extraction from pdf
    try:
        pdf_texts_df = pdf2txt(args["PDF_DIR"])
        pdf_texts_df.to_csv(args["OUTPUT_DIR"] / "texts_pdf.csv", index=False)
    except Exception as e:
        print(f"Unable to get texts (pdf):\n{e}")
        return time.time()

    # text extraction from pdf
    try:
        xml_texts_df = xml2txt(args["XML_DIR"])
        xml_texts_df.to_csv(args["OUTPUT_DIR"] / "texts_xml.csv", index=False)
    except Exception as e:
        print(f"Unable to get texts (xml):\n{e}")
        raise e

    return time.time()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--XML_DIR", type=pathlib.Path)
    parser.add_argument("--PDF_DIR", type=pathlib.Path)
    parser.add_argument("--OUTPUT_DIR", type=pathlib.Path)

    args = vars(parser.parse_args())
    valid_args: dict[str, bool] = {k: os.path.exists(v) for k, v in args.items()}
    assert all(
        valid_args.values()
    ), f"Invalid path is provided for:\n{[k for k, v, in valid_args.items() if v is False]}"

    time_start = time.time()
    time_end = main(args)
    solution_time = time_end - time_start

    print(f"Solution finished in {solution_time:.2f}s")


"""
\n(references|data availability (statement)?|data and methods|methods and data|availability of data (and materials?)?)\b
\b(secnerefer|(tnemetats)? ytilibaliava atad|sdohtem dna atad|atad dna sdohtem|(s?lairetam dna)? atad fo ytilibaliava)\n
"""


"""
gbif
fasta
"""
