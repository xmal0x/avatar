import { http } from '../../../shared/api/http'

export interface Message {
  message: string
}

export const chatApi = {
  send: (data: Message) => http.post<{ result: string }>('/api/message', data)
}