"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SeriesSnapshotService(BaseModuleService):
    MODULE = "series_snapshot"
    ENTITY = "版本快照"
    OPERATION_TERM = "归并"
    LIST_FIELDS = ["快照编号", "口径说明", "测点范围", "时间范围", "序列条数", "生成方式", "快照水位", "生成时间"]
    REQUIRED_FIELDS = ["快照编号", "口径说明", "测点范围"]
    STATUS_ORDER = ["草稿", "待确认", "已发布", "已归档"]
    ACTION_RULES = {"提交确认": "待确认", "发布快照": "已发布", "标记归档": "已归档"}
    NEGATIVE_ACTIONS = []
