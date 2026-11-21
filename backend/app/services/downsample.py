"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class DownsampleService(BaseModuleService):
    MODULE = "downsample"
    ENTITY = "降采样任务"
    OPERATION_TERM = "聚合"
    LIST_FIELDS = ["任务编号", "源序列", "源采样频率", "目标频率", "聚合方式", "输出点数", "压缩比", "任务水位"]
    REQUIRED_FIELDS = ["任务编号", "源序列", "源采样频率"]
    STATUS_ORDER = ["草稿", "待执行", "执行中", "已完成"]
    ACTION_RULES = {"启动执行": "执行中", "标记完成": "已完成", "标记失败": "已完成"}
    NEGATIVE_ACTIONS = []
