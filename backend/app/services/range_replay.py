"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class RangeReplayService(BaseModuleService):
    MODULE = "range_replay"
    ENTITY = "重采任务"
    OPERATION_TERM = "水位"
    LIST_FIELDS = ["重采编号", "测点编号", "起始时刻", "截止时刻", "重采原因", "覆盖方式", "重采点数", "重采水位"]
    REQUIRED_FIELDS = ["重采编号", "测点编号", "起始时刻"]
    STATUS_ORDER = ["草稿", "待重采", "重采中", "已完成", "已取消"]
    ACTION_RULES = {"启动重采": "重采中", "标记完成": "已完成", "取消重采": "已取消"}
    NEGATIVE_ACTIONS = []
