from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.consumer_dto import ConsumerDTO


T = TypeVar("T", bound="ConsumerResponse")


@_attrs_define
class ConsumerResponse:
    """
    Attributes:
        success (bool):
        message (str):
        consumer (ConsumerDTO):
    """

    success: bool
    message: str
    consumer: ConsumerDTO
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        consumer = self.consumer.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "message": message,
                "consumer": consumer,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consumer_dto import ConsumerDTO

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message")

        consumer = ConsumerDTO.from_dict(d.pop("consumer"))

        consumer_response = cls(
            success=success,
            message=message,
            consumer=consumer,
        )

        consumer_response.additional_properties = d
        return consumer_response

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
