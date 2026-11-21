"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SeriesExportService(BaseModuleService):
    MODULE = "series_export"
    ENTITY = "导出任务"
    OPERATION_TERM = "导出"
    LIST_FIELDS = ["导出编号", "测点范围", "时间范围", "导出格式", "采样粒度", "记录条数", "分片大小", "导出水位"]
    REQUIRED_FIELDS = ["导出编号", "测点范围", "时间范围"]
    STATUS_ORDER = ["草稿", "待导出", "导出中", "已交付"]
    ACTION_RULES = {"启动导出": "导出中", "确认交付": "已交付", "标记失败": "已交付"}
    NEGATIVE_ACTIONS = []
