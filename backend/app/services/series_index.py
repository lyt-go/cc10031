"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SeriesIndexService(BaseModuleService):
    MODULE = "series_index"
    ENTITY = "索引分区"
    OPERATION_TERM = "存储"
    LIST_FIELDS = ["索引编号", "测点编号", "时间分区", "点区间", "索引粒度", "索引条数", "存储位置", "索引版本"]
    REQUIRED_FIELDS = ["索引编号", "测点编号", "时间分区"]
    STATUS_ORDER = ["草稿", "待构建", "已构建", "已失效"]
    ACTION_RULES = {"启动构建": "待构建", "确认构建": "已构建", "标记失效": "已失效"}
    NEGATIVE_ACTIONS = []
