import { serve } from 'https://deno.land/std/http/server.ts'
const s = serve({ port: 3000 })

const HTMLHEAD = `
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Welcome</title>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <meta content="width=device-width, initial-scale=1" name="viewport" />
    </head>
    <body>
        <form action="" method="get">
`
const HTMLFOOT = `
            <p>Input Your Name: <input type="text" name="name" /></p>
            <p><input type="submit" /></p>
        </form>
    </body>
`

for await (const req of s) {
  let grt = "<h1>Welcome, anonymous.</h1>"
  const url = new URL(req.url, 'http://example.com/')
  const name = url.searchParams.get('name')
  if (name !== null && name!.length > 0) {
    grt = "<h1>Hello, " + name! + "</h1>"
  }
  req.respond({ body: HTMLHEAD + grt + HTMLFOOT })
}
