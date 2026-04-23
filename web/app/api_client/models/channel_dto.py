from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChannelDTO")


@_attrs_define
class ChannelDTO:
    """
    Attributes:
        uuid (str):
        title (str):
        link (str):
        disabled_by_user (bool):
    """

    uuid: str
    title: str
    link: str
    disabled_by_user: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        title = self.title

        link = self.link

        disabled_by_user = self.disabled_by_user

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "title": title,
                "link": link,
                "disabled_by_user": disabled_by_user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        uuid = d.pop("uuid")

        title = d.pop("title")

        link = d.pop("link")

        disabled_by_user = d.pop("disabled_by_user")

        channel_dto = cls(
            uuid=uuid,
            title=title,
            link=link,
            disabled_by_user=disabled_by_user,
        )

        channel_dto.additional_properties = d
        return channel_dto

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
