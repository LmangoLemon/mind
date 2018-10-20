import sys

import importlib as importlib
from time import sleep

import yaml
from cct.engine import Engine
from cct.testset import TestSet


def load_case():
    data = None
    with open('./testset.yml') as f:
        data = yaml.load(f)
    return data


def get_case_instance(path):
    name = 'cct.cases.{module_name}'.format(module_name=path)

    module = importlib.import_module(name)

    case = getattr(module, path)
    return case


def get_cases():
    ts_data = load_case()
    case_dict = {}
    for case in ts_data.get('cases'):
        id=case.get('id')
        name=case.get('name')
        dep=case.get('dependence')
        process_at=case.get('process_at')
        case_dict[case.get('id')] = get_case_instance(case.get('path'))(id,name,dep,process_at,)
    return case_dict


if __name__ == '__main__':
    cases = get_cases()

    ts = TestSet(cases)
    engine = Engine(test_set=ts)
    engine.start()