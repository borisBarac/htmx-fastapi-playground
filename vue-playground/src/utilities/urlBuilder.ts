const domain = 'http://localhost:8000'

export const CallType = {
  GET: 'GET',
  POST: 'POST',
  PUT: 'PUT',
  PATCH: 'PATCH',
  DELETE: 'DELETE'
} as const
export type CallType = (typeof CallType)[keyof typeof CallType]

export const QueryType = {
  URL: 'URL',
  BODY: 'BODY'
} as const
export type QueryType = (typeof QueryType)[keyof typeof QueryType]

export const Endpoints = {
  root: '/',
  render: '/render'
} as const
export type Endpoints = (typeof Endpoints)[keyof typeof Endpoints]

export const IframeRoute = (path: Endpoints, queryParams: Record<string, string>) => {
  return {
    path: path,
    queryParams: queryParams,
    callType: CallType.GET,
    bodyType: QueryType.BODY
  } as const
}
export type IframeRoute = ReturnType<typeof IframeRoute>

export const buldWebPathFor = (route: IframeRoute) => {
  const { path, queryParams } = route

  let queryString = ''
  for (const key in queryParams) {
    const value = queryParams[key]
    queryString += `${key}=${value}&`
  }

  const baseUrl = `${domain}${path}`

  if (Object.keys(queryParams).length) {
    const queryStringWithoutLastAmpersand = queryString.slice(0, -1)
    return `${baseUrl}?${queryStringWithoutLastAmpersand}`
  } else {
    return baseUrl
  }
}
