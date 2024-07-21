export type MonacoThemesEnum = 'vs-dark' | 'vs'
export type CodeLanguages = 'json' | 'html'
export type PanelType = 'editor' | 'preview'

export const CodeLangApiParamMap: Record<CodeLanguages, string> = {
  json: 'template_state_base64',
  html: 'template_html_base64'
} as const
export type CallType = (typeof CodeLangApiParamMap)[keyof typeof CodeLangApiParamMap]

export enum ProviderEvents {
  Reload = 'ProviderEventsReloadEvent'
}

export const initJson: string = `{"websiteName": "My Website"}`
export const initHtml: string = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Simple Website</title>
</head>
<body>
  <h1>Welcome to {{websiteName}}.</h1>
  <p>This is a simple paragraph containing some introductory text.</p>
  <ul>
    <li>Item 1 in an unordered list</li>
    <li>Item 2 in the list</li>
  </ul>
  <img src="image.jpg" alt="Image description">
  <a href="https://www.example.com">Link to another website</a>
</body>
</html>`
