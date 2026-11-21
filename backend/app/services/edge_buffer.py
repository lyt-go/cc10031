"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class EdgeBufferService(BaseModuleService):
    MODULE = "edge_buffer"
    ENTITY = "缓冲分片"
    OPERATION_TERM = "水位"
    LIST_FIELDS = ["分片编号", "测点编号", "起始时刻", "结束时刻", "采样点数", "缓冲字节", "落盘方式", "分片水位"]
    REQUIRED_FIELDS = ["分片编号", "测点编号", "起始时刻"]
    STATUS_ORDER = ["草稿", "缓冲中", "已落盘", "已上送"]
    ACTION_RULES = {"启动落盘": "缓冲中", "确认上送": "已上送", "标记丢失": "已落盘"}
    NEGATIVE_ACTIONS = []
