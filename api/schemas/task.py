from typing import Optional

from pydantic import BaseModel, Field
# BaseModelはFastAPIのスキーマモデル
# Taskクラスはid,title,doneの３フィールドを持ち、int Optinal[string]boolの型を持つ
# 右辺のFieldは最初の変数はフィールドのデフォルト値を表します。 title は None 、 done は False をデフォルト値をとる
class TaskBase(BaseModel):
    title: Optional[str] = Field(None,example="クリーニングを取りに行く")
    
class TaskCreate(TaskBase):
        pass

class TaskCreateResponse(TaskCreate):
    id: int
        
class Config:
    orm_mode = True
    
class Task(TaskBase):
    id: int
    done: bool = Field(False,description="完了フラグ")
    
class Config:
    orm_mode = True
    