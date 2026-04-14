# Make Data Count - Finding Data References
<img width="560" height="279" alt="image" src="https://github.com/user-attachments/assets/4d9af4d1-67e9-4a05-9924-0e18042198d2" />

# Overview
Your efforts can help Make Data Count (MDC). Scientific data are critically undervalued even though they provide the basis for discoveries and innovations. We aim to improve our understanding of the links between scientific papers and the data used in those studies—what, when, and how they are mentioned. This will help to establish the value and impact of open scientific data for reuse. The current version of the MDC Data Citation Corpus is an aggregation of links between data and papers, but these links are incomplete: they only cover a fraction of the literature and do not provide context on how the data were used. The outcome of this competition is a highly performant model that will continuously run on scientific literature to automate the addition of high quality and contextualized data-to-paper connections in to the MDC Data Citation Corpus.

# Description
## Goal of the competition
You will identify all the data citations (references to research data) from the full text of scientific literature and tag the type of citation (primary or secondary):
- Primary: Raw or processed data generated as part of the paper, specifically for the study.
- Secondary: Raw or processed data derived or reused from existing records or published data.
## Context
Make Data Count (MDC) is a global, community-driven initiative focused on establishing open standardized metrics for the evaluation and reward of research data reuse and impact. Through both advocacy and infrastructure projects, Make Data Count facilitates the recognition of data as a primary research output, promoting data sharing and reuse across data communities.

Highlighting and valuing data contributions will lead to a more collaborative, transparent, and efficient science, ultimately driving innovation and progress. To assure that this can happen, we need to connect and contextualize data, their relationship to papers, and their reuse.

# Why this is not YET a solved problem
Studies have shown that most research data remain “uncited” (~86 %) (Peters, I., Kraker, P., Lex, E. et al., 2016, https://doi.org/10.1007/s11192-016-1887-4) in the current data citation system which makes it very hard to identify and record them. In addition, references to data are harder to programmatically identify because of the many ways they are mentioned. For example, authors may provide a full description of the data in the methods section, they may indirectly mention it elsewhere, or provide a formal citation in the reference list. Additionally, authors may use variable language when describing the type of relationship between the data and paper, such as suggesting data their data are openly available (“publicly available”) or mentioning the data were obtained from elsewhere (for instance, “obtained from”).

# Potential Impact
The winning Kaggle model will enable MDC to update, release, and maintain an open, comprehensive and high quality set of references to data in scientific papers. The subsequent corpus will be made freely available for use by research communities, allowing for the development of better tools, a better understanding of how data are reused, improved ways of capturing broader researcher outputs, and a shift towards valuing data.

# Evaluation
In this competition, the metric is F1-Score. The F1-score, commonly used in information retrieval, measures accuracy using the statistics precision (p) and recall (r). Precision is the ratio of true positives (tp) to all predicted positives (tp + fp). Recall is the ratio of true positives to all actual positives (tp + fn). The F1 score is given by:
<img width="466" height="166" alt="Screenshot 2026-04-14 131230" src="https://github.com/user-attachments/assets/0db56838-9e73-4b1d-ac2b-e373187f0606" />

The F1 metric weights recall and precision equally, and a good retrieval algorithm will maximize both precision and recall simultaneously. Thus, moderately good performance on both will be favored over extremely good performance on one and poor performance on the other.

# Submission File
You must identify data references contained in the test dataset. These predictions form unique tuples of (article_id, dataset_id, type). If an article contains multiple references of the same dataset_id and type, it should only be predicted once. Only articles containing data references be included in submissions. Articles with no data references should not be included in the submission, and will be penalized as false positives if they are. When mining the research paper full text, the DOIs may appear with or without the 'https://doi.org' stem. Convert all DOIs into the full DOI format in the submission (https://doi.org/[prefix]/[suffix]). The file should contain a header and use the following format:
<img width="449" height="91" alt="Screenshot 2026-04-14 131346" src="https://github.com/user-attachments/assets/5713c03b-d418-4f90-a039-0f10e40008c9" />
