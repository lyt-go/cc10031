"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class IngestWatermarkService(BaseModuleService):
    MODULE = "ingest_watermark"
    ENTITY = "水位标记"
    OPERATION_TERM = "接入"
    LIST_FIELDS = ["水位编号", "测点编号", "事件时间水位", "处理时间水位", "滞后秒数", "迟到点数", "推进方式", "检查时间"]
    REQUIRED_FIELDS = ["水位编号", "测点编号", "事件时间水位"]
    STATUS_ORDER = ["草稿", "正常", "滞后", "已停止"]
    ACTION_RULES = {"标记正常": "正常", "标记滞后": "滞后", "停止推进": "已停止"}
    NEGATIVE_ACTIONS = []
