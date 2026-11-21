"""__NAME__领域服务：字段、状态和动作来自业务配置，数据处理骨架由基类复用。"""
from __future__ import annotations

from app.services.base import BaseModuleService


class TierStorageService(BaseModuleService):
    MODULE = "tier_storage"
    ENTITY = "分层策略"
    OPERATION_TERM = "迁移"
    LIST_FIELDS = ["策略编号", "时间边界", "热区范围", "温区范围", "冷区路径", "迁移方式", "驻留天数", "策略版本"]
    REQUIRED_FIELDS = ["策略编号", "时间边界", "热区范围"]
    STATUS_ORDER = ["草稿", "待生效", "已生效", "已停用"]
    ACTION_RULES = {"提交生效": "待生效", "确认生效": "已生效", "标记停用": "已停用"}
    NEGATIVE_ACTIONS = []
