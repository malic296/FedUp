from dataclasses import dataclass
from typing import Optional

@dataclass
class Channel:
    uuid: str
    title: str
    link: str
    logo_url: str
    disabled_by_user: bool = False
    id: Optional[int] = None
