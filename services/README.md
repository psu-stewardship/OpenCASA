identity.mint()
	should do:
	      curl -iH "Content-Type: application/json" -X POST -d '{}' http://localhost:8000/api/v0/identifier/
	parse resource URI from Location header, then:
	      curl -iH "Accept: application/json" http://localhost:8000/api/v0/identifier/1/
	parse json:
	      {"name": "ark:/42409/rz10p822b", "resource_uri": "/api/v0/identifier/1/"}

annotate.add(identifier, assertions)
annotate.remove(assertion_identifier)
annotate.update(assertion_identifier, property, value);

storage.list_versions(identifier)
storage.ingest_directory(identifier, directory)
storage.validate_object(identifier)

