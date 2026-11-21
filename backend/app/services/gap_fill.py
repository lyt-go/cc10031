"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class GapFillService(BaseModuleService):
    MODULE = "gap_fill"
    ENTITY = "填补区间"
    OPERATION_TERM = "水位"
    LIST_FIELDS = ["区间编号", "测点编号", "缺失起点", "缺失终点", "缺失点数", "填补方法", "填补置信度", "区间水位"]
    REQUIRED_FIELDS = ["区间编号", "测点编号", "缺失起点"]
    STATUS_ORDER = ["草稿", "待填补", "已填补", "已放弃"]
    ACTION_RULES = {"启动填补": "待填补", "确认填补": "已填补", "标记放弃": "已放弃"}
    NEGATIVE_ACTIONS = []
