const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export const http = {
  async post<T>(path: string, body: any): Promise<T> {
    const res = await fetch(`${API_URL}${path}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    })
    if (!res.ok) throw new Error('API error')
    return res.json() as Promise<T>
  }
}