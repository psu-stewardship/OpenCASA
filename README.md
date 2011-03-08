OpenCASA (Open Curatorial and Archival Services Architecture)
=============================================================
OpenCASA is a service architecture, built upon open standards and open source software, providing curatorial and archival functions to applications, such as for ingest, management, discovery, and publishing of digital objects.  Services in OpenCASA are influenced by the (University of California Curation Center's model of microservices)[http://www.cdlib.org/services/uc3/curation/], and perform such functionality as minting and binding durable identifiers, storing arbitrary file structures, versioning, file integrity checking, annotating objects with metadata assertions, and auditing/provenance logging.  

OpenCASA is being developed as part of (Penn State's Digital Stewardship Program)[http://stewardship.psu.edu/].  Development on OpenCASA began as part of the prototype (CAPS project)[http://stewardship.psu.edu/2011/02/caps-a-curation-platform-prototype.html]. Code is freely available via (Github)[http://github.com/psu-stewardship/OpenCASA].

We plan to implement OpenCASA services in the (Python programming language)[http://www.python.org/], leveraging (OpenSRF)[http://www.open-ils.org/dokuwiki/doku.php?id=osrf-devel:user_s_guide] atop the open (XMPP standard)[http://en.wikipedia.org/wiki/Extensible_Messaging_and_Presence_Protocol] as our message broker and service architecture.

