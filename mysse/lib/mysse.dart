import 'package:featurehub_sse_client/featurehub_sse_client.dart';

Future<void> run() async {
EventSource eventSource =
      await EventSource.connect("http://127.0.0.1:5001/stream");
  // listen for events
  eventSource.listen((Event event) {
    print("New event:");
    print("  event: ${event.event}");
    print("  data: ${event.data}");
  });
  print("New event:");
}
