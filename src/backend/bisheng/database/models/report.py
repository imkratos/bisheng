from datetime import datetime
from typing import Optional

from bisheng.database.models.base import SQLModelSerializable
from sqlalchemy import Column, DateTime, text
from sqlmodel import Field


class ReportBase(SQLModelSerializable):
    # ```
    # 使用flow_id 按更新时间倒排获取最新模板的路径
    # 会存储模板生成的最终报告的记录`
    flow_id: Optional[str] = Field(index=False, description='前端展示名称')
    file_name:  Optional[str] = Field(index=False, description='生成报告存储路径')
    template_name:  Optional[str] = Field(index=False, description='报告模板数据存储路径')
    version_key: str = Field(index=True, unique=True, description='前端模板唯一key')
    object_name: str = Field(index=False)
    del_yn: int = Field(index=False, default=0, description='删除状态， 1表示删除')
    create_time: Optional[datetime] = Field(sa_column=Column(
        DateTime, nullable=False, index=True, server_default=text('CURRENT_TIMESTAMP')))
    update_time: Optional[datetime] = Field(
        sa_column=Column(DateTime,
                         nullable=False,
                         server_default=text('CURRENT_TIMESTAMP'),
                         onupdate=text('CURRENT_TIMESTAMP')))


class Report(ReportBase, table=True):
    __tablename__ = 't_report'
    id: Optional[int] = Field(default=None, primary_key=True)


class ReportRead(ReportBase):
    id: Optional[int]


class RoleUpdate(ReportBase):
    role_name: Optional[str]
    remark: Optional[str]


class RoleCreate(ReportBase):
    pass
