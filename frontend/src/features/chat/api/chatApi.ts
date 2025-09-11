import { http } from '../../../shared/api/http'

export interface Message {
  id: number
  message: string
  role: 'user' | 'assistant'
}

export interface MessageCreate {
  content: string;
}

export interface MessageResponse {
content: string;
created_at: string;
id: number;
role: 'assistant' | 'user';
}

export const chatApi = {
  send: (data: MessageCreate) => http.post<MessageResponse>('/api/v1/messages', data)
}