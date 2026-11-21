"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class UploadBatchService(BaseModuleService):
    MODULE = "upload_batch"
    ENTITY = "上送批次"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["批次编号", "分片范围", "测点数量", "记录条数", "压缩方式", "批次校验值", "上送时长", "批次水位"]
    REQUIRED_FIELDS = ["批次编号", "分片范围", "测点数量"]
    STATUS_ORDER = ["草稿", "待上送", "上送中", "已完成", "已失败"]
    ACTION_RULES = {"启动上送": "上送中", "标记完成": "已完成", "标记失败": "已失败"}
    NEGATIVE_ACTIONS = []
