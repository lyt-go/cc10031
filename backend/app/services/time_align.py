"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TimeAlignService(BaseModuleService):
    MODULE = "time_align"
    ENTITY = "对齐规则"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["规则编号", "对齐粒度", "时区基准", "插值方式", "容许偏移", "对齐条数", "未对齐条数", "规则版本"]
    REQUIRED_FIELDS = ["规则编号", "对齐粒度", "时区基准"]
    STATUS_ORDER = ["草稿", "待生效", "已生效", "已废弃"]
    ACTION_RULES = {"提交生效": "待生效", "确认生效": "已生效", "标记废弃": "已废弃"}
    NEGATIVE_ACTIONS = []
