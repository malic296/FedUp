from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.article_dto import ArticleDTO


T = TypeVar("T", bound="ThemeDTO")


@_attrs_define
class ThemeDTO:
    """
    Attributes:
        uuid (str):
        newest_date (datetime.datetime):
        articles (list[ArticleDTO] | Unset):
    """

    uuid: str
    newest_date: datetime.datetime
    articles: list[ArticleDTO] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        newest_date = self.newest_date.isoformat()

        articles: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.articles, Unset):
            articles = []
            for articles_item_data in self.articles:
                articles_item = articles_item_data.to_dict()
                articles.append(articles_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "newest_date": newest_date,
            }
        )
        if articles is not UNSET:
            field_dict["articles"] = articles

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_dto import ArticleDTO

        d = dict(src_dict)
        uuid = d.pop("uuid")

        newest_date = isoparse(d.pop("newest_date"))

        _articles = d.pop("articles", UNSET)
        articles: list[ArticleDTO] | Unset = UNSET
        if _articles is not UNSET:
            articles = []
            for articles_item_data in _articles:
                articles_item = ArticleDTO.from_dict(articles_item_data)

                articles.append(articles_item)

        theme_dto = cls(
            uuid=uuid,
            newest_date=newest_date,
            articles=articles,
        )

        theme_dto.additional_properties = d
        return theme_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
