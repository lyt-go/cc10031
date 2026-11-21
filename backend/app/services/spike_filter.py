"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SpikeFilterService(BaseModuleService):
    MODULE = "spike_filter"
    ENTITY = "异常采样"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["异常编号", "测点编号", "采样时刻", "观测值", "量程上限", "偏离倍数", "判定窗口", "处置结论"]
    REQUIRED_FIELDS = ["异常编号", "测点编号", "采样时刻"]
    STATUS_ORDER = ["草稿", "待判定", "已判定", "已恢复"]
    ACTION_RULES = {"提交判定": "待判定", "确认剔除": "已判定", "标记恢复": "已恢复"}
    NEGATIVE_ACTIONS = []
