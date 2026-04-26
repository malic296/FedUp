from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.article_dto import ArticleDTO


T = TypeVar("T", bound="ArticleResponse")


@_attrs_define
class ArticleResponse:
    """
    Attributes:
        success (bool):
        message (str):
        article (ArticleDTO | None):
    """

    success: bool
    message: str
    article: ArticleDTO | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.article_dto import ArticleDTO

        success = self.success

        message = self.message

        article: dict[str, Any] | None
        if isinstance(self.article, ArticleDTO):
            article = self.article.to_dict()
        else:
            article = self.article

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "article": article,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.article_dto import ArticleDTO

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        def _parse_article(data: object) -> ArticleDTO | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                article_type_0 = ArticleDTO.from_dict(data)

                return article_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ArticleDTO | None, data)

        article = _parse_article(d.pop("article"))

        article_response = cls(
            success=success,
            message=message,
            article=article,
        )

        article_response.additional_properties = d
        return article_response

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
