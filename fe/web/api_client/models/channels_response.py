from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.channel_dto import ChannelDTO


T = TypeVar("T", bound="ChannelsResponse")


@_attrs_define
class ChannelsResponse:
    """
    Attributes:
        success (bool):
        message (str):
        channels (list[ChannelDTO]):
    """

    success: bool
    message: str
    channels: list[ChannelDTO]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        channels = []
        for channels_item_data in self.channels:
            channels_item = channels_item_data.to_dict()
            channels.append(channels_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "channels": channels,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_dto import ChannelDTO

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        channels = []
        _channels = d.pop("channels")
        for channels_item_data in _channels:
            channels_item = ChannelDTO.from_dict(channels_item_data)

            channels.append(channels_item)

        channels_response = cls(
            success=success,
            message=message,
            channels=channels,
        )

        channels_response.additional_properties = d
        return channels_response

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
