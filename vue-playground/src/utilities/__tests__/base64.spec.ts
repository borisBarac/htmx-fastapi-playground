import { describe, it, expect } from 'vitest'
import { encodeBase64 } from '../base64encoder'

describe('encodeBase64 functions', () => {
  it('we need to make sure we are matching the same format of the server', () => {
    const str =
      '<!doctypehtml><html lang=en><meta charset=UTF-8><meta content="width=device-width,initial-scale=1"name=viewport><title>My Website</title><link href=style.css rel=stylesheet><h1>Welcome to My Website!</h1><p>This is a paragraph containing some content for the page.<ul><li>Item 1 in the list<li>Item 2 in the list<li>Item 3 in the list</ul><img alt="Image description"src=image.jpg> <a href=https://www.example.com>Visit an External Link</a><form action=/submit method=post><label for=name>Name:</label> <input id=name name=name required><br><label for=email>Email:</label> <input id=email name=email required type=email><br><button type=submit>Submit</button></form>'
    const serverEncode =
      'PCFkb2N0eXBlaHRtbD48aHRtbCBsYW5nPWVuPjxtZXRhIGNoYXJzZXQ9VVRGLTg+PG1ldGEgY29udGVudD0id2lkdGg9ZGV2aWNlLXdpZHRoLGluaXRpYWwtc2NhbGU9MSJuYW1lPXZpZXdwb3J0Pjx0aXRsZT5NeSBXZWJzaXRlPC90aXRsZT48bGluayBocmVmPXN0eWxlLmNzcyByZWw9c3R5bGVzaGVldD48aDE+V2VsY29tZSB0byBNeSBXZWJzaXRlITwvaDE+PHA+VGhpcyBpcyBhIHBhcmFncmFwaCBjb250YWluaW5nIHNvbWUgY29udGVudCBmb3IgdGhlIHBhZ2UuPHVsPjxsaT5JdGVtIDEgaW4gdGhlIGxpc3Q8bGk+SXRlbSAyIGluIHRoZSBsaXN0PGxpPkl0ZW0gMyBpbiB0aGUgbGlzdDwvdWw+PGltZyBhbHQ9IkltYWdlIGRlc2NyaXB0aW9uInNyYz1pbWFnZS5qcGc+IDxhIGhyZWY9aHR0cHM6Ly93d3cuZXhhbXBsZS5jb20+VmlzaXQgYW4gRXh0ZXJuYWwgTGluazwvYT48Zm9ybSBhY3Rpb249L3N1Ym1pdCBtZXRob2Q9cG9zdD48bGFiZWwgZm9yPW5hbWU+TmFtZTo8L2xhYmVsPiA8aW5wdXQgaWQ9bmFtZSBuYW1lPW5hbWUgcmVxdWlyZWQ+PGJyPjxsYWJlbCBmb3I9ZW1haWw+RW1haWw6PC9sYWJlbD4gPGlucHV0IGlkPWVtYWlsIG5hbWU9ZW1haWwgcmVxdWlyZWQgdHlwZT1lbWFpbD48YnI+PGJ1dHRvbiB0eXBlPXN1Ym1pdD5TdWJtaXQ8L2J1dHRvbj48L2Zvcm0+'

    const feEncode = encodeBase64(str)
    expect(feEncode === serverEncode).toBe(true)
  })
})
