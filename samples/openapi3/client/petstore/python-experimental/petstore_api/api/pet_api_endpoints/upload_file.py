# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import re  # noqa: F401
import sys  # noqa: F401
import typing
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
from decimal import Decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    BoolSchema,
    FileSchema,
    NoneSchema,
    none_type,
    InstantiationMetadata,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    FileBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)

from petstore_api.model.api_response import ApiResponse

# path params
PetIdSchema = Int64Schema
RequestRequiredPathParams = typing.TypedDict(
    'RequestRequiredPathParams',
    {
        'petId': PetIdSchema,
    }
)
RequestOptionalPathParams = typing.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_pet_id = api_client.PathParameter(
    name="petId",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PetIdSchema,
    required=True,
)
# body param


class SchemaForRequestBodyMultipartFormData(
    DictSchema
):
    additionalMetadata = StrSchema
    file = FileSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        additionalMetadata: typing.Union[additionalMetadata, Unset] = unset,
        file: typing.Union[file, Unset] = unset,
        _instantiation_metadata: typing.Optional[InstantiationMetadata] = None,
        **kwargs: typing.Type[Schema],
    ):
        return super().__new__(
            cls,
            *args,
            additionalMetadata=additionalMetadata,
            file=file,
            _instantiation_metadata=_instantiation_metadata,
            **kwargs,
        )


request_body_body = api_client.RequestBody(
    content={
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
)
_path = '/pet/{petId}/uploadImage'
_method = 'POST'
_auth = [
    'petstore_auth',
]
SchemaFor200ResponseBodyApplicationJson = ApiResponse


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: Unset = unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class UploadFile(api_client.Api):

    def upload_file(
        self: api_client.Api,
        body: typing.Union[SchemaForRequestBodyMultipartFormData, Unset] = unset,
        path_params: RequestPathParams = frozendict(),
        content_type: str = 'multipart/form-data',
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization
    ]:
        """
        uploads an image
        Parameters use leading underscores to prevent collisions with user defined
        parameters from the source openapi spec
        """
        self._verify_typed_dict_inputs(RequestPathParams, path_params)

        _path_params = {}
        for parameter in (
            request_path_pet_id,
        ):
            parameter_data = path_params.get(parameter.name, unset)
            if parameter_data is unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        _fields = None
        _body = None
        if body is not unset:
            serialized_data = request_body_body.serialize(body, content_type)
            _headers.add('Content-Type', content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
        response = self.api_client.call_api(
            resource_path=_path,
            method=_method,
            path_params=_path_params,
            headers=_headers,
            fields=_fields,
            body=_body,
            auth_settings=_auth,
        )

        response_for_status = _status_code_to_response.get(str(response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(response, self.api_client.configuration)
        else:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response
