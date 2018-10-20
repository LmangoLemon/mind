# -*- coding: utf-8 -*-
import logging
import sys

import importlib as importlib
from time import sleep

import yaml
from cct.engine import Engine
from cct.testset import TestSet

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

logger = logging.getLogger(__file__)


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
        id = case.get('id')
        name = case.get('name')
        dep = case.get('dependence')
        process_at = case.get('process_at')
        case_dict[case.get('id')] = get_case_instance(case.get('path'))(id, name, dep, process_at, )
    return case_dict


def init_log():
    # 创建一个日志器logger并设置其日志级别为DEBUG
    logger.setLevel(logging.DEBUG)

    # 创建一个流处理器handler并设置其日志级别为DEBUG
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)

    # 创建一个格式器formatter并将其添加到处理器handler
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    # 为日志器logger添加上面创建的处理器handler
    logger.addHandler(handler)


if __name__ == '__main__':
    # init_log()
    cases = get_cases()
    ts = TestSet(cases)
    engine = Engine(test_set=ts)
    engine.start()
