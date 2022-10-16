from fastapi import APIRouter, Depends
import jieba
from common.baseitem import CutWorldsEnum
# import paddlehub as hub


router = APIRouter()
# senta_global = hub.Module(name="senta_cnn")


def get_cut_worlds_enum(num: int):
    temp_map = CutWorldsEnum._value2member_map_
    if num not in temp_map:
        num = 1
    return temp_map[num]


@router.get('/split2worlds')
def split_to_words(content: str, model: CutWorldsEnum = Depends(get_cut_worlds_enum)):
    """ Description 分割语句为词语

    :type content:str: 分词的内容
    :param content:str:

    :type model:CutWorldsEnum: 分割词语的模式
    :param model:CutWorldsEnum: 1-> 精确模式, 2-> 全模式, 3-> 搜索模式, other-> 1

    :raises:

    :rtype:
    """
    result = []
    if model is CutWorldsEnum.accurate:
        result = jieba.lcut(content)
    elif model is CutWorldsEnum.all_cut:
        result = jieba.lcut(content, cut_all=True)
    elif model is CutWorldsEnum.search:
        result = jieba.lcut_for_search(content)
    return {'result': result, 'model': model.name}


# @router.get('/senta')
# def senta(content: str):
#     """ Description 语句情绪分析

#     :type content:str: 分析的语句内容
#     :param content:str:

#     :raises:

#     :rtype:
#     """
#     results = senta_global.sentiment_classify(texts=[content], use_gpu=False, batch_size=1)
#     return {'result': results, 'model': 'senta_cnn'}
