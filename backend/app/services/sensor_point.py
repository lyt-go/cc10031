"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class SensorPointService(BaseModuleService):
    MODULE = "sensor_point"
    ENTITY = "测点档案"
    OPERATION_TERM = "校验"
    LIST_FIELDS = ["测点编号", "所属产线", "传感器型号", "量程范围", "采样频率", "计量单位", "投运日期", "台账版本"]
    REQUIRED_FIELDS = ["测点编号", "所属产线", "传感器型号"]
    STATUS_ORDER = ["草稿", "待校验", "已投运", "已停用"]
    ACTION_RULES = {"提交校验": "待校验", "确认投运": "已投运", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
