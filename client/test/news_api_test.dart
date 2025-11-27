import 'package:test/test.dart';
import 'package:client/api/generated/openapi.dart';


/// tests for NewsApi
void main() {
  final instance = Openapi().getNewsApi();

  group(NewsApi, () {
    // Testnews
    //
    //Future<JsonObject> testNewsNewsGet() async
    test('test testNewsNewsGet', () async {
      // TODO
    });

  });
}
