"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class UnitCalibrateService(BaseModuleService):
    MODULE = "unit_calibrate"
    ENTITY = "标定记录"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["标定编号", "测点编号", "原始单位", "目标单位", "换算系数", "零点偏移", "标定方式", "标定时间"]
    REQUIRED_FIELDS = ["标定编号", "测点编号", "原始单位"]
    STATUS_ORDER = ["草稿", "待标定", "已标定", "已失效"]
    ACTION_RULES = {"提交标定": "待标定", "确认标定": "已标定", "标记失效": "已失效"}
    NEGATIVE_ACTIONS = []
