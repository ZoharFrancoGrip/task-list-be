from dataclasses import Field
from typing import List, Optional
from enum import Enum
import json
import os
from datetime import datetime
from pydantic import BaseModel


class TaskPriority(str, Enum):
    Low = "Low"
    Medium = "Medium"
    High = "High"

class TaskType(str, Enum):
    Bug = "Bug"
    Feature = "Feature"
    Task = "Task"

class TaskStatus(str, Enum):
    ToDo = "TODO"
    InProgress = "In Progress"
    Blocked = "Blocked"
    Done = "Done"

class TaskDifficulty(str, Enum):
    Easy = "Easy"
    Medium = "Medium"
    Hard = "Hard"


class Task(BaseModel):
    id: int
    title: str
    description: str
    priority: TaskPriority
    status: TaskStatus
    type: TaskType
    difficulty: TaskDifficulty
    createdAt: str
