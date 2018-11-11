# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__file__)
step = {
    'flow_list': [
        {
            'type': 'fault',
            'case_list': [
                None,
                {
                    'id': '333',
                    'name': 'node_fault',
                    'model': {

                    }
                },
            ]
        },
        {
            'type': 'service',
            'case_list': [
                {
                    'id': '111',
                    'name': 'create_lun',
                    'model': {

                    }
                },
                {
                    'id': '222',
                    'name': 'create_snap',
                    'model': {

                    }
                },
            ]
        }
    ]
}


def pares_step(step):
    """
    找到每个bbt的依赖关系，用例结果依赖和并发依赖

    :return:
    """

    # 先搞业务流
    ret = []

    flow_service = get_case_list(step, 'service')
    flow_fault = get_case_list(step, 'service')
    flow_io = get_case_list(step, 'service')
    for i in range(len(flow_service.case_list)):
        if i == 0:
            if flow_service[0]:
                ret.append(Case())
        else:
            # check left has service or not
            left_node = 1

    pass


def make_dependence(x, y, step):
    case = get_case(x, y, step)
    if case:
        if x == 0 and is_service(step, y):
            pass
        else:

            pass
    else:
        return None


def get_first_service_case():
    pass


def handle_service_node(case,x, step):
    left_nodes = get_left_nodes(x, step)
    if left_nodes:
        if contains_service_node():
            case.set_dep_rst(get_first_service_case())

        pass
    else:

        pass


def contains_service_node(case_list):
    pass


def get_left_nodes(x, y, step):
    ret = []
    if x > 0:
        for index in [index for index in range(len(step.flow_list)) if index != y]:
            ret.append(step.flow_list[index][x])
        return ret
    else:
        logger.error("invalid x={x}".format(x=x))

        return None


def is_service(step, y):
    return step.flow_list[y] == 'service'


def get_case(x, y, step):
    # TODO add the additional prop type for next process
    return step.flow_list[y].case_list[x]


def get_case_type(y, step):
    return step.flow_list[y].type


def get_case_list(step, flow_type):
    for flow in step.flow_list:
        if flow.type == flow_type:
            return flow
    return None


def to_test_set():
    pass


class Case:
    def __init__(self, dep_rst=None, dep_op=None):
        self.dep = {
            'result': None,
            'op': None

        }

    pass


a = None
print(len(a))
