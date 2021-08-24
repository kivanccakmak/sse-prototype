import 'package:featurehub_sse_client/featurehub_sse_client.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

Future<http.Response> httpJsonPost(String url, Map data) async {
  var response = http.post(
      Uri.parse(url),
      headers: <String, String> {
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: json.encode(data));
  return response;
}

Future<http.Response> httpJsonPostToken(String path, Map data, String token, String url) async {

  var response = http.post(
      Uri.parse(url),
      headers: <String, String> {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': token,
      },
      body: json.encode(data));
  return response;
}

Future<http.Response> Login(username, pass, url) async {
  var response;


  Map<String, String> data = new Map();

  data['username'] = username;
  data['password'] = pass;

  print(url);
  response = await httpJsonPost(url, data);
  return response;



}

Future<void> run() async {
	var accessToken;
	var jsonResponse;
	var response = await Login("kivanc", "1234", "http://127.0.0.1:5001/rest/login");
	jsonResponse = json.decode(response.body);
	if (jsonResponse.containsKey('access_token')) {
		accessToken = 'Bearer ' + jsonResponse["access_token"];
		print(accessToken);
	} else {
		return;
	}

/*EventSource eventSource =*/
      /*await EventSource.connect("http://127.0.0.1:5001/stream");*/
  /*// listen for events*/
  /*eventSource.listen((Event event) {*/
    /*print("New event:");*/
    /*print("  event: ${event.event}");*/
    /*print("  data: ${event.data}");*/
  /*});*/
  /*print("New event:");*/
}
