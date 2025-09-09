import { http } from '../../../shared/api/http'

export interface Message {
  id: number
  message: string
  role: 'user' | 'agent'
}

export interface MessageCreate {
  content: string;
}

export const chatApi = {
  send: (data: MessageCreate) => http.post<{ result: string }>('/api/message', data)
}