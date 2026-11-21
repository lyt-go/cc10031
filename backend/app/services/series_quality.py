"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SeriesQualityService(BaseModuleService):
    MODULE = "series_quality"
    ENTITY = "质量报告"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["报告编号", "测点编号", "统计窗口", "完整率", "重复点数", "越界点数", "校验规则", "质检结论"]
    REQUIRED_FIELDS = ["报告编号", "测点编号", "统计窗口"]
    STATUS_ORDER = ["草稿", "待质检", "质检中", "已出报告"]
    ACTION_RULES = {"启动质检": "待质检", "出具报告": "已出报告", "标记驳回": "已出报告"}
    NEGATIVE_ACTIONS = []
