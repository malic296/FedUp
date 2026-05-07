from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.paged_themes_dto import PagedThemesDTO
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    hours: int | Unset = 72,
    cursor: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["hours"] = hours

    json_cursor: None | str | Unset
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_page: int | None | Unset
    if isinstance(page, Unset):
        json_page = UNSET
    else:
        json_page = page
    params["page"] = json_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/themes/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | PagedThemesDTO | None:
    if response.status_code == 200:
        response_200 = PagedThemesDTO.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | PagedThemesDTO]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 72,
    cursor: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | PagedThemesDTO]:
    """Themes

    Args:
        hours (int | Unset):  Default: 72.
        cursor (None | str | Unset):
        page (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedThemesDTO]
    """

    kwargs = _get_kwargs(
        hours=hours,
        cursor=cursor,
        page=page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 72,
    cursor: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
) -> HTTPValidationError | PagedThemesDTO | None:
    """Themes

    Args:
        hours (int | Unset):  Default: 72.
        cursor (None | str | Unset):
        page (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedThemesDTO
    """

    return sync_detailed(
        client=client,
        hours=hours,
        cursor=cursor,
        page=page,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 72,
    cursor: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
) -> Response[HTTPValidationError | PagedThemesDTO]:
    """Themes

    Args:
        hours (int | Unset):  Default: 72.
        cursor (None | str | Unset):
        page (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | PagedThemesDTO]
    """

    kwargs = _get_kwargs(
        hours=hours,
        cursor=cursor,
        page=page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    hours: int | Unset = 72,
    cursor: None | str | Unset = UNSET,
    page: int | None | Unset = UNSET,
) -> HTTPValidationError | PagedThemesDTO | None:
    """Themes

    Args:
        hours (int | Unset):  Default: 72.
        cursor (None | str | Unset):
        page (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | PagedThemesDTO
    """

    return (
        await asyncio_detailed(
            client=client,
            hours=hours,
            cursor=cursor,
            page=page,
        )
    ).parsed
