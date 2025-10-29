# openapi.api.NewsApi

## Load the API package
```dart
import 'package:openapi/api.dart';
```

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testNewsNewsGet**](NewsApi.md#testnewsnewsget) | **GET** /news/ | Testnews


# **testNewsNewsGet**
> JsonObject testNewsNewsGet()

Testnews

### Example
```dart
import 'package:openapi/api.dart';

final api = Openapi().getNewsApi();

try {
    final response = api.testNewsNewsGet();
    print(response);
} catch on DioException (e) {
    print('Exception when calling NewsApi->testNewsNewsGet: $e\n');
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JsonObject**](JsonObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

