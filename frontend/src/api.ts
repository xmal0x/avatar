const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

export async function apiHello() {
  const res = await fetch(`${API_URL}/api/hello`)
  if (!res.ok) throw new Error('API error')
  return res.json() as Promise<{ message: string }>
}

export async function apiTime() {
  const res = await fetch(`${API_URL}/api/time`)
  if (!res.ok) throw new Error('API error')
  return res.json() as Promise<{ now: string }>
}

export async function apiMessage(message: string) {
  const res = await fetch(`${API_URL}/api/message`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  })
  if (!res.ok) throw new Error('API error')
  return res.json() as Promise<{ result: string }>
}