from fastapi import Request
from sqlalchemy import select

from api.api_v1.spider.schemas import base_schema
from database.models import Announcement18Art, Announcement42verse, AnnouncementIbox, AnnouncementLingjingsj, AnnouncementTheone, AnnouncementShuzimart
from database.async_session import async_session_local


class CRUDAuthentic:

    def __init__(self):
        pass

    @staticmethod
    async def get_announcement(*, platform: int, request: Request) -> base_schema.CRUDBaseSchema:
        async with async_session_local() as session:
            data = []
            if platform and isinstance(platform, int):
                query_sql_mapper = {
                    1: select(Announcement18Art).where(Announcement18Art.is_delete == 0),
                    2: select(Announcement42verse).where(Announcement42verse.is_delete == 0),
                    3: select(AnnouncementIbox).where(AnnouncementIbox.is_delete == 0),
                    4: select(AnnouncementLingjingsj).where(AnnouncementLingjingsj.is_delete == 0),
                    5: select(AnnouncementShuzimart).where(AnnouncementShuzimart.is_delete == 0),
                    6: select(AnnouncementTheone).where(AnnouncementTheone.is_delete == 0),
                }
                try:
                    announcements = (await session.execute(query_sql_mapper.get(platform))).scalars().all()
                    for announcement in announcements:
                        data.append(announcement.__dict__)
                except Exception as e:
                    pass
        return base_schema.CRUDBaseSchema(state=True, data=data)


crud = CRUDAuthentic()
