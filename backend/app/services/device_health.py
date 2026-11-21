"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class DeviceHealthService(BaseModuleService):
    MODULE = "device_health"
    ENTITY = "心跳记录"
    OPERATION_TERM = "采集"
    LIST_FIELDS = ["心跳编号", "采集终端", "上报时刻", "间隔秒数", "丢包次数", "缓存积压", "判定阈值", "心跳状态"]
    REQUIRED_FIELDS = ["心跳编号", "采集终端", "上报时刻"]
    STATUS_ORDER = ["草稿", "正常", "异常", "已失联"]
    ACTION_RULES = {"标记正常": "正常", "标记异常": "异常", "标记失联": "已失联"}
    NEGATIVE_ACTIONS = []
