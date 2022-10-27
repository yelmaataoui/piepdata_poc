from extract_utils import *
from transform_utils import *
from load_utils import *
from post_treatment_feature_utils import *

clinical_trials = extract("clinical_trials.csv")
drugs = extract("drugs.csv")
pubmed = extract("pubmed.csv")

graph_liaison = transform(drugs, clinical_trials, pubmed)

load(graph_liaison, "graph_liaison3.json")

print(journals_more_drugs_publish("graph_liaison3.json"))
