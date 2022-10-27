import json

def read_json(file_input):
    '''read the output json'''
    f = open(file_input)
    graph_liaison_read = json.load(f)
    return graph_liaison_read

def add_drug_number_to_journal_dict(dict_input, key):
    '''append drug number to the given journal'''
    if key in dict_input.keys():
        new_value = dict_input[key] + 1
        dict_input[key] = new_value
    else: 
        dict_input.update({key : 1})
    return dict_input

def journals_more_drugs_publish(json_graph_liaiason_file):
    '''return the journals with the most of drugs publications'''
    graph_liaison_read = read_json(json_graph_liaiason_file)
    drug_values = list(graph_liaison_read.values())
    dict_journals =  {}
    for i  in (range(len(drug_values))):
        lst_drug_journals = []
        for elem in drug_values[i]['journals']:
            lst_drug_journals.append(elem[0].replace('\\xc3\\x28', ''))
        for key in set(lst_drug_journals):
            add_drug_number_to_journal_dict(dict_journals, key )
    max_keys = [key for key, value in dict_journals.items() if value == max(dict_journals.values())]
    return(max_keys)