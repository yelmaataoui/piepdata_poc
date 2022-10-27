import re

def extract_df_contains_drug(drug, dataframe, title_column):
    '''filter the dataframe by the given drug'''
    dataframe['title_lower'] = dataframe[title_column].str.lower()
    dataframe[drug] = dataframe["title_lower"].map(lambda x: bool(re.search( drug.lower() , x)))
    df_contains_drug  =   dataframe[dataframe[drug]== True]
    return df_contains_drug

def related_elements_from_df(dataframe, elem_column):
    '''return elements (pubmed, journals or clinical trials) linked to the given drug'''
    dataframe_filtred = dataframe[[elem_column, 'date']]
    related_elements_value =  list(set(dataframe_filtred.itertuples(index=False, name=None)))
    return related_elements_value

def transform(drugs_df, clinicaltrials_df, pubmed_df):
    '''transform the df inputs to the graph liaison'''
    lst_drugs = drugs_df['drug']
    graph_liason_by_drug_values = []
    for drug in lst_drugs:
        clinicaltrials_contains_drug = extract_df_contains_drug(drug, clinicaltrials_df, 'scientific_title')
        pubmed_contains_drug = extract_df_contains_drug(drug, pubmed_df, 'title')
        clinicaltrials_values = related_elements_from_df(clinicaltrials_contains_drug, 'id')
        pubmed_values = related_elements_from_df(pubmed_contains_drug, 'id')
        journals_clinicaltrials = related_elements_from_df(clinicaltrials_contains_drug, 'journal')
        journals_pubmed = related_elements_from_df(pubmed_contains_drug, 'journal')
        journals_values = list(set(journals_pubmed + journals_clinicaltrials))
        value_drug = {"journals": journals_values, "clinical_trials":clinicaltrials_values, "pubmed":pubmed_values}  
        graph_liason_by_drug_values.append(value_drug)
    graph_liaison_output = dict(zip(lst_drugs,graph_liason_by_drug_values))
    return graph_liaison_output
        